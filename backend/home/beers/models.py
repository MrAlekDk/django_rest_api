from django.db import models


class Beer(models.Model):
    name = models.CharField(max_length=25)
    beer_type = models.CharField(max_length=25)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=44.44)


    @property
    def sale_price(self):
        return '%.2f' %(float(self.price) * 0.8)

     
