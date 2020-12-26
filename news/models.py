from django.db import models
from django.urls import reverse_lazy


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=145)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse_lazy('view_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новина"
        verbose_name_plural = "Новини"


class Category(models.Model):
    title = models.CharField(max_length=75, db_index=True)

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ['id', ]

    def __str__(self):
        return self.title
