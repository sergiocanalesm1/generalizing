from django.db  import models

class DatesMixin(models.Model):
    _creation_date = models.DateTimeField(
        db_column='creation_date',
        verbose_name='Creation Date',
        auto_now_add=True
    )

    def get_creation_date(self):
        return self._creation_date