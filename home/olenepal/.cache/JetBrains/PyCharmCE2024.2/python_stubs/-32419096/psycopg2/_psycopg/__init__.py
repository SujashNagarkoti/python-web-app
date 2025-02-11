# encoding: utf-8
# module psycopg2._psycopg
# from /home/olenepal/.local/lib/python3.10/site-packages/psycopg2/_psycopg.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" psycopg2 PostgreSQL driver """

# imports
import psycopg2 as __psycopg2
import psycopg2.extensions as __psycopg2_extensions


# Variables with simple values

apilevel = '2.0'

paramstyle = 'pyformat'

REPLICATION_LOGICAL = 87654321
REPLICATION_PHYSICAL = 12345678

threadsafety = 2

__libpq_version__ = 160000

__version__ = '2.9.10 (dt dec pq3 ext lo64)'

# functions

def adapt(obj, protocol, alternate): # real signature unknown; restored from __doc__
    """ adapt(obj, protocol, alternate) -> object -- adapt obj to given protocol """
    return object()

def BINARY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def BINARYARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def BOOLEAN(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def BOOLEANARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def BYTES(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def BYTESARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def CIDRARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def Date(year, month, day): # real signature unknown; restored from __doc__
    """
    Date(year, month, day) -> new date
    
    Build an object holding a date value.
    """
    pass

def DATE(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def DATEARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def DateFromPy(datetime_date): # real signature unknown; restored from __doc__
    """ DateFromPy(datetime.date) -> new wrapper """
    pass

def DateFromTicks(ticks): # real signature unknown; restored from __doc__
    """
    DateFromTicks(ticks) -> new date
    
    Build an object holding a date value from the given ticks value.
    
    Ticks are the number of seconds since the epoch; see the documentation of the standard Python time module for details).
    """
    pass

def DATETIME(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def DATETIMEARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def DATETIMETZ(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def DATETIMETZARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def DECIMAL(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def DECIMALARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def encrypt_password(password, user, scope=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ encrypt_password(password, user, [scope], [algorithm]) -- Prepares the encrypted form of a PostgreSQL password. """
    pass

def FLOAT(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def FLOATARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def get_wait_callback(*args, **kwargs): # real signature unknown
    """
    Return the currently registered wait callback.
    
    Return `!None` if no callback is currently registered.
    """
    pass

def INETARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def INTEGER(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def INTEGERARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def INTERVAL(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def INTERVALARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def IntervalFromPy(datetime_timedelta): # real signature unknown; restored from __doc__
    """ IntervalFromPy(datetime.timedelta) -> new wrapper """
    pass

def libpq_version(*args, **kwargs): # real signature unknown
    """ Query actual libpq version loaded. """
    pass

def LONGINTEGER(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def LONGINTEGERARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def MACADDRARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def new_array_type(oids, name, baseobj): # real signature unknown; restored from __doc__
    """
    new_array_type(oids, name, baseobj) -> new type object
    
    Create a new binding object to parse an array.
    
    The object can be used with `register_type()`.
    
    :Parameters:
      * `oids`: Tuple of ``oid`` of the PostgreSQL types to convert.
      * `name`: Name for the new type
      * `baseobj`: Adapter to perform type conversion of a single array item.
    """
    pass

def new_type(oids, name, castobj): # real signature unknown; restored from __doc__
    """
    new_type(oids, name, castobj) -> new type object
    
    Create a new binding object. The object can be used with the
    `register_type()` function to bind PostgreSQL objects to python objects.
    
    :Parameters:
      * `oids`: Tuple of ``oid`` of the PostgreSQL types to convert.
      * `name`: Name for the new type
      * `adapter`: Callable to perform type conversion.
        It must have the signature ``fun(value, cur)`` where ``value`` is
        the string representation returned by PostgreSQL (`!None` if ``NULL``)
        and ``cur`` is the cursor from which data are read.
    """
    pass

def NUMBER(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def parse_dsn(dsn): # real signature unknown; restored from __doc__
    """ parse_dsn(dsn) -> dict -- parse a connection string into parameters """
    return {}

def PYDATE(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def PYDATEARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def PYDATETIME(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def PYDATETIMEARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def PYDATETIMETZ(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def PYDATETIMETZARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def PYINTERVAL(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def PYINTERVALARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def PYTIME(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def PYTIMEARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def quote_ident(p_str, conn_or_curs): # real signature unknown; restored from __doc__
    """
    quote_ident(str, conn_or_curs) -> str -- wrapper around PQescapeIdentifier
    
    :Parameters:
      * `str`: A bytes or unicode object
      * `conn_or_curs`: A connection or cursor, required
    """
    return ""

def register_type(obj, conn_or_curs): # real signature unknown; restored from __doc__
    """
    register_type(obj, conn_or_curs) -> None -- register obj with psycopg type system
    
    :Parameters:
      * `obj`: A type adapter created by `new_type()`
      * `conn_or_curs`: A connection, cursor or None
    """
    pass

def ROWID(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def ROWIDARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def set_wait_callback(None_): # real signature unknown; restored from __doc__
    """
    Register a callback function to block waiting for data.
    
    The callback should have signature :samp:`fun({conn})` and
    is called to wait for data available whenever a blocking function from the
    libpq is called.  Use `!set_wait_callback(None)` to revert to the
    original behaviour (i.e. using blocking libpq functions).
    
    The function is an hook to allow coroutine-based libraries (such as
    Eventlet_ or gevent_) to switch when Psycopg is blocked, allowing
    other coroutines to run concurrently.
    
    See `~psycopg2.extras.wait_select()` for an example of a wait callback
    implementation.
    
    .. _Eventlet: https://eventlet.net/
    .. _gevent: http://www.gevent.org/
    """
    pass

def STRING(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def STRINGARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def Time(hour, minutes, seconds, tzinfo=None): # real signature unknown; restored from __doc__
    """
    Time(hour, minutes, seconds, tzinfo=None) -> new time
    
    Build an object holding a time value.
    """
    pass

def TIME(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def TIMEARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def TimeFromPy(datetime_time): # real signature unknown; restored from __doc__
    """ TimeFromPy(datetime.time) -> new wrapper """
    pass

def TimeFromTicks(ticks): # real signature unknown; restored from __doc__
    """
    TimeFromTicks(ticks) -> new time
    
    Build an object holding a time value from the given ticks value.
    
    Ticks are the number of seconds since the epoch; see the documentation of the standard Python time module for details).
    """
    pass

def Timestamp(year, month, day, hour, minutes, seconds, tzinfo=None): # real signature unknown; restored from __doc__
    """
    Timestamp(year, month, day, hour, minutes, seconds, tzinfo=None) -> new timestamp
    
    Build an object holding a timestamp value.
    """
    pass

def TimestampFromPy(datetime_datetime): # real signature unknown; restored from __doc__
    """ TimestampFromPy(datetime.datetime) -> new wrapper """
    pass

def TimestampFromTicks(ticks): # real signature unknown; restored from __doc__
    """
    TimestampFromTicks(ticks) -> new timestamp
    
    Build an object holding a timestamp value from the given ticks value.
    
    Ticks are the number of seconds since the epoch; see the documentation of the standard Python time module for details).
    """
    pass

def UNICODE(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def UNICODEARRAY(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def UNKNOWN(*args, **kwargs): # real signature unknown
    """ psycopg type-casting object """
    pass

def _connect(dsn, connection_factory=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _connect(dsn, [connection_factory], [async]) -- New database connection. """
    pass

# classes

from .AsIs import AsIs
from .Binary import Binary
from .Boolean import Boolean
from .Column import Column
from .connection import connection
from .ConnectionInfo import ConnectionInfo
from .cursor import cursor
from .Error import Error
from .DatabaseError import DatabaseError
from .DataError import DataError
from .Decimal import Decimal
from .Diagnostics import Diagnostics
from .Float import Float
from .Int import Int
from .IntegrityError import IntegrityError
from .InterfaceError import InterfaceError
from .InternalError import InternalError
from .ISQLQuote import ISQLQuote
from .List import List
from .lobject import lobject
from .Notify import Notify
from .NotSupportedError import NotSupportedError
from .OperationalError import OperationalError
from .ProgrammingError import ProgrammingError
from .QueryCanceledError import QueryCanceledError
from .QuotedString import QuotedString
from .ReplicationConnection import ReplicationConnection
from .ReplicationCursor import ReplicationCursor
from .ReplicationMessage import ReplicationMessage
from .TransactionRollbackError import TransactionRollbackError
from .Warning import Warning
from .Xid import Xid
# variables with complex values

adapters = {
    (
        float,
        ISQLQuote,
    ): 
        Float
    ,
    (
        int,
        '<value is a self-reference, replaced by this string>',
    ): 
        Int
    ,
    (
        bool,
        '<value is a self-reference, replaced by this string>',
    ): 
        Boolean
    ,
    (
        str,
        '<value is a self-reference, replaced by this string>',
    ): 
        QuotedString
    ,
    (
        bytes,
        '<value is a self-reference, replaced by this string>',
    ): 
        Binary
    ,
    (
        bytearray,
        '<value is a self-reference, replaced by this string>',
    ): 
        '<value is a self-reference, replaced by this string>'
    ,
    (
        memoryview,
        '<value is a self-reference, replaced by this string>',
    ): 
        '<value is a self-reference, replaced by this string>'
    ,
    (
        list,
        '<value is a self-reference, replaced by this string>',
    ): 
        List
    ,
    (
        None, # (!) real value is "<class 'datetime.date'>"
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) forward: DateFromPy, real value is '<built-in function DateFromPy>'
    ,
    (
        None, # (!) real value is "<class 'datetime.time'>"
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) forward: TimeFromPy, real value is '<built-in function TimeFromPy>'
    ,
    (
        None, # (!) real value is "<class 'datetime.datetime'>"
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) forward: TimestampFromPy, real value is '<built-in function TimestampFromPy>'
    ,
    (
        None, # (!) real value is "<class 'datetime.timedelta'>"
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) forward: IntervalFromPy, real value is '<built-in function IntervalFromPy>'
    ,
    (
        None, # (!) real value is "<class 'psycopg2._range.NumericRange'>"
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) real value is "<class 'psycopg2._range.NumberRangeAdapter'>"
    ,
    (
        None, # (!) real value is "<class 'psycopg2._range.DateRange'>"
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) real value is "<class 'psycopg2._range.daterange'>"
    ,
    (
        None, # (!) real value is "<class 'psycopg2._range.DateTimeRange'>"
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) real value is "<class 'psycopg2._range.tsrange'>"
    ,
    (
        None, # (!) real value is "<class 'psycopg2._range.DateTimeTZRange'>"
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) real value is "<class 'psycopg2._range.tstzrange'>"
    ,
    (
        tuple,
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) real value is "<class 'psycopg2.extensions.SQL_IN'>"
    ,
    (
        None, # (!) real value is "<class 'NoneType'>"
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) real value is "<class 'psycopg2.extensions.NoneAdapter'>"
    ,
    (
        None, # (!) real value is "<class 'decimal.Decimal'>"
        '<value is a self-reference, replaced by this string>',
    ): 
        Decimal
    ,
}

binary_types = {}

encodings = {
    'ABC': 'cp1258',
    'ALT': 'cp866',
    'BIG5': 'big5',
    'EUCCN': 'euccn',
    'EUCJIS2004': 'euc_jis_2004',
    'EUCJP': 'euc_jp',
    'EUCKR': 'euc_kr',
    'EUC_CN': 'euccn',
    'EUC_JIS_2004': 'euc_jis_2004',
    'EUC_JP': 'euc_jp',
    'EUC_KR': 'euc_kr',
    'GB18030': 'gb18030',
    'GBK': 'gbk',
    'ISO88591': 'iso8859_1',
    'ISO885910': 'iso8859_10',
    'ISO885913': 'iso8859_13',
    'ISO885914': 'iso8859_14',
    'ISO885915': 'iso8859_15',
    'ISO885916': 'iso8859_16',
    'ISO88592': 'iso8859_2',
    'ISO88593': 'iso8859_3',
    'ISO88595': 'iso8859_5',
    'ISO88596': 'iso8859_6',
    'ISO88597': 'iso8859_7',
    'ISO88598': 'iso8859_8',
    'ISO88599': 'iso8859_9',
    'ISO_8859_1': 'iso8859_1',
    'ISO_8859_10': 'iso8859_10',
    'ISO_8859_13': 'iso8859_13',
    'ISO_8859_14': 'iso8859_14',
    'ISO_8859_15': 'iso8859_15',
    'ISO_8859_16': 'iso8859_16',
    'ISO_8859_2': 'iso8859_2',
    'ISO_8859_3': 'iso8859_3',
    'ISO_8859_5': 'iso8859_5',
    'ISO_8859_6': 'iso8859_6',
    'ISO_8859_7': 'iso8859_7',
    'ISO_8859_8': 'iso8859_8',
    'ISO_8859_9': 'iso8859_9',
    'JOHAB': 'johab',
    'KOI8': 'koi8_r',
    'KOI8R': 'koi8_r',
    'KOI8U': 'koi8_u',
    'LATIN1': 'iso8859_1',
    'LATIN10': 'iso8859_16',
    'LATIN2': 'iso8859_2',
    'LATIN3': 'iso8859_3',
    'LATIN4': 'iso8859_4',
    'LATIN5': 'iso8859_9',
    'LATIN6': 'iso8859_10',
    'LATIN7': 'iso8859_13',
    'LATIN8': 'iso8859_14',
    'LATIN9': 'iso8859_15',
    'MSKANJI': 'cp932',
    'Mskanji': 'cp932',
    'SHIFTJIS': 'cp932',
    'SHIFTJIS2004': 'shift_jis_2004',
    'SHIFT_JIS_2004': 'shift_jis_2004',
    'SJIS': 'cp932',
    'SQLASCII': 'ascii',
    'SQL_ASCII': 'ascii',
    'ShiftJIS': 'cp932',
    'TCVN': 'cp1258',
    'TCVN5712': 'cp1258',
    'UHC': 'cp949',
    'UNICODE': 'utf_8',
    'UTF8': 'utf_8',
    'VSCII': 'cp1258',
    'WIN': 'cp1251',
    'WIN1250': 'cp1250',
    'WIN1251': 'cp1251',
    'WIN1252': 'cp1252',
    'WIN1253': 'cp1253',
    'WIN1254': 'cp1254',
    'WIN1255': 'cp1255',
    'WIN1256': 'cp1256',
    'WIN1257': 'cp1257',
    'WIN1258': 'cp1258',
    'WIN866': 'cp866',
    'WIN874': 'cp874',
    'WIN932': 'cp932',
    'WIN936': 'gbk',
    'WIN949': 'cp949',
    'WIN950': 'cp950',
    'WINDOWS932': 'cp932',
    'WINDOWS936': 'gbk',
    'WINDOWS949': 'cp949',
    'WINDOWS950': 'cp950',
    'Windows932': 'cp932',
    'Windows936': 'gbk',
    'Windows949': 'cp949',
    'Windows950': 'cp950',
}

sqlstate_errors = {
    '02000': None, # (!) real value is "<class 'psycopg2.errors.NoData'>"
    '02001': None, # (!) real value is "<class 'psycopg2.errors.NoAdditionalDynamicResultSetsReturned'>"
    '03000': None, # (!) real value is "<class 'psycopg2.errors.SqlStatementNotYetComplete'>"
    '08000': None, # (!) real value is "<class 'psycopg2.errors.ConnectionException'>"
    '08001': None, # (!) real value is "<class 'psycopg2.errors.SqlclientUnableToEstablishSqlconnection'>"
    '08003': None, # (!) real value is "<class 'psycopg2.errors.ConnectionDoesNotExist'>"
    '08004': None, # (!) real value is "<class 'psycopg2.errors.SqlserverRejectedEstablishmentOfSqlconnection'>"
    '08006': None, # (!) real value is "<class 'psycopg2.errors.ConnectionFailure'>"
    '08007': None, # (!) real value is "<class 'psycopg2.errors.TransactionResolutionUnknown'>"
    '08P01': None, # (!) real value is "<class 'psycopg2.errors.ProtocolViolation'>"
    '09000': None, # (!) real value is "<class 'psycopg2.errors.TriggeredActionException'>"
    '0A000': None, # (!) real value is "<class 'psycopg2.errors.FeatureNotSupported'>"
    '0B000': None, # (!) real value is "<class 'psycopg2.errors.InvalidTransactionInitiation'>"
    '0F000': None, # (!) real value is "<class 'psycopg2.errors.LocatorException'>"
    '0F001': None, # (!) real value is "<class 'psycopg2.errors.InvalidLocatorSpecification'>"
    '0L000': None, # (!) real value is "<class 'psycopg2.errors.InvalidGrantor'>"
    '0LP01': None, # (!) real value is "<class 'psycopg2.errors.InvalidGrantOperation'>"
    '0P000': None, # (!) real value is "<class 'psycopg2.errors.InvalidRoleSpecification'>"
    '0Z000': None, # (!) real value is "<class 'psycopg2.errors.DiagnosticsException'>"
    '0Z002': None, # (!) real value is "<class 'psycopg2.errors.StackedDiagnosticsAccessedWithoutActiveHandler'>"
    '20000': None, # (!) real value is "<class 'psycopg2.errors.CaseNotFound'>"
    '21000': None, # (!) real value is "<class 'psycopg2.errors.CardinalityViolation'>"
    '22000': None, # (!) real value is "<class 'psycopg2.errors.DataException'>"
    '22001': None, # (!) real value is "<class 'psycopg2.errors.StringDataRightTruncation'>"
    '22002': None, # (!) real value is "<class 'psycopg2.errors.NullValueNoIndicatorParameter'>"
    '22003': None, # (!) real value is "<class 'psycopg2.errors.NumericValueOutOfRange'>"
    '22004': None, # (!) real value is "<class 'psycopg2.errors.NullValueNotAllowed'>"
    '22005': None, # (!) real value is "<class 'psycopg2.errors.ErrorInAssignment'>"
    '22007': None, # (!) real value is "<class 'psycopg2.errors.InvalidDatetimeFormat'>"
    '22008': None, # (!) real value is "<class 'psycopg2.errors.DatetimeFieldOverflow'>"
    '22009': None, # (!) real value is "<class 'psycopg2.errors.InvalidTimeZoneDisplacementValue'>"
    '2200B': None, # (!) real value is "<class 'psycopg2.errors.EscapeCharacterConflict'>"
    '2200C': None, # (!) real value is "<class 'psycopg2.errors.InvalidUseOfEscapeCharacter'>"
    '2200D': None, # (!) real value is "<class 'psycopg2.errors.InvalidEscapeOctet'>"
    '2200F': None, # (!) real value is "<class 'psycopg2.errors.ZeroLengthCharacterString'>"
    '2200G': None, # (!) real value is "<class 'psycopg2.errors.MostSpecificTypeMismatch'>"
    '2200H': None, # (!) real value is "<class 'psycopg2.errors.SequenceGeneratorLimitExceeded'>"
    '2200L': None, # (!) real value is "<class 'psycopg2.errors.NotAnXmlDocument'>"
    '2200M': None, # (!) real value is "<class 'psycopg2.errors.InvalidXmlDocument'>"
    '2200N': None, # (!) real value is "<class 'psycopg2.errors.InvalidXmlContent'>"
    '2200S': None, # (!) real value is "<class 'psycopg2.errors.InvalidXmlComment'>"
    '2200T': None, # (!) real value is "<class 'psycopg2.errors.InvalidXmlProcessingInstruction'>"
    '22010': None, # (!) real value is "<class 'psycopg2.errors.InvalidIndicatorParameterValue'>"
    '22011': None, # (!) real value is "<class 'psycopg2.errors.SubstringError'>"
    '22012': None, # (!) real value is "<class 'psycopg2.errors.DivisionByZero'>"
    '22013': None, # (!) real value is "<class 'psycopg2.errors.InvalidPrecedingOrFollowingSize'>"
    '22014': None, # (!) real value is "<class 'psycopg2.errors.InvalidArgumentForNtileFunction'>"
    '22015': None, # (!) real value is "<class 'psycopg2.errors.IntervalFieldOverflow'>"
    '22016': None, # (!) real value is "<class 'psycopg2.errors.InvalidArgumentForNthValueFunction'>"
    '22018': None, # (!) real value is "<class 'psycopg2.errors.InvalidCharacterValueForCast'>"
    '22019': None, # (!) real value is "<class 'psycopg2.errors.InvalidEscapeCharacter'>"
    '2201B': None, # (!) real value is "<class 'psycopg2.errors.InvalidRegularExpression'>"
    '2201E': None, # (!) real value is "<class 'psycopg2.errors.InvalidArgumentForLogarithm'>"
    '2201F': None, # (!) real value is "<class 'psycopg2.errors.InvalidArgumentForPowerFunction'>"
    '2201G': None, # (!) real value is "<class 'psycopg2.errors.InvalidArgumentForWidthBucketFunction'>"
    '2201W': None, # (!) real value is "<class 'psycopg2.errors.InvalidRowCountInLimitClause'>"
    '2201X': None, # (!) real value is "<class 'psycopg2.errors.InvalidRowCountInResultOffsetClause'>"
    '22021': None, # (!) real value is "<class 'psycopg2.errors.CharacterNotInRepertoire'>"
    '22022': None, # (!) real value is "<class 'psycopg2.errors.IndicatorOverflow'>"
    '22023': None, # (!) real value is "<class 'psycopg2.errors.InvalidParameterValue'>"
    '22024': None, # (!) real value is "<class 'psycopg2.errors.UnterminatedCString'>"
    '22025': None, # (!) real value is "<class 'psycopg2.errors.InvalidEscapeSequence'>"
    '22026': None, # (!) real value is "<class 'psycopg2.errors.StringDataLengthMismatch'>"
    '22027': None, # (!) real value is "<class 'psycopg2.errors.TrimError'>"
    '2202E': None, # (!) real value is "<class 'psycopg2.errors.ArraySubscriptError'>"
    '2202G': None, # (!) real value is "<class 'psycopg2.errors.InvalidTablesampleRepeat'>"
    '2202H': None, # (!) real value is "<class 'psycopg2.errors.InvalidTablesampleArgument'>"
    '22030': None, # (!) real value is "<class 'psycopg2.errors.DuplicateJsonObjectKeyValue'>"
    '22031': None, # (!) real value is "<class 'psycopg2.errors.InvalidArgumentForSqlJsonDatetimeFunction'>"
    '22032': None, # (!) real value is "<class 'psycopg2.errors.InvalidJsonText'>"
    '22033': None, # (!) real value is "<class 'psycopg2.errors.InvalidSqlJsonSubscript'>"
    '22034': None, # (!) real value is "<class 'psycopg2.errors.MoreThanOneSqlJsonItem'>"
    '22035': None, # (!) real value is "<class 'psycopg2.errors.NoSqlJsonItem'>"
    '22036': None, # (!) real value is "<class 'psycopg2.errors.NonNumericSqlJsonItem'>"
    '22037': None, # (!) real value is "<class 'psycopg2.errors.NonUniqueKeysInAJsonObject'>"
    '22038': None, # (!) real value is "<class 'psycopg2.errors.SingletonSqlJsonItemRequired'>"
    '22039': None, # (!) real value is "<class 'psycopg2.errors.SqlJsonArrayNotFound'>"
    '2203A': None, # (!) real value is "<class 'psycopg2.errors.SqlJsonMemberNotFound'>"
    '2203B': None, # (!) real value is "<class 'psycopg2.errors.SqlJsonNumberNotFound'>"
    '2203C': None, # (!) real value is "<class 'psycopg2.errors.SqlJsonObjectNotFound'>"
    '2203D': None, # (!) real value is "<class 'psycopg2.errors.TooManyJsonArrayElements'>"
    '2203E': None, # (!) real value is "<class 'psycopg2.errors.TooManyJsonObjectMembers'>"
    '2203F': None, # (!) real value is "<class 'psycopg2.errors.SqlJsonScalarRequired'>"
    '2203G': None, # (!) real value is "<class 'psycopg2.errors.SqlJsonItemCannotBeCastToTargetType'>"
    '22P01': None, # (!) real value is "<class 'psycopg2.errors.FloatingPointException'>"
    '22P02': None, # (!) real value is "<class 'psycopg2.errors.InvalidTextRepresentation'>"
    '22P03': None, # (!) real value is "<class 'psycopg2.errors.InvalidBinaryRepresentation'>"
    '22P04': None, # (!) real value is "<class 'psycopg2.errors.BadCopyFileFormat'>"
    '22P05': None, # (!) real value is "<class 'psycopg2.errors.UntranslatableCharacter'>"
    '22P06': None, # (!) real value is "<class 'psycopg2.errors.NonstandardUseOfEscapeCharacter'>"
    '23000': None, # (!) real value is "<class 'psycopg2.errors.IntegrityConstraintViolation'>"
    '23001': None, # (!) real value is "<class 'psycopg2.errors.RestrictViolation'>"
    '23502': None, # (!) real value is "<class 'psycopg2.errors.NotNullViolation'>"
    '23503': None, # (!) real value is "<class 'psycopg2.errors.ForeignKeyViolation'>"
    '23505': None, # (!) real value is "<class 'psycopg2.errors.UniqueViolation'>"
    '23514': None, # (!) real value is "<class 'psycopg2.errors.CheckViolation'>"
    '23P01': None, # (!) real value is "<class 'psycopg2.errors.ExclusionViolation'>"
    '24000': None, # (!) real value is "<class 'psycopg2.errors.InvalidCursorState'>"
    '25000': None, # (!) real value is "<class 'psycopg2.errors.InvalidTransactionState'>"
    '25001': None, # (!) real value is "<class 'psycopg2.errors.ActiveSqlTransaction'>"
    '25002': None, # (!) real value is "<class 'psycopg2.errors.BranchTransactionAlreadyActive'>"
    '25003': None, # (!) real value is "<class 'psycopg2.errors.InappropriateAccessModeForBranchTransaction'>"
    '25004': None, # (!) real value is "<class 'psycopg2.errors.InappropriateIsolationLevelForBranchTransaction'>"
    '25005': None, # (!) real value is "<class 'psycopg2.errors.NoActiveSqlTransactionForBranchTransaction'>"
    '25006': None, # (!) real value is "<class 'psycopg2.errors.ReadOnlySqlTransaction'>"
    '25007': None, # (!) real value is "<class 'psycopg2.errors.SchemaAndDataStatementMixingNotSupported'>"
    '25008': None, # (!) real value is "<class 'psycopg2.errors.HeldCursorRequiresSameIsolationLevel'>"
    '25P01': None, # (!) real value is "<class 'psycopg2.errors.NoActiveSqlTransaction'>"
    '25P02': None, # (!) real value is "<class 'psycopg2.errors.InFailedSqlTransaction'>"
    '25P03': None, # (!) real value is "<class 'psycopg2.errors.IdleInTransactionSessionTimeout'>"
    '25P04': None, # (!) real value is "<class 'psycopg2.errors.TransactionTimeout'>"
    '26000': None, # (!) real value is "<class 'psycopg2.errors.InvalidSqlStatementName'>"
    '27000': None, # (!) real value is "<class 'psycopg2.errors.TriggeredDataChangeViolation'>"
    '28000': None, # (!) real value is "<class 'psycopg2.errors.InvalidAuthorizationSpecification'>"
    '28P01': None, # (!) real value is "<class 'psycopg2.errors.InvalidPassword'>"
    '2B000': None, # (!) real value is "<class 'psycopg2.errors.DependentPrivilegeDescriptorsStillExist'>"
    '2BP01': None, # (!) real value is "<class 'psycopg2.errors.DependentObjectsStillExist'>"
    '2D000': None, # (!) real value is "<class 'psycopg2.errors.InvalidTransactionTermination'>"
    '2F000': None, # (!) real value is "<class 'psycopg2.errors.SqlRoutineException'>"
    '2F002': None, # (!) real value is "<class 'psycopg2.errors.ModifyingSqlDataNotPermitted'>"
    '2F003': None, # (!) real value is "<class 'psycopg2.errors.ProhibitedSqlStatementAttempted'>"
    '2F004': None, # (!) real value is "<class 'psycopg2.errors.ReadingSqlDataNotPermitted'>"
    '2F005': None, # (!) real value is "<class 'psycopg2.errors.FunctionExecutedNoReturnStatement'>"
    '34000': None, # (!) real value is "<class 'psycopg2.errors.InvalidCursorName'>"
    '38000': None, # (!) real value is "<class 'psycopg2.errors.ExternalRoutineException'>"
    '38001': None, # (!) real value is "<class 'psycopg2.errors.ContainingSqlNotPermitted'>"
    '38002': None, # (!) real value is "<class 'psycopg2.errors.ModifyingSqlDataNotPermittedExt'>"
    '38003': None, # (!) real value is "<class 'psycopg2.errors.ProhibitedSqlStatementAttemptedExt'>"
    '38004': None, # (!) real value is "<class 'psycopg2.errors.ReadingSqlDataNotPermittedExt'>"
    '39000': None, # (!) real value is "<class 'psycopg2.errors.ExternalRoutineInvocationException'>"
    '39001': None, # (!) real value is "<class 'psycopg2.errors.InvalidSqlstateReturned'>"
    '39004': None, # (!) real value is "<class 'psycopg2.errors.NullValueNotAllowedExt'>"
    '39P01': None, # (!) real value is "<class 'psycopg2.errors.TriggerProtocolViolated'>"
    '39P02': None, # (!) real value is "<class 'psycopg2.errors.SrfProtocolViolated'>"
    '39P03': None, # (!) real value is "<class 'psycopg2.errors.EventTriggerProtocolViolated'>"
    '3B000': None, # (!) real value is "<class 'psycopg2.errors.SavepointException'>"
    '3B001': None, # (!) real value is "<class 'psycopg2.errors.InvalidSavepointSpecification'>"
    '3D000': None, # (!) real value is "<class 'psycopg2.errors.InvalidCatalogName'>"
    '3F000': None, # (!) real value is "<class 'psycopg2.errors.InvalidSchemaName'>"
    '40000': None, # (!) real value is "<class 'psycopg2.errors.TransactionRollback'>"
    '40001': None, # (!) real value is "<class 'psycopg2.errors.SerializationFailure'>"
    '40002': None, # (!) real value is "<class 'psycopg2.errors.TransactionIntegrityConstraintViolation'>"
    '40003': None, # (!) real value is "<class 'psycopg2.errors.StatementCompletionUnknown'>"
    '40P01': None, # (!) real value is "<class 'psycopg2.errors.DeadlockDetected'>"
    '42000': None, # (!) real value is "<class 'psycopg2.errors.SyntaxErrorOrAccessRuleViolation'>"
    '42501': None, # (!) real value is "<class 'psycopg2.errors.InsufficientPrivilege'>"
    '42601': None, # (!) real value is "<class 'psycopg2.errors.SyntaxError'>"
    '42602': None, # (!) real value is "<class 'psycopg2.errors.InvalidName'>"
    '42611': None, # (!) real value is "<class 'psycopg2.errors.InvalidColumnDefinition'>"
    '42622': None, # (!) real value is "<class 'psycopg2.errors.NameTooLong'>"
    '42701': None, # (!) real value is "<class 'psycopg2.errors.DuplicateColumn'>"
    '42702': None, # (!) real value is "<class 'psycopg2.errors.AmbiguousColumn'>"
    '42703': None, # (!) real value is "<class 'psycopg2.errors.UndefinedColumn'>"
    '42704': None, # (!) real value is "<class 'psycopg2.errors.UndefinedObject'>"
    '42710': None, # (!) real value is "<class 'psycopg2.errors.DuplicateObject'>"
    '42712': None, # (!) real value is "<class 'psycopg2.errors.DuplicateAlias'>"
    '42723': None, # (!) real value is "<class 'psycopg2.errors.DuplicateFunction'>"
    '42725': None, # (!) real value is "<class 'psycopg2.errors.AmbiguousFunction'>"
    '42803': None, # (!) real value is "<class 'psycopg2.errors.GroupingError'>"
    '42804': None, # (!) real value is "<class 'psycopg2.errors.DatatypeMismatch'>"
    '42809': None, # (!) real value is "<class 'psycopg2.errors.WrongObjectType'>"
    '42830': None, # (!) real value is "<class 'psycopg2.errors.InvalidForeignKey'>"
    '42846': None, # (!) real value is "<class 'psycopg2.errors.CannotCoerce'>"
    '42883': None, # (!) real value is "<class 'psycopg2.errors.UndefinedFunction'>"
    '428C9': None, # (!) real value is "<class 'psycopg2.errors.GeneratedAlways'>"
    '42939': None, # (!) real value is "<class 'psycopg2.errors.ReservedName'>"
    '42P01': None, # (!) real value is "<class 'psycopg2.errors.UndefinedTable'>"
    '42P02': None, # (!) real value is "<class 'psycopg2.errors.UndefinedParameter'>"
    '42P03': None, # (!) real value is "<class 'psycopg2.errors.DuplicateCursor'>"
    '42P04': None, # (!) real value is "<class 'psycopg2.errors.DuplicateDatabase'>"
    '42P05': None, # (!) real value is "<class 'psycopg2.errors.DuplicatePreparedStatement'>"
    '42P06': None, # (!) real value is "<class 'psycopg2.errors.DuplicateSchema'>"
    '42P07': None, # (!) real value is "<class 'psycopg2.errors.DuplicateTable'>"
    '42P08': None, # (!) real value is "<class 'psycopg2.errors.AmbiguousParameter'>"
    '42P09': None, # (!) real value is "<class 'psycopg2.errors.AmbiguousAlias'>"
    '42P10': None, # (!) real value is "<class 'psycopg2.errors.InvalidColumnReference'>"
    '42P11': None, # (!) real value is "<class 'psycopg2.errors.InvalidCursorDefinition'>"
    '42P12': None, # (!) real value is "<class 'psycopg2.errors.InvalidDatabaseDefinition'>"
    '42P13': None, # (!) real value is "<class 'psycopg2.errors.InvalidFunctionDefinition'>"
    '42P14': None, # (!) real value is "<class 'psycopg2.errors.InvalidPreparedStatementDefinition'>"
    '42P15': None, # (!) real value is "<class 'psycopg2.errors.InvalidSchemaDefinition'>"
    '42P16': None, # (!) real value is "<class 'psycopg2.errors.InvalidTableDefinition'>"
    '42P17': None, # (!) real value is "<class 'psycopg2.errors.InvalidObjectDefinition'>"
    '42P18': None, # (!) real value is "<class 'psycopg2.errors.IndeterminateDatatype'>"
    '42P19': None, # (!) real value is "<class 'psycopg2.errors.InvalidRecursion'>"
    '42P20': None, # (!) real value is "<class 'psycopg2.errors.WindowingError'>"
    '42P21': None, # (!) real value is "<class 'psycopg2.errors.CollationMismatch'>"
    '42P22': None, # (!) real value is "<class 'psycopg2.errors.IndeterminateCollation'>"
    '44000': None, # (!) real value is "<class 'psycopg2.errors.WithCheckOptionViolation'>"
    '53000': None, # (!) real value is "<class 'psycopg2.errors.InsufficientResources'>"
    '53100': None, # (!) real value is "<class 'psycopg2.errors.DiskFull'>"
    '53200': None, # (!) real value is "<class 'psycopg2.errors.OutOfMemory'>"
    '53300': None, # (!) real value is "<class 'psycopg2.errors.TooManyConnections'>"
    '53400': None, # (!) real value is "<class 'psycopg2.errors.ConfigurationLimitExceeded'>"
    '54000': None, # (!) real value is "<class 'psycopg2.errors.ProgramLimitExceeded'>"
    '54001': None, # (!) real value is "<class 'psycopg2.errors.StatementTooComplex'>"
    '54011': None, # (!) real value is "<class 'psycopg2.errors.TooManyColumns'>"
    '54023': None, # (!) real value is "<class 'psycopg2.errors.TooManyArguments'>"
    '55000': None, # (!) real value is "<class 'psycopg2.errors.ObjectNotInPrerequisiteState'>"
    '55006': None, # (!) real value is "<class 'psycopg2.errors.ObjectInUse'>"
    '55P02': None, # (!) real value is "<class 'psycopg2.errors.CantChangeRuntimeParam'>"
    '55P03': None, # (!) real value is "<class 'psycopg2.errors.LockNotAvailable'>"
    '55P04': None, # (!) real value is "<class 'psycopg2.errors.UnsafeNewEnumValueUsage'>"
    '57000': None, # (!) real value is "<class 'psycopg2.errors.OperatorIntervention'>"
    '57014': None, # (!) real value is "<class 'psycopg2.errors.QueryCanceled'>"
    '57P01': None, # (!) real value is "<class 'psycopg2.errors.AdminShutdown'>"
    '57P02': None, # (!) real value is "<class 'psycopg2.errors.CrashShutdown'>"
    '57P03': None, # (!) real value is "<class 'psycopg2.errors.CannotConnectNow'>"
    '57P04': None, # (!) real value is "<class 'psycopg2.errors.DatabaseDropped'>"
    '57P05': None, # (!) real value is "<class 'psycopg2.errors.IdleSessionTimeout'>"
    '58000': None, # (!) real value is "<class 'psycopg2.errors.SystemError'>"
    '58030': None, # (!) real value is "<class 'psycopg2.errors.IoError'>"
    '58P01': None, # (!) real value is "<class 'psycopg2.errors.UndefinedFile'>"
    '58P02': None, # (!) real value is "<class 'psycopg2.errors.DuplicateFile'>"
    '72000': None, # (!) real value is "<class 'psycopg2.errors.SnapshotTooOld'>"
    'F0000': None, # (!) real value is "<class 'psycopg2.errors.ConfigFileError'>"
    'F0001': None, # (!) real value is "<class 'psycopg2.errors.LockFileExists'>"
    'HV000': None, # (!) real value is "<class 'psycopg2.errors.FdwError'>"
    'HV001': None, # (!) real value is "<class 'psycopg2.errors.FdwOutOfMemory'>"
    'HV002': None, # (!) real value is "<class 'psycopg2.errors.FdwDynamicParameterValueNeeded'>"
    'HV004': None, # (!) real value is "<class 'psycopg2.errors.FdwInvalidDataType'>"
    'HV005': None, # (!) real value is "<class 'psycopg2.errors.FdwColumnNameNotFound'>"
    'HV006': None, # (!) real value is "<class 'psycopg2.errors.FdwInvalidDataTypeDescriptors'>"
    'HV007': None, # (!) real value is "<class 'psycopg2.errors.FdwInvalidColumnName'>"
    'HV008': None, # (!) real value is "<class 'psycopg2.errors.FdwInvalidColumnNumber'>"
    'HV009': None, # (!) real value is "<class 'psycopg2.errors.FdwInvalidUseOfNullPointer'>"
    'HV00A': None, # (!) real value is "<class 'psycopg2.errors.FdwInvalidStringFormat'>"
    'HV00B': None, # (!) real value is "<class 'psycopg2.errors.FdwInvalidHandle'>"
    'HV00C': None, # (!) real value is "<class 'psycopg2.errors.FdwInvalidOptionIndex'>"
    'HV00D': None, # (!) real value is "<class 'psycopg2.errors.FdwInvalidOptionName'>"
    'HV00J': None, # (!) real value is "<class 'psycopg2.errors.FdwOptionNameNotFound'>"
    'HV00K': None, # (!) real value is "<class 'psycopg2.errors.FdwReplyHandle'>"
    'HV00L': None, # (!) real value is "<class 'psycopg2.errors.FdwUnableToCreateExecution'>"
    'HV00M': None, # (!) real value is "<class 'psycopg2.errors.FdwUnableToCreateReply'>"
    'HV00N': None, # (!) real value is "<class 'psycopg2.errors.FdwUnableToEstablishConnection'>"
    'HV00P': None, # (!) real value is "<class 'psycopg2.errors.FdwNoSchemas'>"
    'HV00Q': None, # (!) real value is "<class 'psycopg2.errors.FdwSchemaNotFound'>"
    'HV00R': None, # (!) real value is "<class 'psycopg2.errors.FdwTableNotFound'>"
    'HV010': None, # (!) real value is "<class 'psycopg2.errors.FdwFunctionSequenceError'>"
    'HV014': None, # (!) real value is "<class 'psycopg2.errors.FdwTooManyHandles'>"
    'HV021': None, # (!) real value is "<class 'psycopg2.errors.FdwInconsistentDescriptorInformation'>"
    'HV024': None, # (!) real value is "<class 'psycopg2.errors.FdwInvalidAttributeValue'>"
    'HV090': None, # (!) real value is "<class 'psycopg2.errors.FdwInvalidStringLengthOrBufferLength'>"
    'HV091': None, # (!) real value is "<class 'psycopg2.errors.FdwInvalidDescriptorFieldIdentifier'>"
    'P0000': None, # (!) real value is "<class 'psycopg2.errors.PlpgsqlError'>"
    'P0001': None, # (!) real value is "<class 'psycopg2.errors.RaiseException'>"
    'P0002': None, # (!) real value is "<class 'psycopg2.errors.NoDataFound'>"
    'P0003': None, # (!) real value is "<class 'psycopg2.errors.TooManyRows'>"
    'P0004': None, # (!) real value is "<class 'psycopg2.errors.AssertFailure'>"
    'XX000': None, # (!) real value is "<class 'psycopg2.errors.InternalError_'>"
    'XX001': None, # (!) real value is "<class 'psycopg2.errors.DataCorrupted'>"
    'XX002': None, # (!) real value is "<class 'psycopg2.errors.IndexCorrupted'>"
}

string_types = {} # real value of type <class 'dict'> replaced

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x778d259ce050>'

__spec__ = None # (!) real value is "ModuleSpec(name='psycopg2._psycopg', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x778d259ce050>, origin='/home/olenepal/.local/lib/python3.10/site-packages/psycopg2/_psycopg.cpython-310-x86_64-linux-gnu.so')"

