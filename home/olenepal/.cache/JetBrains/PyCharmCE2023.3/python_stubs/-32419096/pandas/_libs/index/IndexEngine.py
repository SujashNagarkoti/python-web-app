# encoding: utf-8
# module pandas._libs.index
# from /home/olenepal/.local/lib/python3.10/site-packages/pandas/_libs/index.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /home/olenepal/.local/lib/python3.10/site-packages/numpy/__init__.py
import pandas._libs.algos as algos # /home/olenepal/.local/lib/python3.10/site-packages/pandas/_libs/algos.cpython-310-x86_64-linux-gnu.so
import pandas._libs.hashtable as _hash # /home/olenepal/.local/lib/python3.10/site-packages/pandas/_libs/hashtable.cpython-310-x86_64-linux-gnu.so

from .object import object

class IndexEngine(object):
    # no doc
    def clear_mapping(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        Return an indexer suitable for taking from a non unique index
                return the labels in the same order as the target
                and a missing indexer into the targets (which correspond
                to the -1 indices in the results
        
                Returns
                -------
                indexer : np.ndarray[np.intp]
                missing : np.ndarray[np.intp]
        """
        pass

    def get_loc(self, *args, **kwargs): # real signature unknown
        pass

    def sizeof(self, *args, **kwargs): # real signature unknown
        """ return the sizeof our mapping """
        pass

    def _update_from_sliced(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass

    is_mapping_populated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_monotonic_decreasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_monotonic_increasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_unique = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    over_size_threshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fd2ee2c8270>'


