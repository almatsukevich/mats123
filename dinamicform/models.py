try:
    from django.db.models import JSONField
except ImportError:
    from django.contrib.postgres.fields import JSONField

#from django.contrib.postgres.fields import JSONField
from django.db import models

class InputModel(models.Model):
    field = models.CharField(max_length=30)
    data = JSONField()

    def __str__(self):
        return self.data,self.field
