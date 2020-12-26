from django.db import models
from django.urls import reverse_lazy


class Post(models.Model):
    title = models.CharField(max_length=155, verbose_name='Заголовок')
    slug = models.SlugField(max_length=155, verbose_name='Url', unique=True)
    author = models.CharField(max_length=35, verbose_name='Автор')
    content = models.TextField(blank=True, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Редаговано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото|Зображення')
    is_published = models.BooleanField(default=False, verbose_name='Чи опобліковувати')
    views = models.IntegerField(default=0, verbose_name='К-сть переглядів')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категорія')
    tag = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('post', kwargs={'slug': self.slug})


    class Meta:
        verbose_name = "Допис"
        verbose_name_plural = "Дописи"
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=155, verbose_name='Назва')
    slug = models.SlugField(max_length=155, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ['title']



class Tag(models.Model):
    title = models.CharField(max_length=55, verbose_name='Назва')
    slug = models.SlugField(max_length=55, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('tag', kwargs={'slug': self.slug})


    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ['title']
