from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def get_user(self):
    return self.username + " :" + self.first_name + " " + self.last_name
User.add_to_class("__str__", get_user)

class Account(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.BooleanField(default=False, verbose_name='isMale')
    dateOfBirth = models.DateField(null=False)
    hobby = models.TextField(default='', blank=True)
    avatar = models.ImageField(blank=True)
    coverPhoto = models.ImageField(blank=True)
    def __str__(self):
        title = self.user.__str__() + ': {}'
        return title.format(self.dateOfBirth)