from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to="images/jobs")
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title
