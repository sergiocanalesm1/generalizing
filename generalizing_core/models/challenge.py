from django.db import models

from generalizing_core.models.user import User
from generalizing_core.models.lesson import Lesson
from generalizing_core.models.mixins.dates_mixin import DatesMixin
from generalizing_core.models.mixins.identity_mixin import IdentityMixin

class Challenge(IdentityMixin,DatesMixin):
    _user = models.ManyToManyField(
        User,
        db_column='user',
        verbose_name='User'
    )

    _lesson_1 = models.ForeignKey(
        Lesson,
        db_column='lesson_1',
        verbose_name='Lesson 1'
    )

    _lesson_2 = models.ForeignKey(
        Lesson,
        db_column='lesson_2',
        verbose_name='Lesson 2'
    )

    class Meta:
        verbose_name='Challenge'
        verbose_name_plural='Challenges'
        db_table='challenges'