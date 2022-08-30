from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self,email, password, **extra_fields):
        if not email:
            raise ValueError("Укажите пожалуйста адресс электронной почты")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,**extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser дожен быть is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser должен быть is_superuser=True.')

        return self._create_user(email,password,**extra_fields)

class User(AbstractUser):

    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=64, verbose_name='Имя получателя', null=True)
    last_name = models.CharField(max_length=64, verbose_name='Фамилия получателя', null=True)
    city = models.CharField(max_length=64, verbose_name='Город', null=True)
    street = models.CharField(max_length=64, verbose_name='Улица', null=True)
    house = models.CharField(max_length=64, verbose_name='№ дома', null=True)
    flat = models.CharField(max_length=64, verbose_name='№ квартиры', null=True)
    phone = models.CharField(max_length=64, verbose_name='Номер для связи', null=True)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'