from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager

# Create your models here.

status_list = (
    ('user', 'Foydalanuvchi'),
    ('editor', 'Tahrirlovchi')
)



class Role(models.Model):
	name = models.CharField("Nomi", max_length=120)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField("Ismi", max_length=100)
    last_name = models.CharField("Familyasi", max_length=100)
    email = models.EmailField('Email', max_length=254, unique=True)
    status = models.CharField('Status', max_length=7,
                              choices=status_list, default='user')
    job_title = models.CharField("Kasbi", max_length=120)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name="Role", null=True, blank=True)
    organization = models.CharField("Tashkilot", max_length=120)
    phone_number = models.CharField("Telefon", max_length=20)
    address = models.CharField("Manzil", max_length=120)

    is_staff = models.BooleanField('is staff', default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(
        'Updated profile', auto_now=True, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    class Meta:

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.first_name + ' ' + self.last_name