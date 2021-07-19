from django.db import models

# Create your models here.
class Xl_store(models.Model):
    num=models.IntegerField()
    userid=models.CharField(max_length=30)
    class Meta:
        db_table='Xl_store'