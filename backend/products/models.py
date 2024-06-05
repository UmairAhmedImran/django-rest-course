from django.db import models

# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=12, default=99.9, decimal_places=2)

    @property
    def sales_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return None
