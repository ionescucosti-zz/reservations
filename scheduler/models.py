from django.db import models


class Rental(models.Model):
    name = models.CharField(max_length=50, primary_key=True)


class Reservations(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    checkin = models.DateField(null=False)
    checkout = models.DateField(null=False)
