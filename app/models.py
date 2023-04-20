from django.db import models

# Create your models here.

class Topic(models.Model):
    Topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.Topic_name

class Webpage(models.Model):
    Topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Url=models.URLField()
    Email=models.EmailField()

    def __str__(self):
        return self.Name

class AccessRecord(models.Model):
    Name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=200)
    date=models.DateField()

    def __str__(self):
        return self.author