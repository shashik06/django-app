from django.db import models

# Create your models here.
class other(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    slug = models.SlugField(default="", null=False)
    date = models.DateField()
    tags = models.CharField(max_length=50)
    image = models.FileField(upload_to="media/",max_length=250,null=True,default=None)