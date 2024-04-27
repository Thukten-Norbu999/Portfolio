from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone, timesince

import uuid
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extrafields):
        if not username:
            raise ValueError(("Username must be set"))
        if not email:
            raise ValueError(("Email must be set"))
        if not password:
            raise ValueError(("Password must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extrafields)
        user.set_password(password)
        user.save()
    def create_superuser(self, username, email, password, **extrafields):
        pass


class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    first_name = models.CharField(max_length=150, verbose_name="First Name", blank=False)
    last_name = models.CharField(max_length=150, verbose_name="Last Name")
    username = models.CharField(max_length=200, unique=True, verbose_name='Username')
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]

    objects = CustomUserManager()

    create_at = models.DateTimeField(auto_now_add=timezone.get_current_timezone)
    last_login = models.DateTimeField(auto_now_add=timezone.get_current_timezone)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
