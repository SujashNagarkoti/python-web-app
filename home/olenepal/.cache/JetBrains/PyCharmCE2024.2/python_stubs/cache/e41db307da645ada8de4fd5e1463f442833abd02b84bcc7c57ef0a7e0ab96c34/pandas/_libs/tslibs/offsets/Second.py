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

class Second(Tick):
    """
    Offset ``n`` seconds.
    
        Parameters
        ----------
        n : int, default 1
            The number of seconds represented.
    
        See Also
        --------
        :class:`~pandas.tseries.offsets.DateOffset` : Standard kind of date increment.
    
        Examples
        --------
        You can use the parameter ``n`` to represent a shift of n seconds.
    
        >>> from pandas.tseries.offsets import Second
        >>> ts = pd.Timestamp(2022, 12, 9, 15)
        >>> ts
        Timestamp('2022-12-09 15:00:00')
    
        >>> ts + Second(n=10)
        Timestamp('2022-12-09 15:00:10')
        >>> ts - Second(n=10)
        Timestamp('2022-12-09 14:59:50')
    
        >>> ts + Second(n=-10)
        Timestamp('2022-12-09 14:59:50')
    """
    def __init__(self, n=10): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _creso = 7
    _nanos_inc = 1000000000
    _period_dtype_code = 9000
    _prefix = 'S'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7874c3905860>'


