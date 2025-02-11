# encoding: utf-8
# module pandas._libs.index
# from /home/olenepal/.local/lib/python3.10/site-packages/pandas/_libs/index.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /home/olenepal/.local/lib/python3.10/site-packages/numpy/__init__.py
import pandas._libs.algos as algos # /home/olenepal/.local/lib/python3.10/site-packages/pandas/_libs/algos.cpython-310-x86_64-linux-gnu.so
import pandas._libs.hashtable as _hash # /home/olenepal/.local/lib/python3.10/site-packages/pandas/_libs/hashtable.cpython-310-x86_64-linux-gnu.so

from .object import object

class BaseMultiIndexCodesEngine(object):
    """
    Base class for MultiIndexUIntEngine and MultiIndexPyIntEngine, which
        represent each label in a MultiIndex as an integer, by juxtaposing the bits
        encoding each level, with appropriate offsets.
    
        For instance: if 3 levels have respectively 3, 6 and 1 possible values,
        then their labels can be represented using respectively 2, 3 and 1 bits,
        as follows:
         _ _ _ _____ _ __ __ __
        |0|0|0| ... |0| 0|a1|a0| -> offset 0 (first level)
         — — — ————— — —— —— ——
        |0|0|0| ... |0|b2|b1|b0| -> offset 2 (bits required for first level)
         — — — ————— — —— —— ——
        |0|0|0| ... |0| 0| 0|c0| -> offset 5 (bits required for first two levels)
         ‾ ‾ ‾ ‾‾‾‾‾ ‾ ‾‾ ‾‾ ‾‾
        and the resulting unsigned integer representation will be:
         _ _ _ _____ _ __ __ __ __ __ __
        |0|0|0| ... |0|c0|b2|b1|b0|a1|a0|
         ‾ ‾ ‾ ‾‾‾‾‾ ‾ ‾‾ ‾‾ ‾‾ ‾‾ ‾‾ ‾‾
    
        Offsets are calculated at initialization, labels are transformed by method
        _codes_to_ints.
    
        Keys are located by first locating each component against the respective
        level, then locating (the integer representation of) codes.
    """
    def get_indexer(self, *args, **kwargs): # real signature unknown
        """
        Returns an array giving the positions of each value of `target` in
                `self.values`, where -1 represents a value in `target` which does not
                appear in `self.values`
        
                Parameters
                ----------
                target : np.ndarray
        
                Returns
                -------
                np.ndarray[intp_t, ndim=1] of the indexer of `target` into
                `self.values`
        """
        pass

    def get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer_with_fill(self, *args, **kwargs): # real signature unknown
        """
        Returns an array giving the positions of each value of `target` in
                `values`, where -1 represents a value in `target` which does not
                appear in `values`
        
                If `method` is "backfill" then the position for a value in `target`
                which does not appear in `values` is that of the next greater value
                in `values` (if one exists), and -1 if there is no such value.
        
                Similarly, if the method is "pad" then the position for a value in
                `target` which does not appear in `values` is that of the next smaller
                value in `values` (if one exists), and -1 if there is no such value.
        
                Parameters
                ----------
                target: ndarray[object] of tuples
                    need not be sorted, but all must have the same length, which must be
                    the same as the length of all tuples in `values`
                values : ndarray[object] of tuples
                    must be sorted and all have the same length.  Should be the set of
                    the MultiIndex's values.
                method: string
                    "backfill" or "pad"
                limit: int or None
                    if provided, limit the number of fills to this value
        
                Returns
                -------
                np.ndarray[intp_t, ndim=1] of the indexer of `target` into `values`,
                filled with the `method` (and optionally `limit`) specified
        """
        pass

    def get_loc(self, *args, **kwargs): # real signature unknown
        pass

    def _codes_to_ints(self, *args, **kwargs): # real signature unknown
        pass

    def _extract_level_codes(self, *args, **kwargs): # real signature unknown
        """
        Map the requested list of (tuple) keys to their integer representations
                for searching in the underlying integer index.
        
                Parameters
                ----------
                target : MultiIndex
        
                Returns
                ------
                int_keys : 1-dimensional array of dtype uint64 or object
                    Integers representing one combination each
        """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Parameters
                ----------
                levels : list-like of numpy arrays
                    Levels of the MultiIndex.
                labels : list-like of numpy arrays of integer dtype
                    Labels of the MultiIndex.
                offsets : numpy array of uint64 dtype
                    Pre-calculated offsets, one for each level of the index.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


