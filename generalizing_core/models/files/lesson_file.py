from django.core.files.storage import FileSystemStorage
from django.db import models

from generalizing_core.models.lesson import Lesson
from generalizing_core.models.mixins.identity_mixin import IdentityMixin

fs = FileSystemStorage(location='/media/lessons') #TODO donde se guarda estooooo

class LessonFile(IdentityMixin):

    _lesson = models.ForeignKey(
        Lesson,
        db_column='lesson',
        verbose_name='Lesson'
    )

    _file = models.FileField(
        storage=fs,
        db_column='file',
        verbose_name='File'
    )