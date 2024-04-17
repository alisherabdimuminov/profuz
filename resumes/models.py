from django.db import models


class Resume(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/resumes/", null=True, blank=True)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=50)
    birth_date = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    education = models.CharField(max_length=50)
    mother_lang = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
