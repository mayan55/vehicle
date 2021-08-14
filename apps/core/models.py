from django.db import models


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False, blank=True)
    is_active = models.BooleanField(default=True, blank=True)

    class Meta:
        abstract = True