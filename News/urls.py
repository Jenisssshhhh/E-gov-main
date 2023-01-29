from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    #path('card',views.card,name='card'),
    path('all_news',views.all_news,name='all_news'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('all_categories',views.all_categories,name='all_categories'),
    path('category/<int:id>',views.category,name='category')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
