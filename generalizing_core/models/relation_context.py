from django.db import models

from generalizing_core.models.relation import Relation
from generalizing_core.models.mixins.identity_mixin import IdentityMixin

class RelationContext(IdentityMixin):

    description = models.TextField(
        verbose_name='Description',
        blank=True,
        null=True
    )

    place = models.CharField(
        verbose_name='Place',
        max_length=240,
        blank=True,
        null=True,
    )

    dialogued = models.BooleanField(
        verbose_name='Dialogued',
        blank=True,
        null=True,
    )

    daydreamed = models.BooleanField(
        verbose_name='Day Dreamed',
        blank=True,
        null=True,
    )

    past_week_sleep_hrs = models.CharField(
        max_length=50,
        verbose_name='Past Week Sleep Hours',
        null=True,
        blank=True,
    )

    mood = models.CharField(
        max_length=50,
        verbose_name='Mood',
        null=True,
        blank=True,
    )

    relaxation = models.CharField(
        max_length=50,
        verbose_name='Relaxation',
        null=True,
        blank=True,
    )


    iterations = models.IntegerField(
        verbose_name='Iterations',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name='Relation Context'
        verbose_name_plural='Relations Contexts'
        db_table='relations_contexts'