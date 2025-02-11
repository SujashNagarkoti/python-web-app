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

class BYearBegin(YearOffset):
    """
    DateOffset increments between the first business day of the year.
    
        Parameters
        ----------
        n : int, default 1
            The number of years represented.
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
        month : int, default 1
            A specific integer for the month of the year.
    
        See Also
        --------
        :class:`~pandas.tseries.offsets.DateOffset` : Standard kind of date increment.
    
        Examples
        --------
        >>> from pandas.tseries.offsets import BYearBegin
        >>> ts = pd.Timestamp('2020-05-24 05:01:15')
        >>> ts + BYearBegin()
        Timestamp('2021-01-01 05:01:15')
        >>> ts - BYearBegin()
        Timestamp('2020-01-01 05:01:15')
        >>> ts + BYearBegin(-1)
        Timestamp('2020-01-01 05:01:15')
        >>> ts + BYearBegin(2)
        Timestamp('2022-01-03 05:01:15')
        >>> ts + BYearBegin(month=11)
        Timestamp('2020-11-02 05:01:15')
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _day_opt = 'business_start'
    _default_month = 1
    _outputName = 'BusinessYearBegin'
    _prefix = 'BAS'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7874c3905c20>'


