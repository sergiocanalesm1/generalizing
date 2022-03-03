from django.db import models
from django.core.files.storage import FileSystemStorage

from generalizing_core.models.mixins.identity_mixin import IdentityMixin
from generalizing_core.models.choices.domain import Domain
from generalizing_core.models.choices.origin import Origin
from generalizing_core.models.tag import Tag
from generalizing_core.models.user import User

fs = FileSystemStorage(location='/media/lessons')

class Lesson(IdentityMixin):

    name = models.CharField(#TODO ponerle más
        max_length=100,
        verbose_name='Name',
    )

    creation_date = models.DateTimeField(
        verbose_name='Creation Date',
        auto_now_add=True
    )

    description = models.TextField(
        verbose_name='Description',
        blank=False,
        null=False
    )

    origin = models.CharField(
        max_length=100,
        verbose_name='Origin',
        choices=Origin.choices
    )

    domain = models.CharField(
        max_length=100,
        verbose_name='Domain',
        blank=True,
        null=True,
        choices=Domain.choices
    )

    tags = models.ManyToManyField(
        Tag,
        verbose_name='Tags',
        blank=True,
    )

    user = models.ForeignKey(
        User,
        verbose_name='User',
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name='Lesson'
        verbose_name_plural='Lessons'
        db_table='lessons'