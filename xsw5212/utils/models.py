from django.db import models


class BaseModel(models.Model):
    active = models.BooleanField(default=True)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)

    class Meta:
        abstract = True
