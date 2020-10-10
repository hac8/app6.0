from django.db import models


class Groups(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Students(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    second_last_name = models.CharField(max_length=50)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
