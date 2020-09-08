from django.db import models

# Create your models here.
class Resident(models.Model):
    rid = models.CharField(max_length=20)
    rname = models.CharField(max_length=20)
    remail = models.EmailField()
    rpassword = models.CharField(max_length=20)
    rcontact = models.CharField(max_length=10)
    class Meta:
        db_table = "resident"