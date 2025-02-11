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


from .Tick import Tick

class Hour(Tick):
    """
    Offset ``n`` hours.
    
        Parameters
        ----------
        n : int, default 1
            The number of hours represented.
    
        See Also
        --------
        :class:`~pandas.tseries.offsets.DateOffset` : Standard kind of date increment.
    
        Examples
        --------
        You can use the parameter ``n`` to represent a shift of n hours.
    
        >>> from pandas.tseries.offsets import Hour
        >>> ts = pd.Timestamp(2022, 12, 9, 15)
        >>> ts
        Timestamp('2022-12-09 15:00:00')
    
        >>> ts + Hour()
        Timestamp('2022-12-09 16:00:00')
        >>> ts - Hour(4)
        Timestamp('2022-12-09 11:00:00')
    
        >>> ts + Hour(-4)
        Timestamp('2022-12-09 11:00:00')
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _creso = 5
    _nanos_inc = 3600000000000
    _period_dtype_code = 7000
    _prefix = 'H'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7874c39057a0>'


