from enum import unique
import imp
import uuid
from django.db import models

class IdentityMixin(models.Model):

    id = models.AutoField(
        db_column='id',
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID'
    )

    uuid = models.UUIDField(
        db_column='uuid',
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    
    class Meta:
        abstract=True