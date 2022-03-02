from statistics import mode
from tabnanny import verbose
from django.db import models

from generalizing_core.models.mixins.identity_mixin import IdentityMixin
from generalizing_core.models.mixins.dates_mixin import DatesMixin

class User(IdentityMixin,DatesMixin):
    
    _name = models.CharField(
        db_column='name',
        verbose_name='Name',
        max_length=30,
        null=True,
        blank=True
    )

    _password = models.CharField(
        verbose_name='Password',
        max_length=240,
        null=True,
        blank=True
    )

    email = models.EmailField(
        db_column = 'email',
        verbose_name='Email Address',
        unique=True
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural='Users'
        db_table = 'users'