"""
This type stub file was generated by pyright.
"""

"""
inspectors.py   # Per-endpoint view introspection

See schemas.__init__.py for package overview.
"""
class ViewInspector:
    """
    Descriptor class on APIView.

    Provide subclass for per-view schema generation
    """
    header_regex = ...
    def __init__(self):
        self.instance_schemas = ...
    
    def __get__(self, instance, owner):
        """
        Enables `ViewInspector` as a Python _Descriptor_.

        This is how `view.schema` knows about `view`.

        `__get__` is called when the descriptor is accessed on the owner.
        (That will be when view.schema is called in our case.)

        `owner` is always the owner class. (An APIView, or subclass for us.)
        `instance` is the view instance or `None` if accessed from the class,
        rather than an instance.

        See: https://docs.python.org/3/howto/descriptor.html for info on
        descriptor usage.
        """
        self.view = ...
    
    def __set__(self, instance, other):
        ...
    
    @property
    def view(self):
        """View property."""
        ...
    
    @view.setter
    def view(self, value):
        ...
    
    @view.deleter
    def view(self):
        ...
    
    def get_description(self, path, method):
        """
        Determine a path description.

        This will be based on the method docstring if one exists,
        or else the class docstring.
        """
        ...
    
    def _get_description_section(self, view, header, description):
        ...
    


class DefaultSchema(ViewInspector):
    """Allows overriding AutoSchema using DEFAULT_SCHEMA_CLASS setting"""
    def __get__(self, instance, owner):
        ...
    


