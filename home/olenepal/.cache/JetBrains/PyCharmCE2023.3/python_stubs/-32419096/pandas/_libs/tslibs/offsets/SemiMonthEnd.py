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

class SemiMonthEnd(SemiMonthOffset):
    """
    Two DateOffset's per month repeating on the last day of the month & day_of_month.
    
        Parameters
        ----------
        n : int
        normalize : bool, default False
        day_of_month : int, {1, 3,...,27}, default 15
    
        Examples
        --------
        >>> ts = pd.Timestamp(2022, 1, 14)
        >>> ts + pd.offsets.SemiMonthEnd()
        Timestamp('2022-01-15 00:00:00')
    
        >>> ts = pd.Timestamp(2022, 1, 15)
        >>> ts + pd.offsets.SemiMonthEnd()
        Timestamp('2022-01-31 00:00:00')
    
        >>> ts = pd.Timestamp(2022, 1, 31)
        >>> ts + pd.offsets.SemiMonthEnd()
        Timestamp('2022-02-15 00:00:00')
    
        If you want to get the result for the current month:
    
        >>> ts = pd.Timestamp(2022, 1, 15)
        >>> pd.offsets.SemiMonthEnd().rollforward(ts)
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

    _min_day_of_month = 1
    _prefix = 'SM'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fd2ef2aa0d0>'


