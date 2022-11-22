from django.db import models


class About(models.Model):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='about/')
    description = models.TextField()

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='service/')
    description = models.TextField()

    def __str__(self):
        return self.title

