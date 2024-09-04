from django.db import models

class PollAdmin(models.Model):
    sno = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, verbose_name='Username')
    email = models.EmailField(max_length=100, verbose_name='Email')
    mobile = models.CharField(max_length=100, verbose_name='Mobile', unique=True)
    password = models.CharField(max_length=100, verbose_name='Password')
    confirm_password = models.CharField(max_length=100, verbose_name='Confirm Password', default='')

    def __str__(self):
        return self.username

class EndUser(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    unique_id = models.CharField(max_length=50, verbose_name='Unique ID', unique=True)
    mobile = models.CharField(max_length=15, verbose_name='Mobile Number')

    def __str__(self):
        return self.name  # Display name in admin panel