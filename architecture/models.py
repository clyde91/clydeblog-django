from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Architect(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country,on_delete=models.DO_NOTHING,blank=True, null=True)
    profile = models.ImageField(upload_to='architecture/img_architect', blank=True, null=True)

    def __str__(self):
        return self.name

class Structure(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Architecture(models.Model):
    name = models.CharField(max_length=30)
    build_time = models.CharField(max_length=30, blank=True, null=True)
    architect = models.ForeignKey(Architect, on_delete=models.DO_NOTHING, blank=True, null=True)
    structure = models.ForeignKey(Structure, on_delete=models.DO_NOTHING, blank=True, null=True)
    build_country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

