# encoding: utf-8
# module pandas._libs.tslibs.offsets
# from /home/olenepal/.local/lib/python3.10/site-packages/pandas/_libs/tslibs/offsets.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import re as re # /usr/lib/python3.10/re.py
import time as time # <module 'time' (built-in)>
import numpy as np # /home/olenepal/.local/lib/python3.10/site-packages/numpy/__init__.py
from pandas._libs.properties import cache_readonly

from pandas._libs.tslibs.timedeltas import Timedelta

from pandas._libs.tslibs.timestamps import Timestamp


from .SingleConstructorOffset import SingleConstructorOffset

class BusinessMixin(SingleConstructorOffset):
    """ Mixin to business types to provide related functions. """
    def _init_custom(self, *args, **kwargs): # real signature unknown
        """ Additional __init__ for Custom subclasses. """
        pass

    def _repr_attrs(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    calendar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    holidays = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Alias for self._offset.
        """

    weekmask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7874c3905a10>'


