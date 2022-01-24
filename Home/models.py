from django.db import models
from . widgets import DateInput
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
# Create your models here.

#Date Validator
def date_valid(value):
    today=datetime.date.today()
    # print(value.day)
    # print(today.day)
    # print(value.month)
    # print(today.month)
    # print(value.year)
    # print(today.year)
    if value.year != today.year or value.month != today.month or value.day != today.day:
        raise ValidationError("Attendance can only be for today's date!")
    # else:
    #     print("passed")

class student(models.Model):
    name=models.CharField(max_length=30)
    roll=models.IntegerField()

    def __str__(self):
        return f"{self.name} and {self.roll}"

    class Meta:
        ordering = ['roll']


class subject(models.Model):
    sub = models.CharField(max_length=64)
    def __str__(self):
        return self.sub

class time(models.Model):
    sub = models.ForeignKey(subject,on_delete=models.CASCADE)
    time = models.CharField(max_length=64)
    def __str__(self):
        return self.time
    

class attendance(models.Model):
    name = models.CharField(max_length=64,blank=False)
    roll = models.IntegerField(blank=False)
    date = models.DateField(auto_now_add=False,auto_now=False,blank=False,validators=[date_valid])
    sub = models.ForeignKey(subject,on_delete=models.SET_NULL,blank=True,null=True)
    # time = models.ForeignKey(time,on_delete=models.SET_NULL,blank=True,null=True)
    """ def save(self, *args, **kwargs):
        if self.date is not datetime.date.today():
            raise ValidationError("The date has to be today!")
        super(Event, self).save(*args, **kwargs) """

    class Meta:
        ordering = ["-date","roll"]


class attendanceclass(models.Model):
    date=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    status=models.IntegerField(default=0)

    #class Meta:
        #unique_together = ('date','status')

class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)
    def get_email(self):
        return self.email

class user_type(models.Model):
    is_principle = models.BooleanField(default=False)
    is_hod = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.is_student == True:
            return User.get_email(self.user) + " - is_student"
        elif self.is_teacher == True:
            return User.get_email(self.user) + " - is_teacher"
        elif self.is_hod == True:
            return User.get_email(self.user) + " - is_hod"
        else:
            return User.get_email(self.user) + " - is_principle"