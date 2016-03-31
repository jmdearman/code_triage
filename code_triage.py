#!/usr/bin/env python2
from __future__ import division, print_function
import collections
import os
import numpy as np
import h5py

header_text = """
INTRO TO ANTIPATTERNS IN SCIENTIFIC COMPUTING PART I: CODE TRIAGE
-----------------------------------------------------------------
"""

intro_text = """
You are an engineer at NASA.

You've told all of your colleagues how awesome Python is, and you managed to
convince your friend, Marty, to check it out.

Marty works on the Guidance team for NASA's next generation space capsule.

He's working on some code to assess landing performance against 2 metrics:
    1. The capsule must splashdown within a given range to the target site.      
    2. To be extra safe, there's also a keep-out zone to let the Navy
       know where to park the recovery ship out of harms way.

Marty is having trouble with the code he wrote this morning.
"""

message_text = """
================================================================================
Subject: Python Bug
From: Marty McFly
================================================================================

Dear Colleague,

I was initially really excited about this Python thing you showed me last week.
I read PEP8 and translated my code from MATLAB, but my second ellipse is
coming out wrong (too small).

Do you think there's a bug in Python?

I attached a copy of my code (marty.py) and the data file (touchdown_data.h5).

Cheers,
-Marty

P.S. Can you give me any pointers on how I can improve my code?
"""

end_text = """
CODE TRIAGE WRAP-UP
-------------------
- use __future__ to get Python 3 integer division (return floats)
- use astropy.units instead of rolling your own conversions
- define functions or use iteration to avoid repetition (DRY)
- vectorize computational for-loops with numpy
- use adapter classes to improve workflow
- sign up for INTRO TO ANTIPATTERNS IN SCIENTIFIC COMPUTING PART II

LINKS
-----
- Raymond Hettinger: Beyond PEP 8
    https://youtu.be/wf-BqAjZb8M
- Katherine D. Huff & Anthony Scopatz: Effective Computation in Physics
    https://youtu.be/Qc9035gw2OQ
- Erik Rose: Designing Poetic APIs
    https://youtu.be/JQYnFyG7A8c
"""

def configure():
    """Generate data for Code Triage."""
    Variable = collections.namedtuple('Variable', ('name', 'sigma', 'unit'))

    filename = 'touchdown_data.h5'
    nruns = 10000
    seed = 0

    variables = [
        Variable('miss_x', 2000, 'm'),
        Variable('miss_y',  500, 'm'),
        Variable('velocity_x', 5, 'm/s'),
        Variable('velocity_y', 4, 'm/s'),
        Variable('velocity_z', 8, 'm/s'),
        Variable('yaw', .1, 'rad'),
        Variable('pitch', .2, 'rad'),
        Variable('roll', .5, 'rad'),
        Variable('wind_x', 5, 'm/s'),
        Variable('wind_y', 4, 'm/s'),
        Variable('wind_z', 1, 'm/s')
        ]

    rs = np.random.RandomState(seed)  # seed the random number generator

    with h5py.File(filename, 'w') as f:
        for v in variables:
            ds = f.create_dataset(v.name, data=v.sigma*rs.randn(nruns))
            ds.attrs['unit'] = v.unit

def start():
    """Show intro messages."""
    configure()
    clear()
    print(header_text, end='')
    raw_input()
    print(intro_text)
    raw_input('Press return to check your email...')
    clear()
    print(message_text)

def end():
    """Show wrap up message."""
    clear()
    print(end_text)

def clear():
    """Clear the screen."""
    os.system('clear')

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='python adventure game',
                                     add_help=False)
    parser.add_argument('action', choices=('help', 'start', 'end', 'configure'),
                        help='action', nargs='?', default='help')
    args = parser.parse_args()

    if args.action == 'configure':
        configure()
    elif args.action == 'start':
        start()
    elif args.action == 'end':
        end()
    elif args.action == 'help':
        parser.print_help()
