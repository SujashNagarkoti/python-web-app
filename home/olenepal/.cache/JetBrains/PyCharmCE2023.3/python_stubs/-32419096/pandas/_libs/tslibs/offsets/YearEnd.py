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


from .YearOffset import YearOffset

class YearEnd(YearOffset):
    """
    DateOffset increments between calendar year end dates.
    
        YearEnd goes to the next date which is the end of the year.
    
        Parameters
        ----------
        n : int, default 1
            The number of years represented.
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
        month : int, default 12
            A specific integer for the month of the year.
    
        See Also
        --------
        :class:`~pandas.tseries.offsets.DateOffset` : Standard kind of date increment.
    
        Examples
        --------
        >>> ts = pd.Timestamp(2022, 1, 1)
        >>> ts + pd.offsets.YearEnd()
        Timestamp('2022-12-31 00:00:00')
    
        >>> ts = pd.Timestamp(2022, 12, 31)
        >>> ts + pd.offsets.YearEnd()
        Timestamp('2023-12-31 00:00:00')
    
        >>> ts = pd.Timestamp(2022, 1, 1)
        >>> ts + pd.offsets.YearEnd(month=2)
        Timestamp('2022-02-28 00:00:00')
    
        If you want to get the end of the current year:
    
        >>> ts = pd.Timestamp(2022, 12, 31)
        >>> pd.offsets.YearEnd().rollforward(ts)
        Timestamp('2022-12-31 00:00:00')
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _period_dtype_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _day_opt = 'end'
    _default_month = 12
    _prefix = 'A'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fd2ef2a9bf0>'


