from django.db import models

from generalizing_core.models.relation import Relation
from generalizing_core.models.mixins.identity_mixin import IdentityMixin

class RelationContext(IdentityMixin):

    _place = models.CharField(
        db_column='place',
        verbose_name='Place',
        max_length=240
    )

    _dialogued = models.BooleanField(
        db_column='dialogued',
        verbose_name='Dialogued'
    )

    _daydreamed = models.BooleanField(
        db_column='daydreamed',
        verbose_name='Day Dreamed'
    )

    _past_week_sleep_hrs = models.IntegerField(
        max_length=40,
        db_column='past_week_sleep_hours',
        verbose_name='Past Week Sleep Hours'
    )

    _mood = models.IntegerField(
        max_length=5,
        db_column='mood',
        verbose_name='Mood'
    )

    _relaxation = models.IntegerField(
        max_length=5,
        db_column='relaxation',
        verbose_name='Relaxation'
    )

    _iterations = models.IntegerField(
        max_length=100,
        db_column='iterations',
        verbose_name='Iterations'
    )

    class Meta:
        verbose_name='Relation Context'
        verbose_name_plural='Relations Contexts'
        db_table='relations_contexts'