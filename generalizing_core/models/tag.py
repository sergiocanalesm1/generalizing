from django.db import models

from generalizing_core.models.mixins.identity_mixin import  IdentityMixin

class Tag(IdentityMixin):
    
    tag = models.CharField(
        verbose_name='Tags',
        max_length=50
    )

    class Meta:
        verbose_name='Tag'
        verbose_name_plural='Tags'
        db_table='tags'