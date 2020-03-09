"""
This type stub file was generated by pyright.
"""

from collections import OrderedDict
from collections.abc import MutableMapping

class ReturnDict(OrderedDict):
    """
    Return object from `serializer.data` for the `Serializer` class.
    Includes a backlink to the serializer instance for renderers
    to use if they need richer field information.
    """
    def __init__(self, *args, **kwargs):
        self.serializer = ...
    
    def copy(self):
        ...
    
    def __repr__(self):
        ...
    
    def __reduce__(self):
        ...
    


class ReturnList(list):
    """
    Return object from `serializer.data` for the `SerializerList` class.
    Includes a backlink to the serializer instance for renderers
    to use if they need richer field information.
    """
    def __init__(self, *args, **kwargs):
        self.serializer = ...
    
    def __repr__(self):
        ...
    
    def __reduce__(self):
        ...
    


class BoundField:
    """
    A field object that also includes `.value` and `.error` properties.
    Returned when iterating over a serializer instance,
    providing an API similar to Django forms and form fields.
    """
    def __init__(self, field, value, errors, prefix=...):
        self.value = ...
        self.errors = ...
        self.name = ...
    
    def __getattr__(self, attr_name):
        ...
    
    @property
    def _proxy_class(self):
        ...
    
    def __repr__(self):
        ...
    
    def as_form_field(self):
        ...
    


class JSONBoundField(BoundField):
    def as_form_field(self):
        ...
    


class NestedBoundField(BoundField):
    """
    This `BoundField` additionally implements __iter__ and __getitem__
    in order to support nested bound fields. This class is the type of
    `BoundField` that is used for serializer fields.
    """
    def __init__(self, field, value, errors, prefix=...):
        ...
    
    def __iter__(self):
        ...
    
    def __getitem__(self, key):
        ...
    
    def as_form_field(self):
        ...
    


class BindingDict(MutableMapping):
    """
    This dict-like object is used to store fields on a serializer.

    This ensures that whenever fields are added to the serializer we call
    `field.bind()` so that the `field_name` and `parent` attributes
    can be set correctly.
    """
    def __init__(self, serializer):
        self.serializer = ...
        self.fields = ...
    
    def __setitem__(self, key, field):
        ...
    
    def __getitem__(self, key):
        ...
    
    def __delitem__(self, key):
        ...
    
    def __iter__(self):
        ...
    
    def __len__(self):
        ...
    
    def __repr__(self):
        ...
    

