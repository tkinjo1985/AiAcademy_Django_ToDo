"""
This type stub file was generated by pyright.
"""

"""
Provides generic filtering backends that can be used to filter the results
returned by list views.
"""
class BaseFilterBackend:
    """
    A base class from which all filter backend classes should inherit.
    """
    def filter_queryset(self, request, queryset, view):
        """
        Return a filtered queryset.
        """
        ...
    
    def get_schema_fields(self, view):
        ...
    
    def get_schema_operation_parameters(self, view):
        ...
    


class SearchFilter(BaseFilterBackend):
    search_param = ...
    template = ...
    lookup_prefixes = ...
    search_title = ...
    search_description = ...
    def get_search_fields(self, view, request):
        """
        Search fields are obtained from the view, but the request is always
        passed to this method. Sub-classes can override this method to
        dynamically change the search fields based on request content.
        """
        ...
    
    def get_search_terms(self, request):
        """
        Search terms are set by a ?search=... query parameter,
        and may be comma and/or whitespace delimited.
        """
        ...
    
    def construct_search(self, field_name):
        ...
    
    def must_call_distinct(self, queryset, search_fields):
        """
        Return True if 'distinct()' should be used to query the given lookups.
        """
        ...
    
    def filter_queryset(self, request, queryset, view):
        ...
    
    def to_html(self, request, queryset, view):
        ...
    
    def get_schema_fields(self, view):
        ...
    
    def get_schema_operation_parameters(self, view):
        ...
    


class OrderingFilter(BaseFilterBackend):
    ordering_param = ...
    ordering_fields = ...
    ordering_title = ...
    ordering_description = ...
    template = ...
    def get_ordering(self, request, queryset, view):
        """
        Ordering is set by a comma delimited ?ordering=... query parameter.

        The `ordering` query parameter can be overridden by setting
        the `ordering_param` value on the OrderingFilter or by
        specifying an `ORDERING_PARAM` value in the API settings.
        """
        ...
    
    def get_default_ordering(self, view):
        ...
    
    def get_default_valid_fields(self, queryset, view, context=...):
        ...
    
    def get_valid_fields(self, queryset, view, context=...):
        ...
    
    def remove_invalid_fields(self, queryset, fields, view, request):
        ...
    
    def filter_queryset(self, request, queryset, view):
        ...
    
    def get_template_context(self, request, queryset, view):
        ...
    
    def to_html(self, request, queryset, view):
        ...
    
    def get_schema_fields(self, view):
        ...
    
    def get_schema_operation_parameters(self, view):
        ...
    

