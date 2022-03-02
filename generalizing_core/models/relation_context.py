from django.db import models

from generalizing_core.models.relation import Relation
from generalizing_core.models.mixins.identity_mixin import IdentityMixin

class RelationContext(IdentityMixin):

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

    #TODO business rule to accept below 50
    past_week_sleep_hrs = models.IntegerField(
        verbose_name='Past Week Sleep Hours',
        blank=True,
        null=True,
    )

    #TODO business rule to accept from 1-5
    mood = models.IntegerField(
        verbose_name='Mood',
        blank=True,
        null=True,
    )

    #TODO business rule to accept from 1-5
    relaxation = models.IntegerField(
        verbose_name='Relaxation',
        blank=True,
        null=True,
    )

    #TODO business rule to accept below 50
    iterations = models.IntegerField(
        verbose_name='Iterations',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name='Relation Context'
        verbose_name_plural='Relations Contexts'
        db_table='relations_contexts'