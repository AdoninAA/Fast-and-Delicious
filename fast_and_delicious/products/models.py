from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import GenericTaggedItemBase, TagBase


class ItemTag(TagBase):
    image = models.ImageField(
        upload_to='categories/',
        verbose_name='Изображение',
        blank=True
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
        )

    class Meta:
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")


class TaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(
        ItemTag,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name='Категория',
    )


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.CharField(
        unique=True,
        max_length=50,
    )
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
        upload_to='items/', #Добавить источник
        blank=True,
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name='Доступно',
    )
    tags = TaggableManager(through=TaggedItem, related_name="tagged_items", verbose_name='Категории', )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-price']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

