# encoding: utf-8
# module pandas._libs.tslibs.base
# from /home/olenepal/.local/lib/python3.10/site-packages/pandas/_libs/tslibs/base.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
"""
We define base classes that will be inherited by Timestamp, Timedelta, etc
in order to allow for fast isinstance checks without circular dependency issues.

This is analogous to core.dtypes.generic.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import datetime as __datetime


# functions

def __pyx_unpickle_ABCTimestamp(*args, **kwargs): # real signature unknown
    pass

# classes

class ABCTimestamp(__datetime.datetime):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fd2ef2a9000>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.base', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fd2ef2a9000>, origin='/home/olenepal/.local/lib/python3.10/site-packages/pandas/_libs/tslibs/base.cpython-310-x86_64-linux-gnu.so')"

__test__ = {}

