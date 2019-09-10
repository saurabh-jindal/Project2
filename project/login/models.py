from django.db import models



class Signup(models.Model):
    name = models.CharField(max_length=70)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    def __str__(self):
        return self.name
