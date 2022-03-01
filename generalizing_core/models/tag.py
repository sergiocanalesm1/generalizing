from django.db import models

from generalizing_core.models.mixins.identity_mixin import  IdentityMixin

class Tag(IdentityMixin):
    
    _tag = models.CharField(
        db_column='tag',
        verbose_name='Tags',
        max_length=30
    )

    class Meta:
        verbose_name='Tag'
        verbose_name_plural='Tags'
        db_table='tags'