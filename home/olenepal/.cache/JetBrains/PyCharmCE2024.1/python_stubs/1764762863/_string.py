# encoding: utf-8
# module _string
# from (built-in)
# by generator 1.147
""" string helper module """
# no imports

# functions

def formatter_field_name_split(*args, **kwargs): # real signature unknown
    """ split the argument as a field name """
    pass

def formatter_parser(*args, **kwargs): # real signature unknown
    """ parse the argument as a format string """
    pass

# classes

class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    def create_module(spec): # reliably restored by inspect
        """ Create a built-in module """
        pass

    def exec_module(module): # reliably restored by inspect
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module() instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod(<function BuiltinImporter.module_repr at 0x74d5c2752290>)>, 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x74d5c2752320>)>, 'find_module': <classmethod(<function BuiltinImporter.find_module at 0x74d5c27523b0>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x74d5c2752440>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x74d5c27524d0>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x74d5c27525f0>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x74d5c2752710>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x74d5c2752830>)>, 'load_module': <classmethod(<function _load_module_shim at 0x74d5c2751750>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_string', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

