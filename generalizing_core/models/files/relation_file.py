from django.core.files.storage import FileSystemStorage
from django.db import models

from generalizing_core.models.relation import Relation
from generalizing_core.models.mixins.identity_mixin import IdentityMixin

fs = FileSystemStorage(location='/media/relations') #TODO donde se guarda estooooo

class RelationFile(IdentityMixin):

    _relation = models.ForeignKey(
        Relation,
        db_column='relation',
        verbose_name='Relation'
    )

    _file = models.FileField(
        storage=fs,
        db_column='file',
        verbose_name='File'
    )