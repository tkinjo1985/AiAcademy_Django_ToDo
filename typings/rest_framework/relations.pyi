"""
This type stub file was generated by pyright.
"""

from rest_framework.fields import Field
from rest_framework.reverse import reverse
from typing import Any, Optional

def method_overridden(method_name, klass, instance):
    """
    Determine if a method has been overridden.
    """
    ...

class ObjectValueError(ValueError):
    """
    Raised when `queryset.get()` failed due to an underlying `ValueError`.
    Wrapping prevents calling code conflating this with unrelated errors.
    """
    ...


class ObjectTypeError(TypeError):
    """
    Raised when `queryset.get()` failed due to an underlying `TypeError`.
    Wrapping prevents calling code conflating this with unrelated errors.
    """
    ...


class Hyperlink(str):
    """
    A string like object that additionally has an associated name.
    We use this for hyperlinked URLs that may render as a named link
    in some contexts, or render as a plain URL in others.
    """
    def __new__(cls, url, obj):
        ...
    
    def __getnewargs__(self):
        ...
    
    @property
    def name(self):
        ...
    
    is_hyperlink = ...


class PKOnlyObject:
    """
    This is a mock object, used for when we only need the pk of the object
    instance, but still want to return an object with a .pk attribute,
    in order to keep the same interface as a regular model instance.
    """
    def __init__(self, pk):
        self.pk = ...
    
    def __str__(self):
        ...
    


MANY_RELATION_KWARGS = ('read_only', 'write_only', 'required', 'default', 'initial', 'source', 'label', 'help_text', 'style', 'error_messages', 'allow_empty', 'html_cutoff', 'html_cutoff_text')
class RelatedField(Field):
    queryset = ...
    html_cutoff = ...
    html_cutoff_text = ...
    def __init__(self, **kwargs):
        self.queryset = ...
        self.html_cutoff = ...
        self.html_cutoff_text = ...
    
    def __new__(cls, *args, **kwargs):
        ...
    
    @classmethod
    def many_init(cls, *args, **kwargs):
        """
        This method handles creating a parent `ManyRelatedField` instance
        when the `many=True` keyword argument is passed.

        Typically you won't need to override this method.

        Note that we're over-cautious in passing most arguments to both parent
        and child classes in order to try to cover the general case. If you're
        overriding this method you'll probably want something much simpler, eg:

        @classmethod
        def many_init(cls, *args, **kwargs):
            kwargs['child'] = cls()
            return CustomManyRelatedField(*args, **kwargs)
        """
        ...
    
    def run_validation(self, data=...):
        ...
    
    def get_queryset(self):
        ...
    
    def use_pk_only_optimization(self):
        ...
    
    def get_attribute(self, instance):
        ...
    
    def get_choices(self, cutoff: Optional[Any] = ...):
        ...
    
    @property
    def choices(self):
        ...
    
    @property
    def grouped_choices(self):
        ...
    
    def iter_options(self):
        ...
    
    def display_value(self, instance):
        ...
    


class StringRelatedField(RelatedField):
    """
    A read only field that represents its targets using their
    plain string representation.
    """
    def __init__(self, **kwargs):
        ...
    
    def to_representation(self, value):
        ...
    


class PrimaryKeyRelatedField(RelatedField):
    default_error_messages = ...
    def __init__(self, **kwargs):
        self.pk_field = ...
    
    def use_pk_only_optimization(self):
        ...
    
    def to_internal_value(self, data):
        ...
    
    def to_representation(self, value):
        ...
    


class HyperlinkedRelatedField(RelatedField):
    lookup_field = ...
    view_name = ...
    default_error_messages = ...
    def __init__(self, view_name: Optional[Any] = ..., **kwargs):
        self.lookup_field = ...
        self.lookup_url_kwarg = ...
        self.format = ...
        self.reverse = ...
    
    def use_pk_only_optimization(self):
        ...
    
    def get_object(self, view_name, view_args, view_kwargs):
        """
        Return the object corresponding to a matched URL.

        Takes the matched URL conf arguments, and should return an
        object instance, or raise an `ObjectDoesNotExist` exception.
        """
        ...
    
    def get_url(self, obj, view_name, request, format):
        """
        Given an object, return the URL that hyperlinks to the object.

        May raise a `NoReverseMatch` if the `view_name` and `lookup_field`
        attributes are not configured to correctly match the URL conf.
        """
        ...
    
    def to_internal_value(self, data):
        ...
    
    def to_representation(self, value):
        ...
    


class HyperlinkedIdentityField(HyperlinkedRelatedField):
    """
    A read-only field that represents the identity URL for an object, itself.

    This is in contrast to `HyperlinkedRelatedField` which represents the
    URL of relationships to other objects.
    """
    def __init__(self, view_name: Optional[Any] = ..., **kwargs):
        ...
    
    def use_pk_only_optimization(self):
        ...
    


class SlugRelatedField(RelatedField):
    """
    A read-write field that represents the target of the relationship
    by a unique 'slug' attribute.
    """
    default_error_messages = ...
    def __init__(self, slug_field: Optional[Any] = ..., **kwargs):
        self.slug_field = ...
    
    def to_internal_value(self, data):
        ...
    
    def to_representation(self, obj):
        ...
    


class ManyRelatedField(Field):
    """
    Relationships with `many=True` transparently get coerced into instead being
    a ManyRelatedField with a child relationship.

    The `ManyRelatedField` class is responsible for handling iterating through
    the values and passing each one to the child relationship.

    This class is treated as private API.
    You shouldn't generally need to be using this class directly yourself,
    and should instead simply set 'many=True' on the relationship.
    """
    initial = ...
    default_empty_html = ...
    default_error_messages = ...
    html_cutoff = ...
    html_cutoff_text = ...
    def __init__(self, child_relation: Optional[Any] = ..., *args, **kwargs):
        self.child_relation = ...
        self.allow_empty = ...
        self.html_cutoff = ...
        self.html_cutoff_text = ...
    
    def get_value(self, dictionary):
        ...
    
    def to_internal_value(self, data):
        ...
    
    def get_attribute(self, instance):
        ...
    
    def to_representation(self, iterable):
        ...
    
    def get_choices(self, cutoff: Optional[Any] = ...):
        ...
    
    @property
    def choices(self):
        ...
    
    @property
    def grouped_choices(self):
        ...
    
    def iter_options(self):
        ...
    


