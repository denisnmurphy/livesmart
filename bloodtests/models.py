from django.db import models

class Test(models.Model):
    name=models.CharField(max_length=100)
    unit=models.CharField(max_length=10)
    code=models.CharField(max_length=4)

    def __str__(self):
        return self.name

class TestResult(models.Model):
    upper = models.IntegerField()
    lower = models.IntegerField()

    def __str__(self):
        return
