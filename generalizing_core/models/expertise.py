from django.db import models

from generalizing_core.models.mixins.identity_mixin import IdentityMixin
from generalizing_core.models.choices.domain import Domain
from generalizing_core.models.user import User

class Expertise(IdentityMixin):
    
    _area = models.CharField(
        max_length=100,
        db_column='domain',
        verbose_name='Domain',
        blank=True,
        null=True,
        choices=Domain.choices
    )

    _description = models.TextField(
        db_column='description',
        verbose_name='Description',
        blank=True,
        null=True
    )

    _user = models.ForeignKey( 
        User,
        db_column='user',
        verbose_name='User',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name='Expertise'
        verbose_name_plural='Expertises'
        db_table='expertises'