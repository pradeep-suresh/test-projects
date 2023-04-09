from django.db import models

# Create your models here.

class DividendHistory(models.Model):
    stock_symbol     = models.CharField(primary_key=True, blank=False, max_length=10)
    adj_dividend     = models.DecimalField(max_digits = 10, decimal_places=3, blank=False)
    dividend         = models.DecimalField(max_digits = 10, decimal_places=3, blank=False)
    record_date      = models.DateField() 
    payment_date     = models.DateField()
    declaration_date = models.DateField()
