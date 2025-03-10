from django.db import models


class Item(models.Model):
    CURRENCY_CHOICES = [
        ("usd", "USD"),
        ("eur", "EUR"),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="usd")

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField(help_text="Discount amount in cents")

    def __str__(self):
        return f"{self.amount / 100}$"

class Tax(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.FloatField(help_text="Tax percentage (e.g. 10 for 10%)")

    def __str__(self):
        return f"{self.percentage}%"


class Order(models.Model):
    items = models.ManyToManyField('Item')
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True, blank=True)

    def total_price(self):
        return sum(item.price for item in self.items.all())

    def __str__(self):
        return f'Order {self.id} - {self.items.count()} items.'
