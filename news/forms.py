from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
#from captcha.fields import CaptchaField,CaptchaTextInput

# додавання форм на сайт

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'  перший спосіб (не дуже)
        fields = ['title', 'content', 'photo', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),

        }

    def clean_title(self):
        title = self.cleaned_data['title']
        title = list(title)
        title[0] = title[0].upper()
        title = ''.join(title)
        if re.match(r'\d', title):
            raise ValidationError('Назва не починається з цифри!!!')
        return title


# Регістрація і логін

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя:', widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label='Имя :', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Фамилия:', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля:', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя:', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={'class':'form-control'}))

class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class':'form-control','rows':5}))
    #captcha =CaptchaField()

#class CaptchaTestModelForm(forms.Form):
#    captcha = CaptchaField()
