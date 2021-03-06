"""
This type stub file was generated by pyright.
"""

from django.db import models

"""
Helper functions for mapping model fields to a dictionary of default
keyword arguments that should be used for their equivalent serializer fields.
"""
NUMERIC_FIELD_TYPES = (models.IntegerField, models.FloatField, models.DecimalField, models.DurationField)
class ClassLookupDict:
    """
    Takes a dictionary with classes as keys.
    Lookups against this object will traverses the object's inheritance
    hierarchy in method resolution order, and returns the first matching value
    from the dictionary or raises a KeyError if nothing matches.
    """
    def __init__(self, mapping):
        self.mapping = ...
    
    def __getitem__(self, key):
        ...
    
    def __setitem__(self, key, value):
        ...
    


def needs_label(model_field, field_name):
    """
    Returns `True` if the label based on the model's verbose name
    is not equal to the default label it would have based on it's field name.
    """
    ...

def get_detail_view_name(model):
    """
    Given a model class, return the view name to use for URL relationships
    that refer to instances of the model.
    """
    ...

def get_field_kwargs(field_name, model_field):
    """
    Creates a default instance of a basic non-relational field.
    """
    ...

def get_relation_kwargs(field_name, relation_info):
    """
    Creates a default instance of a flat relational field.
    """
    ...

def get_nested_relation_kwargs(relation_info):
    ...

def get_url_kwargs(model_field):
    ...

