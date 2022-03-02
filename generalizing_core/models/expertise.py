from django.db import models

from generalizing_core.models.mixins.identity_mixin import IdentityMixin
from generalizing_core.models.choices.domain import Domain
from generalizing_core.models.user import User

class Expertise(IdentityMixin):
    
    area = models.CharField(
        max_length=100,
        verbose_name='Domain',
        blank=True,
        null=True,
        choices=Domain.choices
    )

    description = models.TextField(
        verbose_name='Description',
        blank=True,
        null=True
    )

    user = models.ForeignKey( 
        User,
        verbose_name='User',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name='Expertise'
        verbose_name_plural='Expertises'
        db_table='expertises'