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


from .BusinessMixin import BusinessMixin

class BusinessDay(BusinessMixin):
    """
    DateOffset subclass representing possibly n business days.
    
        Parameters
        ----------
        n : int, default 1
            The number of days represented.
        normalize : bool, default False
            Normalize start/end dates to midnight.
    
        Examples
        --------
        You can use the parameter ``n`` to represent a shift of n business days.
    
        >>> ts = pd.Timestamp(2022, 12, 9, 15)
        >>> ts.strftime('%a %d %b %Y %H:%M')
        'Fri 09 Dec 2022 15:00'
        >>> (ts + pd.offsets.BusinessDay(n=5)).strftime('%a %d %b %Y %H:%M')
        'Fri 16 Dec 2022 15:00'
    
        Passing the parameter ``normalize`` equal to True, you shift the start
        of the next business day to midnight.
    
        >>> ts = pd.Timestamp(2022, 12, 9, 15)
        >>> ts + pd.offsets.BusinessDay(normalize=True)
        Timestamp('2022-12-12 00:00:00')
    """
    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _apply_array(self, *args, **kwargs): # real signature unknown
        pass

    def _offset_str(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, n=5): # real signature unknown; restored from __doc__
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
        'offset',
    )
    _period_dtype_code = 5000
    _prefix = 'B'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7874c3905a70>'


