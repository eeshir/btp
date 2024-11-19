from django.db import models

# Create your models here.
from django.db import models
from django.forms import forms


class NewModel(models.Model):
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    q9 = models.IntegerField()
    q10 = models.IntegerField()
    q11 = models.IntegerField()
    q12 = models.IntegerField()
    q13 = models.IntegerField()
    q14 = models.IntegerField()
    q15 = models.IntegerField()
    q16 = models.IntegerField()
    q17 = models.IntegerField()
    q18 = models.IntegerField()
    q19 = models.IntegerField()
    q20 = models.IntegerField()

    class Meta:
        app_label = 'formapp'


# class MyModel(models.Model):
#     q1 = models.IntegerField()
#     q2 = models.IntegerField()
#     q3 = models.IntegerField()
#     q4 = models.IntegerField()
#     q5 = models.IntegerField()
#     q6 = models.IntegerField()
#     q7 = models.IntegerField()
#     q8 = models.IntegerField()
#     q9 = models.IntegerField()
#     q10 = models.IntegerField()
#     q11 = models.IntegerField()
#     q12 = models.IntegerField()
#     q13 = models.IntegerField()
#     q14 = models.IntegerField()
#     q15 = models.IntegerField()
#     q16 = models.IntegerField()
#     q17 = models.IntegerField()
#     q18 = models.IntegerField()
#     q19 = models.IntegerField()
#     q20 = models.IntegerField()
#
#     class Meta:
#         app_label = 'formapp'