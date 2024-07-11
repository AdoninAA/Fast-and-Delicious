from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.CharField(
        unique=True,
        max_length=50,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления', )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Новая цена',
    )
    old_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Старая цена',
        blank=True,
        null=True,
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='items/',  # Добавить источник
        blank=True,
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name='Доступно',
    )
    category = models.ForeignKey(
        Category,
        related_name='Категории',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-price']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
