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


from .MonthOffset import MonthOffset

class MonthBegin(MonthOffset):
    """
    DateOffset of one month at beginning.
    
        MonthBegin goes to the next date which is a start of the month.
    
        Parameters
        ----------
        n : int, default 1
            The number of months represented.
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
    
        See Also
        --------
        :class:`~pandas.tseries.offsets.DateOffset` : Standard kind of date increment.
    
        Examples
        --------
        >>> ts = pd.Timestamp(2022, 11, 30)
        >>> ts + pd.offsets.MonthBegin()
        Timestamp('2022-12-01 00:00:00')
    
        >>> ts = pd.Timestamp(2022, 12, 1)
        >>> ts + pd.offsets.MonthBegin()
        Timestamp('2023-01-01 00:00:00')
    
        If you want to get the start of the current month:
    
        >>> ts = pd.Timestamp(2022, 12, 1)
        >>> pd.offsets.MonthBegin().rollback(ts)
        Timestamp('2022-12-01 00:00:00')
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _day_opt = 'start'
    _prefix = 'MS'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fd2ef2a9f50>'


