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

class _CustomBusinessMonth(BusinessMixin):
    """
    DateOffset subclass representing custom business month(s).
    
        Increments between beginning/end of month dates.
    
        Parameters
        ----------
        n : int, default 1
            The number of months represented.
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
        weekmask : str, Default 'Mon Tue Wed Thu Fri'
            Weekmask of valid business days, passed to ``numpy.busdaycalendar``.
        holidays : list
            List/array of dates to exclude from the set of valid business days,
            passed to ``numpy.busdaycalendar``.
        calendar : np.busdaycalendar
            Calendar to integrate.
        offset : timedelta, default timedelta(0)
            Time offset to apply.
    """
    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    cbday_roll = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x7fd30470ab40>'
    month_roll = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x7fd2ef362180>'
    m_offset = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x7fd2ef2e2e40>'
    _attributes = (
        'n',
        'normalize',
        'weekmask',
        'holidays',
        'calendar',
        'offset',
    )
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fd2ef2aa4f0>'


