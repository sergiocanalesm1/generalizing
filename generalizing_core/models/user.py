from django.db import models
from django.contrib.auth.models import AbstractUser

from generalizing_core.models.mixins.identity_mixin import IdentityMixin

class User(AbstractUser,IdentityMixin):

    email = models.EmailField(
        verbose_name='Email Address',
        unique=True,
        blank=False,
        null=False
    )

    birth_date = models.DateField(
        verbose_name='Birth Date',
        blank=True,
        null=True
    )

    #TODO create choices
    gender = models.CharField(
        max_length=20,
        verbose_name='Gender',
        null=True,
        blank=True,
    )

    #TODO create choices
    workspace = models.CharField(
        max_length=100,
        verbose_name='Work Space',
        null=True,
        blank=True,
    )

    #TODO create choices
    city_population = models.CharField(
        max_length=50,
        verbose_name='City Population',
        null=True,
        blank=True,
    )

    #TODO create choices
    average_weekly_sleep_hrs = models.CharField(
        max_length=50,
        verbose_name='Average Weekly Sleep Hours',
        null=True,
        blank=True,
    )

    creation_date = models.DateTimeField(
        verbose_name='Creation Date',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural='Users'
        db_table = 'users'