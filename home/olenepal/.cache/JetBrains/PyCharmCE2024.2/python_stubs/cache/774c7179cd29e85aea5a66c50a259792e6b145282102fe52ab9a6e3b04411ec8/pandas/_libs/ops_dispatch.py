# encoding: utf-8
# module pandas._libs.ops_dispatch
# from /home/olenepal/.local/lib/python3.10/site-packages/pandas/_libs/ops_dispatch.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def maybe_dispatch_ufunc_to_dunder_op(*args, **kwargs): # real signature unknown
    """
    Dispatch a ufunc to the equivalent dunder method.
    
        Parameters
        ----------
        self : ArrayLike
            The array whose dunder method we dispatch to
        ufunc : Callable
            A NumPy ufunc
        method : {'reduce', 'accumulate', 'reduceat', 'outer', 'at', '__call__'}
        inputs : ArrayLike
            The input arrays.
        kwargs : Any
            The additional keyword arguments, e.g. ``out``.
    
        Returns
        -------
        result : Any
            The result of applying the ufunc
    """
    pass

# no classes
# variables with complex values

DISPATCHED_UFUNCS = None # (!) real value is "{'floordiv', 'pos', 'gt', 'mul', 'xor', 'divmod', 'or', 'le', 'neg', 'pow', 'add', 'truediv', 'remainder', 'ne', 'matmul', 'eq', 'abs', 'lt', 'and', 'mod', 'sub', 'ge'}"

REVERSED_NAMES = {
    'eq': '__eq__',
    'ge': '__le__',
    'gt': '__lt__',
    'le': '__ge__',
    'lt': '__gt__',
    'ne': '__ne__',
}

UFUNC_ALIASES = {
    'absolute': 'abs',
    'bitwise_and': 'and',
    'bitwise_or': 'or',
    'bitwise_xor': 'xor',
    'divide': 'truediv',
    'equal': 'eq',
    'floor_divide': 'floordiv',
    'greater': 'gt',
    'greater_equal': 'ge',
    'less': 'lt',
    'less_equal': 'le',
    'multiply': 'mul',
    'negative': 'neg',
    'not_equal': 'ne',
    'positive': 'pos',
    'power': 'pow',
    'remainder': 'mod',
    'subtract': 'sub',
    'true_divide': 'truediv',
}

UNARY_UFUNCS = None # (!) real value is "{'abs', 'pos', 'neg'}"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7874c48fe7d0>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.ops_dispatch', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7874c48fe7d0>, origin='/home/olenepal/.local/lib/python3.10/site-packages/pandas/_libs/ops_dispatch.cpython-310-x86_64-linux-gnu.so')"

__test__ = {}

