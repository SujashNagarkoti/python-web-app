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


from .QuarterOffset import QuarterOffset

class BQuarterEnd(QuarterOffset):
    """
    DateOffset increments between the last business day of each Quarter.
    
        startingMonth = 1 corresponds to dates like 1/31/2007, 4/30/2007, ...
        startingMonth = 2 corresponds to dates like 2/28/2007, 5/31/2007, ...
        startingMonth = 3 corresponds to dates like 3/30/2007, 6/29/2007, ...
    
        Parameters
        ----------
        n : int, default 1
            The number of quarters represented.
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
        startingMonth : int, default 3
            A specific integer for the month of the year from which we start quarters.
    
        See Also
        --------
        :class:`~pandas.tseries.offsets.DateOffset` : Standard kind of date increment.
    
        Examples
        --------
        >>> from pandas.tseries.offsets import BQuarterEnd
        >>> ts = pd.Timestamp('2020-05-24 05:01:15')
        >>> ts + BQuarterEnd()
        Timestamp('2020-06-30 05:01:15')
        >>> ts + BQuarterEnd(2)
        Timestamp('2020-09-30 05:01:15')
        >>> ts + BQuarterEnd(1, startingMonth=2)
        Timestamp('2020-05-29 05:01:15')
        >>> ts + BQuarterEnd(startingMonth=2)
        Timestamp('2020-05-29 05:01:15')
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _day_opt = 'business_end'
    _default_starting_month = 3
    _from_name_starting_month = 12
    _output_name = 'BusinessQuarterEnd'
    _prefix = 'BQ'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fd2ef2a9d10>'


