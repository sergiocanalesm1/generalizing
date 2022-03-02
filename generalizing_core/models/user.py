from django.db import models

from generalizing_core.models.mixins.identity_mixin import IdentityMixin

class User(IdentityMixin):
    
    username = models.CharField(
        verbose_name='Username',
        max_length=30,
    )

    password = models.CharField(
        verbose_name='Password',
        max_length=240,
    )

    email = models.EmailField(
        verbose_name='Email Address',
        unique=True
    )

    creation_date = models.DateTimeField(
        verbose_name='Creation Date',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural='Users'
        db_table = 'users'