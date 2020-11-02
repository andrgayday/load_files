from django.db import models


class MyFiles(models.Model):
    my_file = models.FileField()
