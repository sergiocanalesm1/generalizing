from django.db import models

from generalizing_core.models.lesson import Lesson
from generalizing_core.models.user import User
from generalizing_core.models.mixins.identity_mixin import IdentityMixin
from generalizing_core.models.mixins.dates_mixin import DatesMixin
from generalizing_core.models.choices.type import Type
from generalizing_core.models.challenge import Challenge

class Relation(IdentityMixin,DatesMixin):

    _user = models.ForeignKey(
        User,
        db_column='user',
        verbose_name='User',
        on_delete=models.PROTECT
    )

    _lessons = models.ManyToManyField(
        Lesson,
        db_column='lesson',
        verbose_name='Lessons',
    )

    _explanation = models.TextField(
        db_column='explanation',
        verbose_name='Explanation',
        blank=False,
        null=False
    )

    _type = models.CharField(
        max_length=50,
        db_column='domain',
        verbose_name='Domain',
        blank=True,
        null=True,
        choices=Type.choices
    )

    _challenge = models.ForeignKey(
        Challenge,
        db_column='challenge',
        verbose_name='Challenge',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name='Relation'
        verbose_name_plural='Relations'
        db_table='relations'
    
    #TODO Business rule: lessons must be of different domains
