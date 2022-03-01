from xxlimited import Null
from django.db import models

from generalizing_core.models.lesson import Lesson
from generalizing_core.models.mixins.identity_mixin import IdentityMixin
from generalizing_core.models.mixins.dates_mixin import DatesMixin
from generalizing_core.models.choices.type import Type

class Relation(IdentityMixin,DatesMixin):

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
        db_column='domain',
        verbose_name='Domain',
        blank=True,
        null=True,
        choices=Type.choices
    )

    class Meta:
        verbose_name='Relation'
        verbose_name_plural='Relations'
        db_table='relations'
    
    #TODO Business rule: lessons must be of different domains
