# encoding: utf-8
# module pandas._libs.join
# from /home/olenepal/.local/lib/python3.10/site-packages/pandas/_libs/join.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /home/olenepal/.local/lib/python3.10/site-packages/numpy/__init__.py
from pandas._libs.algos import groupsort_indexer


# functions

def asof_join_backward_on_X_by_Y(*args, **kwargs): # real signature unknown
    pass

def asof_join_forward_on_X_by_Y(*args, **kwargs): # real signature unknown
    pass

def asof_join_nearest_on_X_by_Y(*args, **kwargs): # real signature unknown
    pass

def ffill_indexer(*args, **kwargs): # real signature unknown
    pass

def full_outer_join(*args, **kwargs): # real signature unknown
    pass

def inner_join(*args, **kwargs): # real signature unknown
    pass

def inner_join_indexer(*args, **kwargs): # real signature unknown
    """
    Two-pass algorithm for monotonic indexes. Handles many-to-one merges.
    
        Both left and right are monotonic increasing but not necessarily unique.
    """
    pass

def left_join_indexer(*args, **kwargs): # real signature unknown
    """
    Two-pass algorithm for monotonic indexes. Handles many-to-one merges.
    
        Both left and right are monotonic increasing, but at least one of them
        is non-unique (if both were unique we'd use left_join_indexer_unique).
    """
    pass

def left_join_indexer_unique(*args, **kwargs): # real signature unknown
    """ Both left and right are strictly monotonic increasing. """
    pass

def left_outer_join(*args, **kwargs): # real signature unknown
    pass

def outer_join_indexer(*args, **kwargs): # real signature unknown
    """ Both left and right are monotonic increasing but not necessarily unique. """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fd2ee2cada0>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.join', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fd2ee2cada0>, origin='/home/olenepal/.local/lib/python3.10/site-packages/pandas/_libs/join.cpython-310-x86_64-linux-gnu.so')"

__test__ = {}

