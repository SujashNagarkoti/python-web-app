# encoding: utf-8
# module pandas._libs.tslibs.parsing
# from /home/olenepal/.local/lib/python3.10/site-packages/pandas/_libs/tslibs/parsing.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" Parsing functions for datetime and datetime-like strings. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import re as re # /usr/lib/python3.10/re.py
import time as time # <module 'time' (built-in)>
import warnings as warnings # /usr/lib/python3.10/warnings.py
import numpy as np # /home/olenepal/.local/lib/python3.10/site-packages/numpy/__init__.py
from pandas._libs.tslibs.np_datetime import OutOfBoundsDatetime

from pandas._libs.tslibs.strptime import array_strptime

import datetime as __datetime
import dateutil.tz._common as __dateutil_tz__common
import decimal as __decimal


# functions

def concat_date_cols((dates, times)): # real signature unknown; restored from __doc__
    """
    Concatenates elements from numpy arrays in `date_cols` into strings.
    
        Parameters
        ----------
        date_cols : tuple[ndarray]
    
        Returns
        -------
        arr_of_rows : ndarray[object]
    
        Examples
        --------
        >>> dates=np.array(['3/31/2019', '4/31/2019'], dtype=object)
        >>> times=np.array(['11:20', '10:45'], dtype=object)
        >>> result = concat_date_cols((dates, times))
        >>> result
        array(['3/31/2019 11:20', '4/31/2019 10:45'], dtype=object)
    """
    pass

def find_stack_level(): # reliably restored by inspect
    """
    Find the first place in the stack that is not inside pandas
        (tests notwithstanding).
    """
    pass

def get_option(pat): # real signature unknown; restored from __doc__
    """
    get_option(pat)
    
    Retrieves the value of the specified option.
    
    Available options:
    
    - compute.[use_bottleneck, use_numba, use_numexpr]
    - display.[chop_threshold, colheader_justify, date_dayfirst, date_yearfirst,
      encoding, expand_frame_repr, float_format]
    - display.html.[border, table_schema, use_mathjax]
    - display.[large_repr, max_categories, max_columns, max_colwidth, max_dir_items,
      max_info_columns, max_info_rows, max_rows, max_seq_items, memory_usage,
      min_rows, multi_sparse, notebook_repr_html, pprint_nest_depth, precision,
      show_dimensions]
    - display.unicode.[ambiguous_as_wide, east_asian_width]
    - display.[width]
    - future.[infer_string]
    - io.excel.ods.[reader, writer]
    - io.excel.xls.[reader]
    - io.excel.xlsb.[reader]
    - io.excel.xlsm.[reader, writer]
    - io.excel.xlsx.[reader, writer]
    - io.hdf.[default_format, dropna_table]
    - io.parquet.[engine]
    - io.sql.[engine]
    - mode.[chained_assignment, copy_on_write, data_manager, sim_interactive,
      string_storage, use_inf_as_na]
    - plotting.[backend]
    - plotting.matplotlib.[register_converters]
    - styler.format.[decimal, escape, formatter, na_rep, precision, thousands]
    - styler.html.[mathjax]
    - styler.latex.[environment, hrules, multicol_align, multirow_align]
    - styler.render.[encoding, max_columns, max_elements, max_rows, repr]
    - styler.sparse.[columns, index]
    
    Parameters
    ----------
    pat : str
        Regexp which should match a single option.
        Note: partial matches are supported for convenience, but unless you use the
        full option name (e.g. x.y.z.option_name), your code may break in future
        versions if new options with similar names are introduced.
    
    Returns
    -------
    result : the value of the option
    
    Raises
    ------
    OptionError : if no such option exists
    
    Notes
    -----
    Please reference the :ref:`User Guide <options>` for more information.
    
    The available options with its descriptions:
    
    compute.use_bottleneck : bool
        Use the bottleneck library to accelerate if it is installed,
        the default is True
        Valid values: False,True
        [default: True] [currently: True]
    compute.use_numba : bool
        Use the numba engine option for select operations if it is installed,
        the default is False
        Valid values: False,True
        [default: False] [currently: False]
    compute.use_numexpr : bool
        Use the numexpr library to accelerate computation if it is installed,
        the default is True
        Valid values: False,True
        [default: True] [currently: True]
    display.chop_threshold : float or None
        if set to a float value, all float values smaller than the given threshold
        will be displayed as exactly 0 by repr and friends.
        [default: None] [currently: None]
    display.colheader_justify : 'left'/'right'
        Controls the justification of column headers. used by DataFrameFormatter.
        [default: right] [currently: right]
    display.date_dayfirst : boolean
        When True, prints and parses dates with the day first, eg 20/01/2005
        [default: False] [currently: False]
    display.date_yearfirst : boolean
        When True, prints and parses dates with the year first, eg 2005/01/20
        [default: False] [currently: False]
    display.encoding : str/unicode
        Defaults to the detected encoding of the console.
        Specifies the encoding to be used for strings returned by to_string,
        these are generally strings meant to be displayed on the console.
        [default: utf-8] [currently: utf-8]
    display.expand_frame_repr : boolean
        Whether to print out the full DataFrame repr for wide DataFrames across
        multiple lines, `max_columns` is still respected, but the output will
        wrap-around across multiple "pages" if its width exceeds `display.width`.
        [default: True] [currently: True]
    display.float_format : callable
        The callable should accept a floating point number and return
        a string with the desired format of the number. This is used
        in some places like SeriesFormatter.
        See formats.format.EngFormatter for an example.
        [default: None] [currently: None]
    display.html.border : int
        A ``border=value`` attribute is inserted in the ``<table>`` tag
        for the DataFrame HTML repr.
        [default: 1] [currently: 1]
    display.html.table_schema : boolean
        Whether to publish a Table Schema representation for frontends
        that support it.
        (default: False)
        [default: False] [currently: False]
    display.html.use_mathjax : boolean
        When True, Jupyter notebook will process table contents using MathJax,
        rendering mathematical expressions enclosed by the dollar symbol.
        (default: True)
        [default: True] [currently: True]
    display.large_repr : 'truncate'/'info'
        For DataFrames exceeding max_rows/max_cols, the repr (and HTML repr) can
        show a truncated table, or switch to the view from
        df.info() (the behaviour in earlier versions of pandas).
        [default: truncate] [currently: truncate]
    display.max_categories : int
        This sets the maximum number of categories pandas should output when
        printing out a `Categorical` or a Series of dtype "category".
        [default: 8] [currently: 8]
    display.max_columns : int
        If max_cols is exceeded, switch to truncate view. Depending on
        `large_repr`, objects are either centrally truncated or printed as
        a summary view. 'None' value means unlimited.
    
        In case python/IPython is running in a terminal and `large_repr`
        equals 'truncate' this can be set to 0 or None and pandas will auto-detect
        the width of the terminal and print a truncated object which fits
        the screen width. The IPython notebook, IPython qtconsole, or IDLE
        do not run in a terminal and hence it is not possible to do
        correct auto-detection and defaults to 20.
        [default: 0] [currently: 0]
    display.max_colwidth : int or None
        The maximum width in characters of a column in the repr of
        a pandas data structure. When the column overflows, a "..."
        placeholder is embedded in the output. A 'None' value means unlimited.
        [default: 50] [currently: 50]
    display.max_dir_items : int
        The number of items that will be added to `dir(...)`. 'None' value means
        unlimited. Because dir is cached, changing this option will not immediately
        affect already existing dataframes until a column is deleted or added.
    
        This is for instance used to suggest columns from a dataframe to tab
        completion.
        [default: 100] [currently: 100]
    display.max_info_columns : int
        max_info_columns is used in DataFrame.info method to decide if
        per column information will be printed.
        [default: 100] [currently: 100]
    display.max_info_rows : int or None
        df.info() will usually show null-counts for each column.
        For large frames this can be quite slow. max_info_rows and max_info_cols
        limit this null check only to frames with smaller dimensions than
        specified.
        [default: 1690785] [currently: 1690785]
    display.max_rows : int
        If max_rows is exceeded, switch to truncate view. Depending on
        `large_repr`, objects are either centrally truncated or printed as
        a summary view. 'None' value means unlimited.
    
        In case python/IPython is running in a terminal and `large_repr`
        equals 'truncate' this can be set to 0 and pandas will auto-detect
        the height of the terminal and print a truncated object which fits
        the screen height. The IPython notebook, IPython qtconsole, or
        IDLE do not run in a terminal and hence it is not possible to do
        correct auto-detection.
        [default: 60] [currently: 60]
    display.max_seq_items : int or None
        When pretty-printing a long sequence, no more then `max_seq_items`
        will be printed. If items are omitted, they will be denoted by the
        addition of "..." to the resulting string.
    
        If set to None, the number of items to be printed is unlimited.
        [default: 100] [currently: 100]
    display.memory_usage : bool, string or None
        This specifies if the memory usage of a DataFrame should be displayed when
        df.info() is called. Valid values True,False,'deep'
        [default: True] [currently: True]
    display.min_rows : int
        The numbers of rows to show in a truncated view (when `max_rows` is
        exceeded). Ignored when `max_rows` is set to None or 0. When set to
        None, follows the value of `max_rows`.
        [default: 10] [currently: 10]
    display.multi_sparse : boolean
        "sparsify" MultiIndex display (don't display repeated
        elements in outer levels within groups)
        [default: True] [currently: True]
    display.notebook_repr_html : boolean
        When True, IPython notebook will use html representation for
        pandas objects (if it is available).
        [default: True] [currently: True]
    display.pprint_nest_depth : int
        Controls the number of nested levels to process when pretty-printing
        [default: 3] [currently: 3]
    display.precision : int
        Floating point output precision in terms of number of places after the
        decimal, for regular formatting as well as scientific notation. Similar
        to ``precision`` in :meth:`numpy.set_printoptions`.
        [default: 6] [currently: 6]
    display.show_dimensions : boolean or 'truncate'
        Whether to print out dimensions at the end of DataFrame repr.
        If 'truncate' is specified, only print out the dimensions if the
        frame is truncated (e.g. not display all rows and/or columns)
        [default: truncate] [currently: truncate]
    display.unicode.ambiguous_as_wide : boolean
        Whether to use the Unicode East Asian Width to calculate the display text
        width.
        Enabling this may affect to the performance (default: False)
        [default: False] [currently: False]
    display.unicode.east_asian_width : boolean
        Whether to use the Unicode East Asian Width to calculate the display text
        width.
        Enabling this may affect to the performance (default: False)
        [default: False] [currently: False]
    display.width : int
        Width of the display in characters. In case python/IPython is running in
        a terminal this can be set to None and pandas will correctly auto-detect
        the width.
        Note that the IPython notebook, IPython qtconsole, or IDLE do not run in a
        terminal and hence it is not possible to correctly detect the width.
        [default: 80] [currently: 80]
    future.infer_string Whether to infer sequence of str objects as pyarrow string dtype, which will be the default in pandas 3.0 (at which point this option will be deprecated).
        [default: False] [currently: False]
    io.excel.ods.reader : string
        The default Excel reader engine for 'ods' files. Available options:
        auto, odf.
        [default: auto] [currently: auto]
    io.excel.ods.writer : string
        The default Excel writer engine for 'ods' files. Available options:
        auto, odf.
        [default: auto] [currently: auto]
    io.excel.xls.reader : string
        The default Excel reader engine for 'xls' files. Available options:
        auto, xlrd.
        [default: auto] [currently: auto]
    io.excel.xlsb.reader : string
        The default Excel reader engine for 'xlsb' files. Available options:
        auto, pyxlsb.
        [default: auto] [currently: auto]
    io.excel.xlsm.reader : string
        The default Excel reader engine for 'xlsm' files. Available options:
        auto, xlrd, openpyxl.
        [default: auto] [currently: auto]
    io.excel.xlsm.writer : string
        The default Excel writer engine for 'xlsm' files. Available options:
        auto, openpyxl.
        [default: auto] [currently: auto]
    io.excel.xlsx.reader : string
        The default Excel reader engine for 'xlsx' files. Available options:
        auto, xlrd, openpyxl.
        [default: auto] [currently: auto]
    io.excel.xlsx.writer : string
        The default Excel writer engine for 'xlsx' files. Available options:
        auto, openpyxl, xlsxwriter.
        [default: auto] [currently: auto]
    io.hdf.default_format : format
        default format writing format, if None, then
        put will default to 'fixed' and append will default to 'table'
        [default: None] [currently: None]
    io.hdf.dropna_table : boolean
        drop ALL nan rows when appending to a table
        [default: False] [currently: False]
    io.parquet.engine : string
        The default parquet reader/writer engine. Available options:
        'auto', 'pyarrow', 'fastparquet', the default is 'auto'
        [default: auto] [currently: auto]
    io.sql.engine : string
        The default sql reader/writer engine. Available options:
        'auto', 'sqlalchemy', the default is 'auto'
        [default: auto] [currently: auto]
    mode.chained_assignment : string
        Raise an exception, warn, or no action if trying to use chained assignment,
        The default is warn
        [default: warn] [currently: warn]
    mode.copy_on_write : bool
        Use new copy-view behaviour using Copy-on-Write. Defaults to False,
        unless overridden by the 'PANDAS_COPY_ON_WRITE' environment variable
        (if set to "1" for True, needs to be set before pandas is imported).
        [default: False] [currently: False]
    mode.data_manager : string
        Internal data manager type; can be "block" or "array". Defaults to "block",
        unless overridden by the 'PANDAS_DATA_MANAGER' environment variable (needs
        to be set before pandas is imported).
        [default: block] [currently: block]
    mode.sim_interactive : boolean
        Whether to simulate interactive mode for purposes of testing
        [default: False] [currently: False]
    mode.string_storage : string
        The default storage for StringDtype. This option is ignored if
        ``future.infer_string`` is set to True.
        [default: python] [currently: python]
    mode.use_inf_as_na : boolean
        True means treat None, NaN, INF, -INF as NA (old way),
        False means None and NaN are null, but INF, -INF are not NA
        (new way).
    
        This option is deprecated in pandas 2.1.0 and will be removed in 3.0.
        [default: False] [currently: False]
        (Deprecated, use `` instead.)
    plotting.backend : str
        The plotting backend to use. The default value is "matplotlib", the
        backend provided with pandas. Other backends can be specified by
        providing the name of the module that implements the backend.
        [default: matplotlib] [currently: matplotlib]
    plotting.matplotlib.register_converters : bool or 'auto'.
        Whether to register converters with matplotlib's units registry for
        dates, times, datetimes, and Periods. Toggling to False will remove
        the converters, restoring any converters that pandas overwrote.
        [default: auto] [currently: auto]
    styler.format.decimal : str
        The character representation for the decimal separator for floats and complex.
        [default: .] [currently: .]
    styler.format.escape : str, optional
        Whether to escape certain characters according to the given context; html or latex.
        [default: None] [currently: None]
    styler.format.formatter : str, callable, dict, optional
        A formatter object to be used as default within ``Styler.format``.
        [default: None] [currently: None]
    styler.format.na_rep : str, optional
        The string representation for values identified as missing.
        [default: None] [currently: None]
    styler.format.precision : int
        The precision for floats and complex numbers.
        [default: 6] [currently: 6]
    styler.format.thousands : str, optional
        The character representation for thousands separator for floats, int and complex.
        [default: None] [currently: None]
    styler.html.mathjax : bool
        If False will render special CSS classes to table attributes that indicate Mathjax
        will not be used in Jupyter Notebook.
        [default: True] [currently: True]
    styler.latex.environment : str
        The environment to replace ``\begin{table}``. If "longtable" is used results
        in a specific longtable environment format.
        [default: None] [currently: None]
    styler.latex.hrules : bool
        Whether to add horizontal rules on top and bottom and below the headers.
        [default: False] [currently: False]
    styler.latex.multicol_align : {"r", "c", "l", "naive-l", "naive-r"}
        The specifier for horizontal alignment of sparsified LaTeX multicolumns. Pipe
        decorators can also be added to non-naive values to draw vertical
        rules, e.g. "\|r" will draw a rule on the left side of right aligned merged cells.
        [default: r] [currently: r]
    styler.latex.multirow_align : {"c", "t", "b"}
        The specifier for vertical alignment of sparsified LaTeX multirows.
        [default: c] [currently: c]
    styler.render.encoding : str
        The encoding used for output HTML and LaTeX files.
        [default: utf-8] [currently: utf-8]
    styler.render.max_columns : int, optional
        The maximum number of columns that will be rendered. May still be reduced to
        satisfy ``max_elements``, which takes precedence.
        [default: None] [currently: None]
    styler.render.max_elements : int
        The maximum number of data-cell (<td>) elements that will be rendered before
        trimming will occur over columns, rows or both if needed.
        [default: 262144] [currently: 262144]
    styler.render.max_rows : int, optional
        The maximum number of rows that will be rendered. May still be reduced to
        satisfy ``max_elements``, which takes precedence.
        [default: None] [currently: None]
    styler.render.repr : str
        Determine which output to use in Jupyter Notebook in {"html", "latex"}.
        [default: html] [currently: html]
    styler.sparse.columns : bool
        Whether to sparsify the display of hierarchical columns. Setting to False will
        display each explicit level element in a hierarchical key for each column.
        [default: True] [currently: True]
    styler.sparse.index : bool
        Whether to sparsify the display of a hierarchical index. Setting to False will
        display each explicit level element in a hierarchical key for each row.
        [default: True] [currently: True]
    
    Examples
    --------
    >>> pd.get_option('display.max_columns')  # doctest: +SKIP
    4
    """
    pass

def get_rule_month(D): # real signature unknown; restored from __doc__
    """
    Return starting month of given freq, default is December.
    
        Parameters
        ----------
        source : str
            Derived from `freq.rule_code` or `freq.freqstr`.
    
        Returns
        -------
        rule_month: str
    
        Examples
        --------
        >>> get_rule_month('D')
        'DEC'
    
        >>> get_rule_month('A-JAN')
        'JAN'
    """
    pass

def guess_datetime_format(*args, **kwargs): # real signature unknown
    """
    Guess the datetime format of a given datetime string.
    
        Parameters
        ----------
        dt_str : str
            Datetime string to guess the format of.
        dayfirst : bool, default False
            If True parses dates with the day first, eg 20/01/2005
            Warning: dayfirst=True is not strict, but will prefer to parse
            with day first (this is a known bug).
    
        Returns
        -------
        str or None : ret
            datetime format string (for `strftime` or `strptime`),
            or None if it can't be guessed.
    """
    pass

def parse_datetime_string_with_reso(*args, **kwargs): # real signature unknown
    """
    Try hard to parse datetime string, leveraging dateutil plus some extra
        goodies like quarter recognition.
    
        Parameters
        ----------
        date_string : str
        freq : str or None, default None
            Helps with interpreting time string if supplied
            Corresponds to `offset.rule_code`
        dayfirst : bool, default None
            If None uses default from print_config
        yearfirst : bool, default None
            If None uses default from print_config
    
        Returns
        -------
        datetime
        str
            Describing resolution of parsed string.
    
        Raises
        ------
        ValueError : preliminary check suggests string is not datetime
        DateParseError : error within dateutil
    """
    pass

def py_parse_datetime_string(*args, **kwargs): # real signature unknown
    pass

def quarter_to_myear(*args, **kwargs): # real signature unknown
    """
    A quarterly frequency defines a "year" which may not coincide with
        the calendar-year.  Find the calendar-year and calendar-month associated
        with the given year and quarter under the `freq`-derived calendar.
    
        Parameters
        ----------
        year : int
        quarter : int
        freq : str or None
    
        Returns
        -------
        year : int
        month : int
    
        See Also
        --------
        Period.qyear
    """
    pass

def try_parse_dates(*args, **kwargs): # real signature unknown
    pass

def try_parse_year_month_day(*args, **kwargs): # real signature unknown
    pass

def _DATEUTIL_LEXER_SPLIT(*args, **kwargs): # real signature unknown
    pass

def _does_string_look_like_datetime(*args, **kwargs): # real signature unknown
    """
    Checks whether given string is a datetime: it has to start with '0' or
        be greater than 1000.
    
        Parameters
        ----------
        py_string: str
    
        Returns
        -------
        bool
            Whether given string is potentially a datetime.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class DateParseError(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class InvalidOperation(__decimal.DecimalException):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


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


class tzoffset(__datetime.tzinfo):
    """
    A simple class for representing a fixed offset from UTC.
    
        :param name:
            The timezone name, to be returned when ``tzname()`` is called.
        :param offset:
            The time zone offset in seconds, or (since version 2.6.0, represented
            as a :py:class:`datetime.timedelta` object).
    """
    def dst(self, dt): # reliably restored by inspect
        # no doc
        pass

    def fromutc(self, dt): # reliably restored by inspect
        # no doc
        pass

    def is_ambiguous(self, dt): # reliably restored by inspect
        """
        Whether or not the "wall time" of a given datetime is ambiguous in this
                zone.
        
                :param dt:
                    A :py:class:`datetime.datetime`, naive or time zone aware.
                :return:
                    Returns ``True`` if ambiguous, ``False`` otherwise.
        
                .. versionadded:: 2.6.0
        """
        pass

    def tzname(self, dt): # reliably restored by inspect
        # no doc
        pass

    def utcoffset(self, dt): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, name, offset): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _cache_lock = None # (!) real value is '<unlocked _thread.lock object at 0x7fd301542740>'
    _TzOffsetFactory__instances = None # (!) real value is '<WeakValueDictionary at 0x7fd2ef350160>'
    _TzOffsetFactory__strong_cache = OrderedDict()
    _TzOffsetFactory__strong_cache_size = 8
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'dateutil.tz.tz', '__doc__': '\\n    A simple class for representing a fixed offset from UTC.\\n\\n    :param name:\\n        The timezone name, to be returned when ``tzname()`` is called.\\n    :param offset:\\n        The time zone offset in seconds, or (since version 2.6.0, represented\\n        as a :py:class:`datetime.timedelta` object).\\n    ', '__init__': <function tzoffset.__init__ at 0x7fd2ef31c8b0>, 'utcoffset': <function tzoffset.utcoffset at 0x7fd2ef31c940>, 'dst': <function tzoffset.dst at 0x7fd2ef31c9d0>, 'tzname': <function tzoffset.tzname at 0x7fd2ef31ca60>, 'fromutc': <function tzoffset.fromutc at 0x7fd2ef31cb80>, 'is_ambiguous': <function tzoffset.is_ambiguous at 0x7fd2ef31cc10>, '__eq__': <function tzoffset.__eq__ at 0x7fd2ef31cca0>, '__hash__': None, '__ne__': <function tzoffset.__ne__ at 0x7fd2ef31cd30>, '__repr__': <function tzoffset.__repr__ at 0x7fd2ef31cdc0>, '__reduce__': <method '__reduce__' of 'object' objects>, '__dict__': <attribute '__dict__' of 'tzoffset' objects>, '__weakref__': <attribute '__weakref__' of 'tzoffset' objects>, '_TzOffsetFactory__instances': <WeakValueDictionary at 0x7fd2ef350160>, '_TzOffsetFactory__strong_cache': OrderedDict(), '_TzOffsetFactory__strong_cache_size': 8, '_cache_lock': <unlocked _thread.lock object at 0x7fd301542740>})"
    __hash__ = None


class _dateutil_tzlocal(__dateutil_tz__common._tzinfo):
    """ A :class:`tzinfo` subclass built around the ``time`` timezone functions. """
    def dst(self, dt): # reliably restored by inspect
        # no doc
        pass

    def is_ambiguous(self, dt): # reliably restored by inspect
        """
        Whether or not the "wall time" of a given datetime is ambiguous in this
                zone.
        
                :param dt:
                    A :py:class:`datetime.datetime`, naive or time zone aware.
        
        
                :return:
                    Returns ``True`` if ambiguous, ``False`` otherwise.
        
                .. versionadded:: 2.6.0
        """
        pass

    def tzname(self, dt): # reliably restored by inspect
        # no doc
        pass

    def utcoffset(self, dt): # reliably restored by inspect
        # no doc
        pass

    def _isdst(self, dt, fold_naive=True): # reliably restored by inspect
        # no doc
        pass

    def _naive_is_dst(self, dt): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __hash__ = None


class _dateutil_tzutc(__datetime.tzinfo):
    """
    This is a tzinfo object that represents the UTC time zone.
    
        **Examples:**
    
        .. doctest::
    
            >>> from datetime import *
            >>> from dateutil.tz import *
    
            >>> datetime.now()
            datetime.datetime(2003, 9, 27, 9, 40, 1, 521290)
    
            >>> datetime.now(tzutc())
            datetime.datetime(2003, 9, 27, 12, 40, 12, 156379, tzinfo=tzutc())
    
            >>> datetime.now(tzutc()).tzname()
            'UTC'
    
        .. versionchanged:: 2.7.0
            ``tzutc()`` is now a singleton, so the result of ``tzutc()`` will
            always return the same object.
    
            .. doctest::
    
                >>> from dateutil.tz import tzutc, UTC
                >>> tzutc() is tzutc()
                True
                >>> tzutc() is UTC
                True
    """
    def dst(self, dt): # reliably restored by inspect
        # no doc
        pass

    def fromutc(self, dt): # reliably restored by inspect
        """
        Fast track version of fromutc() returns the original ``dt`` object for
                any valid :py:class:`datetime.datetime` object.
        """
        pass

    def is_ambiguous(self, dt): # reliably restored by inspect
        """
        Whether or not the "wall time" of a given datetime is ambiguous in this
                zone.
        
                :param dt:
                    A :py:class:`datetime.datetime`, naive or time zone aware.
        
        
                :return:
                    Returns ``True`` if ambiguous, ``False`` otherwise.
        
                .. versionadded:: 2.6.0
        """
        pass

    def tzname(self, dt): # reliably restored by inspect
        # no doc
        pass

    def utcoffset(self, dt): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _TzSingleton__instance = tzutc()
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'dateutil.tz.tz\', \'__doc__\': "\\n    This is a tzinfo object that represents the UTC time zone.\\n\\n    **Examples:**\\n\\n    .. doctest::\\n\\n        >>> from datetime import *\\n        >>> from dateutil.tz import *\\n\\n        >>> datetime.now()\\n        datetime.datetime(2003, 9, 27, 9, 40, 1, 521290)\\n\\n        >>> datetime.now(tzutc())\\n        datetime.datetime(2003, 9, 27, 12, 40, 12, 156379, tzinfo=tzutc())\\n\\n        >>> datetime.now(tzutc()).tzname()\\n        \'UTC\'\\n\\n    .. versionchanged:: 2.7.0\\n        ``tzutc()`` is now a singleton, so the result of ``tzutc()`` will\\n        always return the same object.\\n\\n        .. doctest::\\n\\n            >>> from dateutil.tz import tzutc, UTC\\n            >>> tzutc() is tzutc()\\n            True\\n            >>> tzutc() is UTC\\n            True\\n    ", \'utcoffset\': <function tzutc.utcoffset at 0x7fd2ef31c3a0>, \'dst\': <function tzutc.dst at 0x7fd2ef31c430>, \'tzname\': <function tzutc.tzname at 0x7fd2ef31c4c0>, \'is_ambiguous\': <function tzutc.is_ambiguous at 0x7fd2ef31c550>, \'fromutc\': <function tzutc.fromutc at 0x7fd2ef31c670>, \'__eq__\': <function tzutc.__eq__ at 0x7fd2ef31c700>, \'__hash__\': None, \'__ne__\': <function tzutc.__ne__ at 0x7fd2ef31c790>, \'__repr__\': <function tzutc.__repr__ at 0x7fd2ef31c820>, \'__reduce__\': <method \'__reduce__\' of \'object\' objects>, \'__dict__\': <attribute \'__dict__\' of \'tzutc\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'tzutc\' objects>, \'_TzSingleton__instance\': tzutc()})'
    __hash__ = None


class _timelex(object):
    # no doc
    def get_tokens(self, *args, **kwargs): # real signature unknown
        """
        This function breaks the time string into lexical units (tokens), which
                can be parsed by the parser. Lexical units are demarcated by changes in
                the character set, so any continuous string of letters is considered
                one unit, any continuous string of numbers is considered one unit.
                The main complication arises from the fact that dots ('.') can be used
                both as separators (e.g. "Sep.20.2009") or decimal points (e.g.
                "4:30:21.447"). As such, it is necessary to read the full context of
                any dot-separated strings before breaking it into tokens; as such, this
                function maintains a "token stack", for when the ambiguous context
                demands that multiple tokens be parsed at once.
        """
        pass

    @classmethod
    def split(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pandas._libs.tslibs.parsing', '__init__': <cyfunction _timelex.__init__ at 0x7fd2ef335be0>, 'get_tokens': <cyfunction _timelex.get_tokens at 0x7fd2ef335cb0>, 'split': <classmethod(<cyfunction _timelex.split at 0x7fd2ef335d80>)>, '__dict__': <attribute '__dict__' of '_timelex' objects>, '__weakref__': <attribute '__weakref__' of '_timelex' objects>, '__doc__': None})"


# variables with complex values

DEFAULTPARSER = None # (!) real value is '<dateutil.parser._parser.parser object at 0x7fd2ef2ed690>'

_DEFAULT_DATETIME = None # (!) real value is 'datetime.datetime(1, 1, 1, 0, 0)'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fd2ef307c40>'

__pyx_capi__ = {
    'get_rule_month': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x7fd2ef3072d0>'
    'parse_datetime_string': None, # (!) real value is '<capsule object "PyDateTime_DateTime *(PyObject *, int, int, NPY_DATETIMEUNIT *)" at 0x7fd2ef306a00>'
    'quarter_to_myear': None, # (!) real value is '<capsule object "PyObject *(int, int, PyObject *, int __pyx_skip_dispatch)" at 0x7fd2ef307360>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.parsing', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fd2ef307c40>, origin='/home/olenepal/.local/lib/python3.10/site-packages/pandas/_libs/tslibs/parsing.cpython-310-x86_64-linux-gnu.so')"

__test__ = {
    'concat_date_cols (line 1121)': "\n    Concatenates elements from numpy arrays in `date_cols` into strings.\n\n    Parameters\n    ----------\n    date_cols : tuple[ndarray]\n\n    Returns\n    -------\n    arr_of_rows : ndarray[object]\n\n    Examples\n    --------\n    >>> dates=np.array(['3/31/2019', '4/31/2019'], dtype=object)\n    >>> times=np.array(['11:20', '10:45'], dtype=object)\n    >>> result = concat_date_cols((dates, times))\n    >>> result\n    array(['3/31/2019 11:20', '4/31/2019 10:45'], dtype=object)\n    ",
    'get_rule_month (line 1193)': "\n    Return starting month of given freq, default is December.\n\n    Parameters\n    ----------\n    source : str\n        Derived from `freq.rule_code` or `freq.freqstr`.\n\n    Returns\n    -------\n    rule_month: str\n\n    Examples\n    --------\n    >>> get_rule_month('D')\n    'DEC'\n\n    >>> get_rule_month('A-JAN')\n    'JAN'\n    ",
}

