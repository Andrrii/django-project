from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    save_on_top = True
    list_display = (
    'id', 'author', 'title', 'content', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo', 'views')
    list_display_links = ("title",)
    search_fields = ('title', 'content', 'created_at')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category', 'author', 'tag')
    fields = ('title', 'slug', 'content', 'photo', 'get_photo', 'author', 'category', 'tag', 'created_at', 'updated_at',
              'is_published', 'views')
    readonly_fields = ('get_photo', 'updated_at',
                       'views', 'created_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src = "{obj.photo.url}" width = "100">')
        else:
            return 'Нема фото  '

    #save_as = True #Зберігає як новий об'єкт
    get_photo.short_description = 'downloaded photo or Image'
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ("title",)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ("title",)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Tag, TagAdmin)
