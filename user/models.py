from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
#from items.models import Item

class CustomManager(BaseUserManager):
    def create_user(self, email, user_name, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        return self.create_user(email, user_name, password, **other_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    user_name = models.CharField(max_length=100, unique=True)
    adress = models.CharField(max_length=500)
    card_number = models.CharField(max_length=16)
    birth_day = models.DateField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    

    
    objects = CustomManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']
    
    def __str__(self):
        return self.user_name
    

