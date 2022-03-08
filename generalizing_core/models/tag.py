from django.db import models

class Tag(models.Model):
    
    tag = models.CharField(
        primary_key=True,
        verbose_name='Tags',
        max_length=50
    )

    class Meta:
        verbose_name='Tag'
        verbose_name_plural='Tags'
        db_table='tags'