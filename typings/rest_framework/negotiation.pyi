"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""
Content negotiation deals with selecting an appropriate renderer given the
incoming request.  Typically this will be based on the request's Accept header.
"""
class BaseContentNegotiation:
    def select_parser(self, request, parsers):
        ...
    
    def select_renderer(self, request, renderers, format_suffix: Optional[Any] = ...):
        ...
    


class DefaultContentNegotiation(BaseContentNegotiation):
    settings = ...
    def select_parser(self, request, parsers):
        """
        Given a list of parsers and a media type, return the appropriate
        parser to handle the incoming request.
        """
        ...
    
    def select_renderer(self, request, renderers, format_suffix: Optional[Any] = ...):
        """
        Given a request and a list of renderers, return a two-tuple of:
        (renderer, media type).
        """
        ...
    
    def filter_renderers(self, renderers, format):
        """
        If there is a '.json' style format suffix, filter the renderers
        so that we only negotiation against those that accept that format.
        """
        ...
    
    def get_accept_list(self, request):
        """
        Given the incoming request, return a tokenized list of media
        type strings.
        """
        ...
    


