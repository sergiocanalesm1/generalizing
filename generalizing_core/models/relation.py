from django.db import models

from generalizing_core.models.lesson import Lesson
from generalizing_core.models.user import User
from generalizing_core.models.mixins.identity_mixin import IdentityMixin
from generalizing_core.models.choices.type import Type
from generalizing_core.models.challenge import Challenge

class Relation(IdentityMixin):

    user = models.ForeignKey(
        User,
        verbose_name='User',
        on_delete=models.PROTECT
    )

    creation_date = models.DateTimeField(
        verbose_name='Creation Date',
        auto_now_add=True
    )

    lessons = models.ManyToManyField(
        Lesson,
        verbose_name='Lessons',
    )

    explanation = models.TextField(
        verbose_name='Explanation',
    )

    type = models.CharField(
        max_length=50,
        verbose_name='Type',
        blank=True,
        null=True,
        choices=Type.choices
    )

    challenge = models.ForeignKey(
        Challenge,
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
