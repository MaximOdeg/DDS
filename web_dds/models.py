from django.core.exceptions import ValidationError
from django.db import models


class Status(models.Model):
    """Модель статуса"""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Type(models.Model):
    """Модель типа"""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    """Модель категории"""

    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="categories")

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    """Модель подкатегории"""

    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="subcategories"
    )

    def __str__(self):
        return self.name


class Transaction(models.Model):
    """Модель записи движения средств"""

    created_at = models.DateField(auto_now_add=True)
    date = models.DateField(verbose_name="Дата создания записи")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Статус")
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="Тип")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, verbose_name="Подкатегория"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    comment = models.TextField(blank=True, verbose_name="Комментарий")

    def __str__(self):
        amount_in_rub = f"{self.amount:,.2f} ₽"
        return f"{self.date} - {amount_in_rub} - {self.status}"

    def clean(self):
        if self.subcategory.category.type != self.type:
            raise ValidationError("Подкатегория не соответствует выбранному типу.")
