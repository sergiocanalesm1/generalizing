from django.db import models
from django.core.files.storage import FileSystemStorage

from generalizing_core.models.mixins.identity_mixin import IdentityMixin
from generalizing_core.models.mixins.dates_mixin import DatesMixin
from generalizing_core.models.choices.domain import Domain
from generalizing_core.models.choices.origin import Origin
from generalizing_core.models.tag import Tag
from generalizing_core.models.user import User

fs = FileSystemStorage(location='/media/lessons')

class Lesson(IdentityMixin,DatesMixin):

    _name = models.CharField(
        max_length=100,
        db_column='name',
        verbose_name='Name',
    )

    _description = models.TextField(
        db_column='description',
        verbose_name='Description',
        blank=False,
        null=False
    )

    _origin = models.CharField(
        max_length=100,
        db_column='origin',
        verbose_name='Origin',
        choices=Origin.choices
    )

    _domain = models.CharField(
        max_length=100,
        db_column='domain',
        verbose_name='Domain',
        blank=True,
        null=True,
        choices=Domain.choices
    )

    _tags = models.ManyToManyField(
        Tag,
        db_column='tag',
        verbose_name='Tags',
        blank=True,
    )

    _user = models.ForeignKey(
        User,
        db_column='user',
        verbose_name='User',
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name='Lesson'
        verbose_name_plural='Lessons'
        db_table='lessons'