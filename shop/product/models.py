from django.db import models


class Product(models.Model):
    CHOICES = (
        ("in stock", "В наличии"),
        ("on order", "Под заказ"),
        ("receipt expected", "Ожидается поступление"),
        ("not available", "Нет в наличии"),
        ("not produced", "Не производится"),
    )

    name = models.CharField(max_length=255, db_index=True)
    vendor_code = models.IntegerField(db_index=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(max_length=50, choices=CHOICES)
    image = models.ImageField(upload_to="media/images/product")
