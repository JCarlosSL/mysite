from django.db import models
from django.utils import timezone

# Create your models here.
class Post1(models.Model):
    post = models.ForeignKey('Post', on_delete = models.CASCADE, default=None)
    author = models.ForeignKey('auth.User',on_delete = models.CASCADE)
    title = models.CharField(max_length=200,null=True,blank=True,default="Setup")
    limite_a = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    limite_b = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    imagen=models.ImageField(upload_to='images/',null=True,blank=True)
    histogram = models.ImageField(upload_to='images/',null=True)
    result = models.ImageField(upload_to='images/',null=True)
    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete = models.CASCADE)
    title = models.CharField(max_length=200,default="Imagen Original")
    imagen = models.ImageField(upload_to='images/',null=True,blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


