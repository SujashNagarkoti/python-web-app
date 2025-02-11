# encoding: utf-8
# module psycopg2._psycopg
# from /home/olenepal/.local/lib/python3.10/site-packages/psycopg2/_psycopg.cpython-310-x86_64-linux-gnu.so
# by generator 1.147
""" psycopg2 PostgreSQL driver """

# imports
import psycopg2 as __psycopg2
import psycopg2.extensions as __psycopg2_extensions


class ReplicationCursor(__psycopg2_extensions.cursor):
    """ A database replication cursor. """
    def consume_stream(self, consumer, keepalive_interval=None): # real signature unknown; restored from __doc__
        """ consume_stream(consumer, keepalive_interval=None) -- Consume replication stream. """
        pass

    def read_message(self): # real signature unknown; restored from __doc__
        """ read_message() -- Try reading a replication message from the server (non-blocking). """
        pass

    def send_feedback(self, write_lsn=0, flush_lsn=0, apply_lsn=0, reply=False, force=False): # real signature unknown; restored from __doc__
        """ send_feedback(write_lsn=0, flush_lsn=0, apply_lsn=0, reply=False, force=False) -- Update a replication feedback, optionally request a reply or force sending a feedback message regardless of the timeout. """
        pass

    def start_replication_expert(self, command, decode=False, status_interval=10): # real signature unknown; restored from __doc__
        """ start_replication_expert(command, decode=False, status_interval=10) -- Start replication with a given command. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    feedback_timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """feedback_timestamp -- the timestamp of the latest feedback message sent to the server"""

    io_timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """io_timestamp -- the timestamp of latest IO with the server"""

    wal_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """LSN position of the current end of WAL on the server."""



