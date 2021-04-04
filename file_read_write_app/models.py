from django.db import models

# Create your models here.


class CsvData(models.Model):
    x1=models.TextField()
    x2=models.TextField()
    x3=models.TextField()
    x4=models.TextField()
    x5=models.TextField()
    x6=models.TextField()
    x8=models.TextField()
    x9=models.TextField()

    class Meta:
        db_table = "csv_data"