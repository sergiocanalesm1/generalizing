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

    #TODO business rule to accept below 50
    _past_week_sleep_hrs = models.IntegerField(
        db_column='past_week_sleep_hours',
        verbose_name='Past Week Sleep Hours'
    )

    #TODO business rule to accept from 1-5
    _mood = models.IntegerField(
        db_column='mood',
        verbose_name='Mood'
    )

    #TODO business rule to accept from 1-5
    _relaxation = models.IntegerField(
        db_column='relaxation',
        verbose_name='Relaxation'
    )

    #TODO business rule to accept below 50
    _iterations = models.IntegerField(
        db_column='iterations',
        verbose_name='Iterations'
    )

    class Meta:
        verbose_name='Relation Context'
        verbose_name_plural='Relations Contexts'
        db_table='relations_contexts'