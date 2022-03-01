from enum import unique
import imp
import uuid
from django.db import models

class IdentityMixin(models.Model):

    _id = models.AutoField(
        db_column='id',
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID'
    )

    _uuid = models.UUIDField(
        db_column='uuid',
        unique=True,
        default=uuid.uuid4,
        editable=False
    )

    def get_id(self):
        return self._id
    
    def get_uuid(self):
        return self._uuid
    
    class Meta:
        abstract=True