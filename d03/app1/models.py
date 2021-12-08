from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=50)
    roll_no=models.IntegerField()
    city=models.CharField(max_length=30)

    def __str__(self):
        return self.name
