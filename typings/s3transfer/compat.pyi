"""This type stub file was generated by pyright."""

import socket
import sys

from botocore.compat import six

if sys.platform.startswith("win"):
    def rename_file(current_filename, new_filename): ...

else:
    rename_file = ...
if six.PY3:
    def accepts_kwargs(func): ...
    SOCKET_ERROR = ...
    MAXINT = ...
else:
    def accepts_kwargs(func): ...
    SOCKET_ERROR = socket.error
    MAXINT = ...

def seekable(fileobj): ...
def readable(fileobj): ...
def fallocate(fileobj, size): ...
