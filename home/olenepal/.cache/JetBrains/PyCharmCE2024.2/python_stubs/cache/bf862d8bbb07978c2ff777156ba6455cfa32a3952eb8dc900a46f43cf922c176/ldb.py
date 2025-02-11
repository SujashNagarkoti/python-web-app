# encoding: utf-8
# module ldb
# from /usr/lib/python3/dist-packages/ldb.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" An interface to LDB, a LDAP-like API that can either to talk an embedded database (TDB-based) or a standards-compliant LDAP server. """
# no imports

# Variables with simple values

ATTR_FLAG_FORCE_BASE64_LDIF = 32

ATTR_FLAG_HIDDEN = 1

ATTR_FLAG_SINGLE_VALUE = 16

ATTR_FLAG_UNIQUE_INDEX = 8

CHANGETYPE_ADD = 1
CHANGETYPE_DELETE = 2
CHANGETYPE_MODIFY = 3
CHANGETYPE_NONE = 0

ERR_ADMIN_LIMIT_EXCEEDED = 11

ERR_AFFECTS_MULTIPLE_DSAS = 71

ERR_ALIAS_DEREFERENCING_PROBLEM = 36

ERR_ALIAS_DEREFERINCING_PROBLEM = 36

ERR_ALIAS_PROBLEM = 33

ERR_ATTRIBUTE_OR_VALUE_EXISTS = 20

ERR_AUTH_METHOD_NOT_SUPPORTED = 7

ERR_BUSY = 51

ERR_COMPARE_FALSE = 5
ERR_COMPARE_TRUE = 6

ERR_CONFIDENTIALITY_REQUIRED = 13

ERR_CONSTRAINT_VIOLATION = 19

ERR_ENTRY_ALREADY_EXISTS = 68

ERR_INAPPROPRIATE_AUTHENTICATION = 48
ERR_INAPPROPRIATE_MATCHING = 18

ERR_INSUFFICIENT_ACCESS_RIGHTS = 50

ERR_INVALID_ATTRIBUTE_SYNTAX = 21

ERR_INVALID_CREDENTIALS = 49

ERR_INVALID_DN_SYNTAX = 34

ERR_LOOP_DETECT = 54

ERR_NAMING_VIOLATION = 64

ERR_NOT_ALLOWED_ON_NON_LEAF = 66

ERR_NOT_ALLOWED_ON_RDN = 67

ERR_NO_SUCH_ATTRIBUTE = 16
ERR_NO_SUCH_OBJECT = 32

ERR_OBJECT_CLASS_MODS_PROHIBITED = 69

ERR_OBJECT_CLASS_VIOLATION = 65

ERR_OPERATIONS_ERROR = 1

ERR_OTHER = 80

ERR_PROTOCOL_ERROR = 2

ERR_REFERRAL = 10

ERR_SASL_BIND_IN_PROGRESS = 14

ERR_SIZE_LIMIT_EXCEEDED = 4

ERR_STRONG_AUTH_REQUIRED = 8

ERR_TIME_LIMIT_EXCEEDED = 3

ERR_UNAVAILABLE = 52

ERR_UNDEFINED_ATTRIBUTE_TYPE = 17

ERR_UNSUPPORTED_CRITICAL_EXTENSION = 12

ERR_UNWILLING_TO_PERFORM = 53

FLAG_FORCE_NO_BASE64_LDIF = 4

FLAG_MOD_ADD = 1
FLAG_MOD_DELETE = 3
FLAG_MOD_REPLACE = 2

FLG_DONT_CREATE_DB = 64

FLG_ENABLE_TRACING = 32

FLG_NOMMAP = 8
FLG_NOSYNC = 2
FLG_RDONLY = 1
FLG_RECONNECT = 4

FLG_SHOW_BINARY = 16

OID_COMPARATOR_AND = '1.2.840.113556.1.4.803'
OID_COMPARATOR_OR = '1.2.840.113556.1.4.804'

PACKING_FORMAT = 637606247

PACKING_FORMAT_V2 = 637606248

SCOPE_BASE = 0
SCOPE_DEFAULT = -1
SCOPE_ONELEVEL = 1
SCOPE_SUBTREE = 2

SEQ_HIGHEST_SEQ = 0
SEQ_HIGHEST_TIMESTAMP = 1

SEQ_NEXT = 2

SUCCESS = 0

SYNTAX_BOOLEAN = '1.3.6.1.4.1.1466.115.121.1.7'

SYNTAX_DIRECTORY_STRING = '1.3.6.1.4.1.1466.115.121.1.15'

SYNTAX_DN = '1.3.6.1.4.1.1466.115.121.1.12'
SYNTAX_INTEGER = '1.3.6.1.4.1.1466.115.121.1.27'

SYNTAX_OCTET_STRING = '1.3.6.1.4.1.1466.115.121.1.40'

SYNTAX_ORDERED_INTEGER = 'LDB_SYNTAX_ORDERED_INTEGER'

SYNTAX_UTC_TIME = '1.3.6.1.4.1.1466.115.121.1.53'

__docformat__ = 'restructuredText'

__version__ = '2.4.4'

# functions

def binary_decode(string): # real signature unknown; restored from __doc__
    """
    S.binary_decode(string) -> string
    
    Perform a RFC2254 binary decode on a string
    """
    return ""

def binary_encode(string): # real signature unknown; restored from __doc__
    """
    S.binary_encode(string) -> string
    
    Perform a RFC2254 binary encoding on a string
    """
    return ""

def register_module(module): # real signature unknown; restored from __doc__
    """
    S.register_module(module) -> None
    
    Register a LDB module.
    """
    pass

def string_to_time(string): # real signature unknown; restored from __doc__
    """
    S.string_to_time(string) -> int
    
    Parse a LDAP time string into a UNIX timestamp.
    """
    return 0

def timestring(p_int): # real signature unknown; restored from __doc__
    """
    S.timestring(int) -> string
    
    Generate a LDAP time string from a UNIX timestamp
    """
    return ""

def valid_attr_name(name): # real signature unknown; restored from __doc__
    """
    S.valid_attr_name(name) -> bool
    
    Check whether the supplied name is a valid attribute name.
    """
    return False

# classes

class Control(object):
    """ LDB control. """
    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    critical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    oid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Dn(object):
    """ A LDB distinguished name. """
    def add_base(self, dn): # real signature unknown; restored from __doc__
        """
        S.add_base(dn) -> None
        Add a base DN to this DN.
        """
        pass

    def add_child(self, dn): # real signature unknown; restored from __doc__
        """
        S.add_child(dn) -> None
        Add a child DN to this DN.
        """
        pass

    def canonical_ex_str(self): # real signature unknown; restored from __doc__
        """
        S.canonical_ex_str() -> string
        Canonical version of this DN (like a posix path, with terminating newline).
        """
        return ""

    def canonical_str(self): # real signature unknown; restored from __doc__
        """
        S.canonical_str() -> string
        Canonical version of this DN (like a posix path).
        """
        return ""

    def check_special(self, name): # real signature unknown; restored from __doc__
        """
        S.check_special(name) -> bool
        
        Check if name is a special DN name
        """
        return False

    def extended_str(self, mode=1): # real signature unknown; restored from __doc__
        """
        S.extended_str(mode=1) -> string
        Extended version of this DN
        """
        return ""

    def get_casefold(self, *args, **kwargs): # real signature unknown
        pass

    def get_component_name(self, num): # real signature unknown; restored from __doc__
        """
        S.get_component_name(num) -> string
        get the attribute name of the specified component
        """
        return ""

    def get_component_value(self, num): # real signature unknown; restored from __doc__
        """
        S.get_component_value(num) -> string
        get the attribute value of the specified component as a binary string
        """
        return ""

    def get_extended_component(self, name): # real signature unknown; restored from __doc__
        """
        S.get_extended_component(name) -> string
        
        returns a DN extended component as a binary string
        """
        return ""

    def get_linearized(self, *args, **kwargs): # real signature unknown
        pass

    def get_rdn_name(self): # real signature unknown; restored from __doc__
        """
        S.get_rdn_name() -> string
        get the RDN attribute name
        """
        return ""

    def get_rdn_value(self): # real signature unknown; restored from __doc__
        """
        S.get_rdn_value() -> string
        get the RDN attribute value as a binary string
        """
        return ""

    def is_child_of(self, basedn): # real signature unknown; restored from __doc__
        """
        S.is_child_of(basedn) -> int
        Returns True if this DN is a child of basedn
        """
        return 0

    def is_null(self, *args, **kwargs): # real signature unknown
        """ Check whether this is a null DN. """
        pass

    def is_special(self): # real signature unknown; restored from __doc__
        """
        S.is_special() -> bool
        Check whether this is a special LDB DN.
        """
        return False

    def is_valid(self): # real signature unknown; restored from __doc__
        """ S.is_valid() -> bool """
        return False

    def parent(self): # real signature unknown; restored from __doc__
        """
        S.parent() -> dn
        Get the parent for this DN.
        """
        pass

    def remove_base_components(self, p_int): # real signature unknown; restored from __doc__
        """
        S.remove_base_components(int) -> bool
        Remove a number of DN components from the base of this DN.
        """
        return False

    def set_component(self, num, name, value): # real signature unknown; restored from __doc__
        """
        S.set_component(num, name, value) -> None
        set the attribute name and value of the specified component
        """
        pass

    def set_extended_component(self, name, value): # real signature unknown; restored from __doc__
        """
        S.set_extended_component(name, value) -> None
        
        set a DN extended component as a binary string
        """
        pass

    def validate(self): # real signature unknown; restored from __doc__
        """
        S.validate() -> bool
        Validate DN is correct.
        """
        return False

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    __hash__ = None


class Ldb(object):
    """ Connection to a LDB database. """
    def add(self, message, controls=None): # real signature unknown; restored from __doc__
        """
        S.add(message, controls=None) -> None
        Add an entry.
        """
        pass

    def connect(self, url, flags=0, options=None): # real signature unknown; restored from __doc__
        """
        S.connect(url, flags=0, options=None) -> None
        Connect to a LDB URL.
        """
        pass

    def delete(self, dn, controls=None): # real signature unknown; restored from __doc__
        """
        S.delete(dn, controls=None) -> None
        Remove an entry.
        """
        pass

    def get_config_basedn(self, *args, **kwargs): # real signature unknown
        pass

    def get_default_basedn(self, *args, **kwargs): # real signature unknown
        pass

    def get_opaque(self, name): # real signature unknown; restored from __doc__
        """
        S.get_opaque(name) -> value
        Get an opaque value set on this LDB connection. 
        :note: The returned value may not be useful in Python.
        """
        pass

    def get_root_basedn(self, *args, **kwargs): # real signature unknown
        pass

    def get_schema_basedn(self, *args, **kwargs): # real signature unknown
        pass

    def modify(self, message, controls=None, validate=False): # real signature unknown; restored from __doc__
        """
        S.modify(message, controls=None, validate=False) -> None
        Modify an entry.
        """
        pass

    def modules(self): # real signature unknown; restored from __doc__
        """
        S.modules() -> list
        Return the list of modules on this LDB connection
        """
        return []

    def msg_diff(self, Message): # real signature unknown; restored from __doc__
        """
        S.msg_diff(Message) -> Message
        Return an LDB Message of the difference between two Message objects.
        """
        return Message

    def parse_ldif(self, ldif): # real signature unknown; restored from __doc__
        """
        S.parse_ldif(ldif) -> iter(messages)
        Parse a string formatted using LDIF.
        """
        pass

    def rename(self, old_dn, new_dn, controls=None): # real signature unknown; restored from __doc__
        """
        S.rename(old_dn, new_dn, controls=None) -> None
        Rename an entry.
        """
        pass

    def schema_attribute_add(self, *args, **kwargs): # real signature unknown
        pass

    def schema_attribute_remove(self, *args, **kwargs): # real signature unknown
        pass

    def schema_format_value(self, *args, **kwargs): # real signature unknown
        pass

    def search(self, base=None, scope=None, expression=None, attrs=None, controls=None): # real signature unknown; restored from __doc__
        """
        S.search(base=None, scope=None, expression=None, attrs=None, controls=None) -> result
        Search in a database.
        
        :param base: Optional base DN to search
        :param scope: Search scope (SCOPE_BASE, SCOPE_ONELEVEL or SCOPE_SUBTREE)
        :param expression: Optional search expression
        :param attrs: Attributes to return (defaults to all)
        :param controls: Optional list of controls
        :return: ldb.Result object
        """
        pass

    def search_iterator(self, base=None, scope=None, expression=None, attrs=None, controls=None, timeout=None): # real signature unknown; restored from __doc__
        """
        S.search_iterator(base=None, scope=None, expression=None, attrs=None, controls=None, timeout=None) -> iterator
        Search in a database.
        
        :param base: Optional base DN to search
        :param scope: Search scope (SCOPE_BASE, SCOPE_ONELEVEL or SCOPE_SUBTREE)
        :param expression: Optional search expression
        :param attrs: Attributes to return (defaults to all)
        :param controls: Optional list of controls
        :param timeout: Optional timeout in seconds (defaults to 300), 0 means the default, -1 no timeout
        :return: ldb.SearchIterator object that provides results when they arrive
        """
        pass

    def sequence_number(self, type): # real signature unknown; restored from __doc__
        """
        S.sequence_number(type) -> value
        Return the value of the sequence according to the requested type
        """
        pass

    def setup_wellknown_attributes(self, *args, **kwargs): # real signature unknown
        pass

    def set_create_perms(self, mode): # real signature unknown; restored from __doc__
        """
        S.set_create_perms(mode) -> None
        Set mode to use when creating new LDB files.
        """
        pass

    def set_debug(self, callback): # real signature unknown; restored from __doc__
        """
        S.set_debug(callback) -> None
        Set callback for LDB debug messages.
        The callback should accept a debug level and debug text.
        """
        pass

    def set_modules_dir(self, path): # real signature unknown; restored from __doc__
        """
        S.set_modules_dir(path) -> None
        Set path LDB should search for modules
        """
        pass

    def set_opaque(self, name, value): # real signature unknown; restored from __doc__
        """
        S.set_opaque(name, value) -> None
        Set an opaque value on this LDB connection. 
        :note: Passing incorrect values may cause crashes.
        """
        pass

    def transaction_cancel(self): # real signature unknown; restored from __doc__
        """
        S.transaction_cancel() -> None
        cancel a new transaction.
        """
        pass

    def transaction_commit(self): # real signature unknown; restored from __doc__
        """
        S.transaction_commit() -> None
        commit a new transaction.
        """
        pass

    def transaction_prepare_commit(self): # real signature unknown; restored from __doc__
        """
        S.transaction_prepare_commit() -> None
        prepare to commit a new transaction (2-stage commit).
        """
        pass

    def transaction_start(self): # real signature unknown; restored from __doc__
        """
        S.transaction_start() -> None
        Start a new transaction.
        """
        pass

    def write_ldif(self, message, changetype): # real signature unknown; restored from __doc__
        """
        S.write_ldif(message, changetype) -> ldif
        Print the message as a string formatted using LDIF.
        """
        pass

    def _register_test_extensions(self): # real signature unknown; restored from __doc__
        """
        S._register_test_extensions() -> None
        Register internal extensions used in testing
        """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    firstmodule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class LdbError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Message(object):
    """ A LDB Message """
    def add(self, element): # real signature unknown; restored from __doc__
        """
        S.add(element)
        
        Add an element to this message.
        """
        pass

    def elements(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def from_dict(cls, ldb, dict, mod_flag=None): # real signature unknown; restored from __doc__
        """
        Message.from_dict(ldb, dict, mod_flag=FLAG_MOD_REPLACE) -> ldb.Message
        Class method to create ldb.Message object from Dictionary.
        mod_flag is one of FLAG_MOD_ADD, FLAG_MOD_REPLACE or FLAG_MOD_DELETE.
        """
        pass

    def get(self, name, default=None, idx=None): # real signature unknown; restored from __doc__
        """
        msg.get(name,default=None,idx=None) -> string
        idx is the index into the values array
        if idx is None, then a list is returned
        if idx is not None, then the element with that index is returned
        if you pass the special name 'dn' then the DN object is returned
        """
        return ""

    def items(self, *args, **kwargs): # real signature unknown
        pass

    def keys(self): # real signature unknown; restored from __doc__
        """
        S.keys() -> list
        
        Return sequence of all attribute names.
        """
        return []

    def remove(self, name): # real signature unknown; restored from __doc__
        """
        S.remove(name)
        
        Remove all entries for attributes with the specified name.
        """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
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

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    dn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


class MessageElement(object):
    """ An element of a Message """
    def flags(self, *args, **kwargs): # real signature unknown
        pass

    def get(self, *args, **kwargs): # real signature unknown
        pass

    def set_flags(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


class Module(object):
    """ LDB module (extension) """
    def add(self, *args, **kwargs): # real signature unknown
        pass

    def delete(self, *args, **kwargs): # real signature unknown
        pass

    def del_transaction(self, *args, **kwargs): # real signature unknown
        pass

    def end_transaction(self, *args, **kwargs): # real signature unknown
        pass

    def modify(self, *args, **kwargs): # real signature unknown
        pass

    def rename(self, *args, **kwargs): # real signature unknown
        pass

    def search(self, *args, **kwargs): # real signature unknown
        pass

    def start_transaction(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class Tree(object):
    """ A search tree """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7874c8382320>'

__spec__ = None # (!) real value is "ModuleSpec(name='ldb', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7874c8382320>, origin='/usr/lib/python3/dist-packages/ldb.cpython-310-x86_64-linux-gnu.so')"

