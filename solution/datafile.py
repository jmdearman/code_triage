import os.path
import collections
import h5py
import astropy.units as u

class DataFile(collections.Mapping):
    def __init__(self, filename):
        if not os.path.isfile(filename):
            raise ValueError('File does not exist at {}.'.format(filename))
    	self.filename = filename
    	self.f = h5py.File(filename)

    def __repr__(self):
    	return '{}({})'.format(self.__class__.__name__, self.filename)

    def __getitem__(self, key):
    	ds = self.f[key]
    	return u.Quantity(ds, ds.attrs['unit'])

    def __iter__(self):
    	return iter(self.f)

    def __len__(self):
    	return len(self.f)
