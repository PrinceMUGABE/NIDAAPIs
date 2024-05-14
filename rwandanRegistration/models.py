from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
]

STATUS_CHOICES = [
    ('active', 'Active'),
    ('non_active', 'Non-Active')
]

MARITAL_STATUS_CHOICES = [
    ('single', 'Single'),
    ('married', 'Married'),
    ('widowed', 'Widowed'),
    ('divorced', 'Divorced'),
    ('separated', 'Separated')
]

class Rwandan(models.Model):
    identity_No = models.CharField(
        max_length=16,
        unique=True,
        validators=[
            RegexValidator(
                r'^1\d{15}$',
                message='Identity No. must be 16 digits starting with 1'
            )
        ]
    )
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=100)
    father_names = models.CharField(max_length=200)
    mother_names = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)