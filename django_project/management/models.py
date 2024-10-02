from django.db import models # type: ignore

class userdata(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    login_image=models.ImageField(upload_to="Doctor/")
    def __str__(self):
        return self.email


class Doctorinfo(models.Model):
    Dc_img=models.ImageField(upload_to='Doctor/')
    Dc_name=models.CharField(max_length=50)
    Dc_sepc=models.CharField(max_length=50)
    def __str__(self):
        return self.Dc_name


class Patientdetails(models.Model):
    dc_name=models.CharField(max_length=50)
    patname=models.CharField(max_length=50)
    age=models.IntegerField(null=False, blank=False)
    date=models.DateField(null=False, blank=False)
    problem=models.CharField(max_length=50)
    def __str__(self):
        return self.patname
    
class Doctorlogin(models.Model):
    username=models.CharField(max_length=50)
    identity=models.CharField(max_length=50)
    def __str__(self):
        return self.username
    
