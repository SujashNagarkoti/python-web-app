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

class FY5253Mixin(SingleConstructorOffset):
    # no doc
    def get_rule_code_suffix(self, *args, **kwargs): # real signature unknown
        pass

    def is_anchored(self, *args, **kwargs): # real signature unknown
        pass

    def _get_suffix_prefix(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    rule_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    startingMonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    variation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weekday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fd2ef2aa2b0>'


