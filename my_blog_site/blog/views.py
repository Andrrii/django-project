from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import *
from django.db.models import F


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Be_Infinity'
        return context


class PostByCategory(ListView):
    template_name = 'blog/news_by_category.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False  # Щоб була помилка 404

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class GetPost(DetailView):  # Формує силки на post
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1  # правильно рахуєм views
        self.object.save()
        self.object.refresh_from_db()
        return context


class PostByTag(ListView):
    template_name = 'blog/news_by_category.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False  # Щоб була помилка 404

    def get_queryset(self):
        return Post.objects.filter(tag__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Дописи по тегу : ' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context


class Search(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self): #search
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context

