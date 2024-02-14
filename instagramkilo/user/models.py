"""_summary_ Modle class
    """
from django.db import models
from django.contrib.auth.models import AbstractUser


# Register your models here.
class User(AbstractUser):

    """imported user"""

    is_email_verified = models.BooleanField(default=False)
