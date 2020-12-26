from django.urls import path
from .views import *
from .decorators import check_recaptcha
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('vidpravka_email/', check_recaptcha(vidpravka_email), name='vidpravka_email'),
    # path('', index, name='home'), # приклад з функцією
    path('', HomeNews.as_view(), name='home'),  # приклад з класом #cache_page(30)(
    path('zag/', zag),
    # path('category/<int:category_id>/', get_category, name='category'),# приклад з функцією
    path('category/<int:category_id>/',NewsByCategory.as_view(), name='category'), # cache_page(60 * 5)()
    # приклад з класом
    # path('news/<int:news_id>/', view_news, name='view_news'),# приклад з функцією
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),  # приклад з класом #cache_page(60)()
    # path('news/offer_news/', offer_news, name='offer_news'),# приклад з функцією
    path('news/offer_news/', OfferNews.as_view(), name='offer_news'),  # приклад з класом
]
