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


from .WeekOfMonthMixin import WeekOfMonthMixin

class LastWeekOfMonth(WeekOfMonthMixin):
    """
    Describes monthly dates in last week of month.
    
        For example "the last Tuesday of each month".
    
        Parameters
        ----------
        n : int, default 1
        weekday : int {0, 1, ..., 6}, default 0
            A specific integer for the day of the week.
    
            - 0 is Monday
            - 1 is Tuesday
            - 2 is Wednesday
            - 3 is Thursday
            - 4 is Friday
            - 5 is Saturday
            - 6 is Sunday.
    
        Examples
        --------
        >>> ts = pd.Timestamp(2022, 1, 1)
        >>> ts + pd.offsets.LastWeekOfMonth()
        Timestamp('2022-01-31 00:00:00')
    """
    @classmethod
    def _from_name(cls, *args, **kwargs): # real signature unknown
        pass

    def _get_offset_day(self, *args, **kwargs): # real signature unknown
        """
        Find the day in the same month as other that has the same
                weekday as self.weekday and is the last such day in the month.
        
                Parameters
                ----------
                other: datetime
        
                Returns
                -------
                day: int
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    _attributes = (
        'n',
        'normalize',
        'weekday',
    )
    _prefix = 'LWOM'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fd2ef2aa250>'


