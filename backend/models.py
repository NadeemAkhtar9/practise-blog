from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date =models.DateTimeField()
    link = models.URLField()

def __str__(self):
    return self.title
    