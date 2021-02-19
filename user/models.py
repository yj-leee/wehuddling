from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email          = models.EmailField(max_length=100, unique=True)
    GENDER_CHOICES = (('M', '남성'),('F', '여성'))
    gender         = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    address        = models.CharField(max_length=100, null=True)
    name           = models.CharField(max_length=30)
    phone_number   = models.CharField(max_length=20)
    update_at      = models.DateTimeField(auto_now=True)
    is_deleted     = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'




