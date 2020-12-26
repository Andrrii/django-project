from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from django import forms
from .models import News, Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget
class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'

class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    save_on_top = True
    list_display = ('id', 'title', 'content', 'category','created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ("title",)
    search_fields = ('title', 'content', 'created_at')
    list_editable = ('is_published',)
    list_filter = ('is_published','category')
    fields = ('title', 'content', 'photo', 'get_photo','category','created_at', 'updated_at',
              'is_published','views')
    readonly_fields = ('get_photo', 'updated_at',
              'views','created_at')
    def get_photo(self,obj):
        if obj.photo:
            return mark_safe(f'<img src = "{obj.photo.url}" width = "100">')
        else:
            return 'Нема фото  '
    get_photo.short_description = 'downloaded photo or Image'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ("title",)
    search_fields = ('title', )


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)


