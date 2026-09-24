from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование товара", help_text="Введите наименование товара"
    )
    description = models.TextField(verbose_name="Описание товара", help_text="Опишите товар", blank=True, null=True)
    image = models.ImageField(
        upload_to="images/",
        blank=True,
        null=True,
        verbose_name="Изображение товара",
        help_text="Загрузите изображение товара",
    )
    category = models.ForeignKey(
        "Category",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Категория товара",
        help_text="Введите категорию товара",
        related_name="products",
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена", help_text="Введите стоимость товара"
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата последнего изменения")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = ["name"]


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория", help_text="Введите название категории товаров")
    description = models.TextField(
        verbose_name="Описание категории", help_text="Опишите категорию товаров", blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]
