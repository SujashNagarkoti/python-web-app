# encoding: utf-8
# module pandas._libs.tslibs.np_datetime
# from /home/olenepal/.local/lib/python3.10/site-packages/pandas/_libs/tslibs/np_datetime.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /home/olenepal/.local/lib/python3.10/site-packages/numpy/__init__.py
import operator as operator # /usr/lib/python3.10/operator.py

# functions

def astype_overflowsafe(*args, **kwargs): # real signature unknown
    """
    Convert an ndarray with datetime64[X] to datetime64[Y]
        or timedelta64[X] to timedelta64[Y],
        raising on overflow.
    """
    pass

def compare_mismatched_resolutions(*args, **kwargs): # real signature unknown
    """
    Overflow-safe comparison of timedelta64/datetime64 with mismatched resolutions.
    
        >>> left = np.array([500], dtype="M8[Y]")
        >>> right = np.array([0], dtype="M8[ns]")
        >>> left < right  # <- wrong!
        array([ True])
    """
    pass

def is_unitless(*args, **kwargs): # real signature unknown
    """ Check if a datetime64 or timedelta64 dtype has no attached unit. """
    pass

def py_get_unit_from_dtype(*args, **kwargs): # real signature unknown
    pass

def py_td64_to_tdstruct(*args, **kwargs): # real signature unknown
    pass

# classes

class OutOfBoundsDatetime(ValueError):
    """
    Raised when the datetime is outside the range that can be represented.
    
        Examples
        --------
        >>> pd.to_datetime("08335394550")
        Traceback (most recent call last):
        OutOfBoundsDatetime: Parsing "08335394550" to datetime overflows,
        at position 0
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class OutOfBoundsTimedelta(ValueError):
    """
    Raised when encountering a timedelta value that cannot be represented.
    
        Representation should be within a timedelta64[ns].
    
        Examples
        --------
        >>> pd.date_range(start="1/1/1700", freq="B", periods=100000)
        Traceback (most recent call last):
        OutOfBoundsTimedelta: Cannot cast 139999 days 00:00:00
        to unit='ns' without overflow.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7874c48ff220>'

__pyx_capi__ = {
    'astype_overflowsafe': None, # (!) real value is '<capsule object "PyArrayObject *(PyArrayObject *, PyArray_Descr *, int __pyx_skip_dispatch, struct __pyx_opt_args_6pandas_5_libs_6tslibs_11np_datetime_astype_overflowsafe *__pyx_optional_args)" at 0x7874c48ff570>'
    'check_dts_bounds': None, # (!) real value is '<capsule object "PyObject *(npy_datetimestruct *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_11np_datetime_check_dts_bounds *__pyx_optional_args)" at 0x7874c48ff390>'
    'cmp_dtstructs': None, # (!) real value is '<capsule object "int (npy_datetimestruct *, npy_datetimestruct *, int)" at 0x7874c48ff5d0>'
    'cmp_scalar': None, # (!) real value is '<capsule object "int (__pyx_t_5numpy_int64_t, __pyx_t_5numpy_int64_t, int)" at 0x7874c48ff360>'
    'convert_reso': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (__pyx_t_5numpy_int64_t, NPY_DATETIMEUNIT, NPY_DATETIMEUNIT, int)" at 0x7874c48ff630>'
    'get_conversion_factor': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (NPY_DATETIMEUNIT, NPY_DATETIMEUNIT)" at 0x7874c48ff5a0>'
    'get_datetime64_unit': None, # (!) real value is '<capsule object "NPY_DATETIMEUNIT (PyObject *)" at 0x7874c48ff4e0>'
    'get_datetime64_value': None, # (!) real value is '<capsule object "npy_datetime (PyObject *)" at 0x7874c48ff480>'
    'get_implementation_bounds': None, # (!) real value is '<capsule object "PyObject *(NPY_DATETIMEUNIT, npy_datetimestruct *, npy_datetimestruct *)" at 0x7874c48ff600>'
    'get_timedelta64_value': None, # (!) real value is '<capsule object "npy_timedelta (PyObject *)" at 0x7874c48ff4b0>'
    'get_unit_from_dtype': None, # (!) real value is '<capsule object "NPY_DATETIMEUNIT (PyArray_Descr *)" at 0x7874c48ff540>'
    'pydate_to_dt64': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyDateTime_Date *, npy_datetimestruct *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_11np_datetime_pydate_to_dt64 *__pyx_optional_args)" at 0x7874c48ff420>'
    'pydate_to_dtstruct': None, # (!) real value is '<capsule object "void (PyDateTime_Date *, npy_datetimestruct *)" at 0x7874c48ff450>'
    'pydatetime_to_dt64': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyDateTime_DateTime *, npy_datetimestruct *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_11np_datetime_pydatetime_to_dt64 *__pyx_optional_args)" at 0x7874c48ff3c0>'
    'pydatetime_to_dtstruct': None, # (!) real value is '<capsule object "void (PyDateTime_DateTime *, npy_datetimestruct *)" at 0x7874c48ff3f0>'
    'string_to_dts': None, # (!) real value is '<capsule object "int (PyObject *, npy_datetimestruct *, NPY_DATETIMEUNIT *, int *, int *, int, struct __pyx_opt_args_6pandas_5_libs_6tslibs_11np_datetime_string_to_dts *__pyx_optional_args)" at 0x7874c48ff510>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.np_datetime', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7874c48ff220>, origin='/home/olenepal/.local/lib/python3.10/site-packages/pandas/_libs/tslibs/np_datetime.cpython-310-x86_64-linux-gnu.so')"

__test__ = {
    'compare_mismatched_resolutions (line 426)': '\n    Overflow-safe comparison of timedelta64/datetime64 with mismatched resolutions.\n\n    >>> left = np.array([500], dtype="M8[Y]")\n    >>> right = np.array([0], dtype="M8[ns]")\n    >>> left < right  # <- wrong!\n    array([ True])\n    ',
}

