import json

#from captcha.helpers import captcha_image_url
#from captcha.models import CaptchaStore
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm# CaptchaTestModelForm
# Create your views here.
from django.http import HttpResponse
from .models import News, Category
from django.views.generic import ListView, DetailView, CreateView
from .utils import MyTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout
from django.core.mail import send_mass_mail,send_mail
# def countb():
#    news = News.objects.order_by('-created_at')
#  countb = 0

# for item in news:
#   if item.is_published:
#      countb += 1
# return countb
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user) #авторизація зразу
            messages.success(request, 'Ура !!! Реєстрація пройшла успішно')
            return redirect('home')
        else:
            messages.error(request, 'Упс ): Щось пішло не так  ')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Упс ): Щось пішло не так  ')
    else:
        form = UserLoginForm()

    return render(request, 'news/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('home')

class HomeNews(ListView):
    model = News
    context_object_name = 'news'
    #  countb()
    extra_context = {'title': 'List of news'}  # для статичних даних
    # 'countb': countb,

    paginate_by = 5  # Скіль на одній сторінці дописів

    # для динамічних даних треба функцію
    # def get_context_data(self, *, object_list=None, **kwargs):
    #   content = super(HomeNews, self).get_context_data(**kwargs)
    #   content['title'] = 'List of news'fff...
    def get_queryset(self):  # Сортування
        sort = News.objects.order_by('-created_at')
        return sort.filter(is_published=True).select_related('category')


class NewsByCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False  # Якшо нема категорії то показувати 404 помилку замість 500х
    paginate_by = 5

    def get_queryset(self):  # Сортування
        test = News.objects.order_by('-created_at')
        return test.filter(category_id=self.kwargs['category_id'], is_published=True, ).select_related('category')

    # countb()
    extra_context = {'title': 'List of news'}  # для статичних даних

    # 'countb': countb,
    def get_context_data(self, *, object_list=None, **kwargs):
        content = super(NewsByCategory, self).get_context_data(**kwargs)
        content['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return content


class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    template_name = 'news/detail_view_news.html'
    context_object_name = 'news_item'


class OfferNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/offer_news.html'
    success_url = reverse_lazy('home')  # redirect
    # Якшо користувач не авторизований то ми перенаправляєм його на задану адресу
    login_url = '/admin/'
    #  або визиваєм помилку 403
    # raise_exception = True

def vidpravka_email(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid() and  request.recaptcha_is_valid:
            mail = send_mail(form.cleaned_data['subject'],form.cleaned_data['content'],
                      'be_infinity@ukr.net',['butsaandrii@gmail.com'],fail_silently=False)
            if mail:
                messages.success(request, 'Ура !!! Email відправленний')
                return redirect('vidpravka_email')
            else:
                messages.error(request,'Помилка відправки')
        else:
            messages.error(request, 'Упс ): Щось пішло не так  ')
    else:
        form = ContactForm()


    return render(request, 'news/vidpravka_email.html', {'form': form,})

# def index(request):
#   news = News.objects.order_by('-created_at')
#   countb()

#  context = {'news': news,
#            'title': 'List of news',
#            'countb':countb
#          }

#  return render(request, 'news/index.html', context=context)


def zag(request):
    print(request)
    return HttpResponse('zagolovok')

# def get_category(request, category_id):
#   news = News.objects.filter(category_id=category_id)
#
#   countb()
#
#   category = Category.objects.get(pk=category_id)
#  return render(request, 'news/category.html', {'news': news, 'category': category,'countb':countb, }
#               )


# def view_news(request, news_id):
#    news_item = get_object_or_404(News, pk=news_id)
#    return render(request, 'news/detail_view_news.html', {'news_item': news_item, })


# def offer_news(request):
# if request.method == 'POST':
# form = NewsForm(request.POST)
# if form.is_valid():
# news = News.objects.create(**form.cleaned_data)
#    news = form.save()
#   return redirect('home')
# else:
#   form = NewsForm()
# return render(request, 'news/offer_news.html', {'form': form, })
