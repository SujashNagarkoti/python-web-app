# encoding: utf-8
# module psycopg2._psycopg
# from /home/olenepal/.local/lib/python3.10/site-packages/psycopg2/_psycopg.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" psycopg2 PostgreSQL driver """

# imports
import psycopg2 as __psycopg2
import psycopg2.extensions as __psycopg2_extensions


class ReplicationConnection(__psycopg2_extensions.connection):
    """ A replication connection. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    autocommit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    isolation_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replication_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """replication_type -- the replication connection type"""

    reset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_isolation_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_session = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



