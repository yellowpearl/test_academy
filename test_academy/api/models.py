from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    unit = models.CharField(max_length=255)
    price = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f'{self.name}: {self.amount} ({self.date})'
