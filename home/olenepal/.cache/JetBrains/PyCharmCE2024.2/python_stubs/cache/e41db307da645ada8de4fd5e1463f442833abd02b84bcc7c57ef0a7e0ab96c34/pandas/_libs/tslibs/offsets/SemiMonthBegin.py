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


from .SemiMonthOffset import SemiMonthOffset

class SemiMonthBegin(SemiMonthOffset):
    """
    Two DateOffset's per month repeating on the first day of the month & day_of_month.
    
        Parameters
        ----------
        n : int
        normalize : bool, default False
        day_of_month : int, {2, 3,...,27}, default 15
    
        Examples
        --------
        >>> ts = pd.Timestamp(2022, 1, 1)
        >>> ts + pd.offsets.SemiMonthBegin()
        Timestamp('2022-01-15 00:00:00')
    """
    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _prefix = 'SMS'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7874c39061c0>'


