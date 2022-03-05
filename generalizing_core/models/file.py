from django.db import models
from generalizing_bo.settings import DEFAULT_FILE_STORAGE
from generalizing_core.models.lesson import Lesson
from generalizing_core.models.relation import Relation
from generalizing_core.models.mixins.identity_mixin import IdentityMixin


class LessonFile(IdentityMixin):

    lesson = models.ForeignKey(
        Lesson,
        db_column='lesson',
        verbose_name='Lesson',
        on_delete=models.CASCADE
    )

    file = models.FileField(
        verbose_name='File'
    )

class RelationFile(IdentityMixin):

    relation = models.ForeignKey(
        Relation,
        db_column='relation',
        verbose_name='Relation',
        on_delete=models.CASCADE
    )

    file = models.FileField(
        verbose_name='File'
    )