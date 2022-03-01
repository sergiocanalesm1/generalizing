from django.db import models

from generalizing_core.models.relation import Relation
from generalizing_core.models.mixins.identity_mixin import IdentityMixin


class RelationFile(IdentityMixin):

    _relation = models.ForeignKey(
        Relation,
        db_column='relation',
        verbose_name='Relation'
    )

    _file = models.FileField(
         upload_to='relation/',
        db_column='file',
        verbose_name='File'
    )