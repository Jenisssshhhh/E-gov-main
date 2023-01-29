from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import card


CHOICES = [
    ('Chitwan', 'Chitwan'), ('Kathmandu', 'Kathmandu'),
    ('Bhaktapur', 'Bhaktapur'), ('Lalitpur', 'Lalitpur'), ]
gen = [('Male', 'Male'), ('Female', 'Female'),
       ('Others', 'Others'), ]
stat = [('Married', 'Married'), ('Single', 'Single'),
        ('Divorce', 'Divorce'), ]
Edu_level = [('Uneducated', 'Uneducated'), ('Slc', 'Slc'), ('Plus_2', 'Plus 2'),
             ('Bacehlors', 'Bacehlors'), ('Masters', 'Masters'), ('PHDs', 'PHDs'), ]
prof = [('Others', 'Others'), ('Service', 'Service'), ('Doctor', 'Doctor'), ('Framer', 'Framer'),
        ('Teacher', 'Teacher'), ('Social', 'Social Worker'), ('Lawyer', 'Lawyer'), ('Businessman', 'Businessman')]
CasteChoice = [('Others', 'Others'), ('Chettri', 'Chettri'), ('Brahmin', 'Brahmin'), ('Newar', 'Newar'),
               ('Thakuri', 'Thakuri')]
Reli = [('Others', 'Others'), ('Hindu', 'Hindu'), ('Buddha', 'Buddha'), ('Islam', 'Islam'),
        ('Christian', 'Christian')]
# Create your models here.


class FilesAdmin(models.Model):
    adminupload = models.FileField(upload_to='uploads/')
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Files Uploads'

    def __str__(self):
        return self.title


class Idcard(models.Model):
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    birthplace = models.CharField(choices=CHOICES, max_length=50)
    citizenship_no = models.IntegerField()
    issue_zone = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    caste = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Id Cards'

    def __str__(self):
        return self.firstname


class Gallery(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploads', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return self.title
