from django.contrib.auth.base_user import BaseUserManager
from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import DefaultAccountAdapter

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):


        print(email)
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        superuser = self.create_user(
            email=email,
            password=password,
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser
