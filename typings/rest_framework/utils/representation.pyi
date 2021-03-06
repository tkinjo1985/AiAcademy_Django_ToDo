"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""
Helper functions for creating user-friendly representations
of serializer classes and serializer fields.
"""
def manager_repr(value):
    ...

def smart_repr(value):
    ...

def field_repr(field, force_many: bool = ...):
    ...

def serializer_repr(serializer, indent, force_many: Optional[Any] = ...):
    ...

def list_repr(serializer, indent):
    ...

