from django.db import models

# Create your models here.

# This models will represented as Tables in databases

# The following model defines the table named "Topic" in the database
# with the column named as 'topicName' of type CharField (like VarChar in SQL)
# with the constraints
# the __str__ finction is a python function that returns the string representation
# of the fied defined inside it.
class Topic(models.Model):
    topicName = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.topicName

class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecords(models.Model):
    name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class Users(models.Model):
    userName = models.CharField(max_length=264,unique=True)
    email = models.EmailField(unique=True)
    #password = models.CharField()

    def __str__(self):
        return str(self.userName)
