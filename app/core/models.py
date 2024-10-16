"""
database models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """manager for users"""
    """BaseUserManager class provide by Django and we want to use that"""

    def create_user(self, email, password=None, **extra_field):
        """create save and return new user"""
        """extra_field makes it so you can provide keyword arguments such as
            Name as an additional field. Name field will then be atomatically
            created when the user model is created.
        """
        """Ensure users have an email address"""
        if not email:
            raise ValueError('User must have an email address')
        """send it through the normalize_email method before saving first"""
        user = self.model(email=self.normalize_email(email), **extra_field)
        """will take password provided and encrypt the password in the db"""
        user.set_password(password)
        """saves user model to support adding multiple databases if needed"""
        user.save(using=self._db)

        return user
     
    def create_superuser(self, email, password):
        """create and retur a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """user in system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=225)
    is_active = models.BooleanField(default=True)
    """Django admin"""
    is_staff = models.BooleanField(default=False)

    """how you assign a user manager in Django"""
    objects = UserManager()

    USERNAME_FIELD = 'email'
