from django.db import models

class Type(models.TextChoices):
    COULD_BENEFIT_FROM = 'Could Benefit From'
    COULD_SOLVE = 'Could Solve'
    COULD_COMBINE_TO_CREATE = 'Could Combine To Create'
    COULD_CONTRAST_TO_CREATE = 'Could Contrast To Create'
    COULD_CAUSE_BE_A_CAUSE = 'Could Be A Cause'