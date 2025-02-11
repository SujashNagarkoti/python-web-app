# encoding: utf-8
# module psycopg2._psycopg
# from /home/olenepal/.local/lib/python3.10/site-packages/psycopg2/_psycopg.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" psycopg2 PostgreSQL driver """

# imports
import psycopg2 as __psycopg2
import psycopg2.extensions as __psycopg2_extensions


from .object import object

class Column(object):
    """
    Description of a column returned by a query.
    
    The DBAPI demands this object to be a 7-items sequence. This object
    respects this interface, but adds names for the exposed attributes
    and adds attribute not requested by the DBAPI.
    """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    display_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The actual length of the column in bytes.

Obtaining this value is computationally intensive, so it is always None"""

    internal_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size in bytes of the column associated to this column on the server.

Set to a negative value for variable-size types."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the column returned."""

    null_ok = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Always none."""

    precision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Total number of significant digits in columns of type NUMERIC.

None for other types."""

    scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Count of decimal digits in the fractional part in columns of type NUMERIC.

None for other types."""

    table_column = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number (within its table) of the column making up the result

None if not available. Note that PostgreSQL column numbers start at 1"""

    table_oid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The OID of the table from which the column was fetched.

None if not available"""

    type_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The PostgreSQL OID of the column.

You can use the pg_type system table to get more informations about the
type. This is the value used by Psycopg to decide what Python type use
to represent the value"""


    __hash__ = None


