from django.db import models

from generalizing_core.models.user import User
from generalizing_core.models.lesson import Lesson
from generalizing_core.models.mixins.identity_mixin import IdentityMixin

class Challenge(IdentityMixin):

    creation_date = models.DateTimeField(
        verbose_name='Creation Date',
        auto_now_add=True
    )

    lesson_1 = models.ForeignKey(
        Lesson,
        verbose_name='Lesson 1',
        on_delete=models.PROTECT,
        related_name='lesson_1'
    )

    lesson_2 = models.ForeignKey(
        Lesson,
        verbose_name='Lesson 2',
        on_delete=models.PROTECT,
        related_name='lesson_2'
    )

    class Meta:
        verbose_name='Challenge'
        verbose_name_plural='Challenges'
        db_table='challenges'