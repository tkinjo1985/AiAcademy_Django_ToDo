"""
This type stub file was generated by pyright.
"""

from django.db import models

class Token(models.Model):
    """
    The default authorization token model.
    """
    key = ...
    user = ...
    created = ...
    class Meta:
        abstract = ...
        verbose_name = ...
        verbose_name_plural = ...
    
    
    def save(self, *args, **kwargs):
        ...
    
    def generate_key(self):
        ...
    
    def __str__(self):
        ...
    


