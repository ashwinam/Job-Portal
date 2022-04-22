from weakref import proxy
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomAccountManager



# ------------------------User Creation--------------------------
# Extending Custom User Model
class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'),max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Types(models.TextChoices):
        EMPLOYEE = "EMPLOYEE", "Employee"
        EMPLOYER = "EMPLOYER", "Employer"

    default_type = Types.EMPLOYEE

    type = models.CharField(_('Types'), max_length=100, choices=Types.choices, default=default_type)

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.default_type
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.email

# model managers for Employee & Employer Tables
class EmployeeManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=NewUser.Types.EMPLOYEE)

class EmployerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=NewUser.Types.EMPLOYER)

# Create a Proxy Model Referrence for Employee & Employer User Types
class Employee(NewUser):
    default_type = NewUser.Types.EMPLOYEE
    objects = EmployeeManager()
    class Meta:
        proxy = True


class Employer(NewUser):
    default_type = NewUser.Types.EMPLOYER
    objects = EmployerManager()
    class Meta:
        proxy = True



# --------------------------------User Profile-------------------------
class EmployerProfile(models.Model):
    employer = models.OneToOneField(Employer, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    phone = models.CharField(max_length=255, validators=[phone_regex], blank = True, null=True)

    def __str__(self) -> str:
        return self.employer.name


# django signal that instantiate the employer profile when it create or update
def create_profile(sender, instance, created, **kwargs):
    if created:
        EmployerProfile.objects.create(employer=instance)
        print(sender, instance, created)
        print("profile created!")

post_save.connect(create_profile, sender=Employer)

def update_profile(sender, instance, created, **kwargs):
    try:
        if created == False:
            instance.employerprofile.save()
            print("profile updated!")
    except AttributeError:
        EmployerProfile.objects.create(employer=instance)

post_save.connect(update_profile, sender=Employer)



class EmployeeProfile(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    phone = models.CharField(max_length=255, validators=[phone_regex], blank = True, null=True)
    age = models.SmallIntegerField(null=True, blank=True)
    
    class Gender(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"
        OTHER = "OTHER", "Other"
    gender = models.CharField(_("Gender"), max_length=100, choices=Gender.choices, null=True, blank=True)

    def __str__(self) -> str:
        return self.employee.name

# django signal that instantiate the employe profile when it create or update
def create_profile(sender, instance, created, **kwargs):
    if created:
        EmployeeProfile.objects.create(employee=instance)
        print(sender, instance, created)
        print("profile created!")

post_save.connect(create_profile, sender=Employee)

def update_profile(sender, instance, created, **kwargs):
    try:
        if created == False:
            instance.employeeprofile.save()
            print("profile updated!")
    except AttributeError:
        EmployeeProfile.objects.create(employee=instance)

post_save.connect(update_profile, sender=Employee)
