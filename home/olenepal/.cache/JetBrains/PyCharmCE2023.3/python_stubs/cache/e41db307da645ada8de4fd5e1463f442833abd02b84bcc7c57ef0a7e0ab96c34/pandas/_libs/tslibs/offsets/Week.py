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

class Week(SingleConstructorOffset):
    """
    Weekly offset.
    
        Parameters
        ----------
        weekday : int or None, default None
            Always generate specific day of week.
            0 for Monday and 6 for Sunday.
    
        See Also
        --------
        pd.tseries.offsets.WeekOfMonth :
         Describes monthly dates like, the Tuesday of the
         2nd week of each month.
    
        Examples
        --------
    
        >>> date_object = pd.Timestamp("2023-01-13")
        >>> date_object
        Timestamp('2023-01-13 00:00:00')
    
        >>> date_plus_one_week = date_object + pd.tseries.offsets.Week(n=1)
        >>> date_plus_one_week
        Timestamp('2023-01-20 00:00:00')
    
        >>> date_next_monday = date_object + pd.tseries.offsets.Week(weekday=0)
        >>> date_next_monday
        Timestamp('2023-01-16 00:00:00')
    
        >>> date_next_sunday = date_object + pd.tseries.offsets.Week(weekday=6)
        >>> date_next_sunday
        Timestamp('2023-01-15 00:00:00')
    """
    def is_anchored(self, *args, **kwargs): # real signature unknown
        pass

    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _apply_array(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _from_name(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, n=1): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    rule_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weekday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _period_dtype_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _attributes = (
        'n',
        'normalize',
        'weekday',
    )
    _inc = datetime.timedelta(days=7)
    _prefix = 'W'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fd2ef2aa190>'


