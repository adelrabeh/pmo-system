from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    full_name_ar = models.CharField(max_length=200, blank=True)
    job_title_ar = models.CharField(max_length=200, blank=True)
    department_name = models.CharField(max_length=200, blank=True)
    class Meta:
        db_table = "users"
