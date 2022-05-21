from django.db import models
class Job(models.Model):
    jobtitle=models.CharField(max_length=50)
    jobdiscription=models.CharField(max_length=50)

class Candidate(models.Model):
    email= models.CharField(max_length=50)
    jobid = models.CharField(max_length=50)
    applydate = models.CharField(max_length=50)
    cname = models.CharField(max_length=50)


class Registration(models.Model):
    email =models.CharField(max_length=100)
    password =models.CharField(max_length=100)
    mobileno =models.CharField(max_length=100)
    technology =models.CharField(max_length=100)
    candidatetype =models.CharField(max_length=100)
    higherquli =models.CharField(max_length=100)

class  Fupload(models.Model):
    filepath = models.CharField(max_length=100)


class  portpho(models.Model):
    filepath = models.CharField(max_length=100)
    filetype = models.CharField(max_length=100)

# Create your models here.
