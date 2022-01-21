from django.db import models

# Create your models here.
class event_tbl(models.Model):
    name = models.CharField(max_length=30, unique=True)
    desciption = models.TextField()
    poster_link = models.URLField()
    from_dt = models.DateTimeField()
    to_dt = models.DateTimeField()
    deadline = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=40)
    
    def __str__(self) :
        return self.name

class participant_tbl(models.Model):
    name = models.CharField(max_length=30)
    contact = models.BigIntegerField()
    email = models.EmailField()
    event_name = models.CharField(max_length=30)
    reg_type = models.CharField(max_length=15)
    people = models.IntegerField()
    
    def __str__(self) :
        return self.name
