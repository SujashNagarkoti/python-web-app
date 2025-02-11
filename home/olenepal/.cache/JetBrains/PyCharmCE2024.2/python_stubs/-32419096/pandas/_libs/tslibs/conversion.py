# encoding: utf-8
# module pandas._libs.tslibs.conversion
# from /home/olenepal/.local/lib/python3.10/site-packages/pandas/_libs/tslibs/conversion.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /home/olenepal/.local/lib/python3.10/site-packages/numpy/__init__.py
from pandas._libs.tslibs.np_datetime import OutOfBoundsDatetime

import datetime as __datetime


# functions

def localize_pydatetime(*args, **kwargs): # real signature unknown
    """
    Take a datetime/Timestamp in UTC and localizes to timezone tz.
    
        Parameters
        ----------
        dt : datetime or Timestamp
        tz : tzinfo or None
    
        Returns
        -------
        localized : datetime or Timestamp
    """
    pass

def precision_from_unit(*args, **kwargs): # real signature unknown
    """
    Return a casting of the unit represented to nanoseconds + the precision
        to round the fractional part.
    
        Notes
        -----
        The caller is responsible for ensuring that the default value of "ns"
        takes the place of None.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class timezone(__datetime.tzinfo):
    """ Fixed offset from UTC implementation of tzinfo. """
    def dst(self, *args, **kwargs): # real signature unknown
        """ Return None. """
        pass

    def fromutc(self, *args, **kwargs): # real signature unknown
        """ datetime in UTC -> datetime in local time. """
        pass

    def tzname(self, *args, **kwargs): # real signature unknown
        """ If name is specified when timezone is created, returns the name.  Otherwise returns offset as 'UTC(+|-)HH:MM'. """
        pass

    def utcoffset(self, *args, **kwargs): # real signature unknown
        """ Return fixed offset. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getinitargs__(self, *args, **kwargs): # real signature unknown
        """ pickle support """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    max = datetime.timezone(datetime.timedelta(seconds=86340))
    min = datetime.timezone(datetime.timedelta(days=-1, seconds=60))
    utc = datetime.timezone.utc


class _TSObject(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    creso = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tzinfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7874c3900c90>'


# variables with complex values

DT64NS_DTYPE = None # (!) real value is "dtype('<M8[ns]')"

TD64NS_DTYPE = None # (!) real value is "dtype('<m8[ns]')"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7874c48ff760>'

__pyx_capi__ = {
    'cast_from_unit': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyObject *, PyObject *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10conversion_cast_from_unit *__pyx_optional_args)" at 0x7874c3900ba0>'
    'convert_datetime_to_tsobject': None, # (!) real value is '<capsule object "struct __pyx_obj_6pandas_5_libs_6tslibs_10conversion__TSObject *(PyDateTime_DateTime *, PyDateTime_TZInfo *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10conversion_convert_datetime_to_tsobject *__pyx_optional_args)" at 0x7874c3900ae0>'
    'convert_str_to_tsobject': None, # (!) real value is '<capsule object "struct __pyx_obj_6pandas_5_libs_6tslibs_10conversion__TSObject *(PyObject *, PyDateTime_TZInfo *, PyObject *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10conversion_convert_str_to_tsobject *__pyx_optional_args)" at 0x7874c3900b10>'
    'convert_timezone': None, # (!) real value is '<capsule object "PyDateTime_TZInfo *(PyDateTime_TZInfo *, PyDateTime_TZInfo *, int, int, int)" at 0x7874c3900c30>'
    'convert_to_tsobject': None, # (!) real value is '<capsule object "struct __pyx_obj_6pandas_5_libs_6tslibs_10conversion__TSObject *(PyObject *, PyDateTime_TZInfo *, PyObject *, int, int, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10conversion_convert_to_tsobject *__pyx_optional_args)" at 0x7874c3900ab0>'
    'get_datetime64_nanos': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyObject *, NPY_DATETIMEUNIT)" at 0x7874c3900b40>'
    'localize_pydatetime': None, # (!) real value is '<capsule object "PyDateTime_DateTime *(PyDateTime_DateTime *, PyDateTime_TZInfo *, int __pyx_skip_dispatch)" at 0x7874c3900b70>'
    'maybe_localize_tso': None, # (!) real value is '<capsule object "PyObject *(struct __pyx_obj_6pandas_5_libs_6tslibs_10conversion__TSObject *, PyDateTime_TZInfo *, NPY_DATETIMEUNIT)" at 0x7874c3900c00>'
    'parse_pydatetime': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyDateTime_DateTime *, npy_datetimestruct *, int)" at 0x7874c3900c60>'
    'precision_from_unit': None, # (!) real value is '<capsule object "__pyx_ctuple___dunderpyx_t_5numpy_int64_t__and_int (PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10conversion_precision_from_unit *__pyx_optional_args)" at 0x7874c3900bd0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.conversion', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7874c48ff760>, origin='/home/olenepal/.local/lib/python3.10/site-packages/pandas/_libs/tslibs/conversion.cpython-310-x86_64-linux-gnu.so')"

__test__ = {}

