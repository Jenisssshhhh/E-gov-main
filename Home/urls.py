from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls  import url
from django.views.static import serve
from Home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('slider', views.slider, name='slider'),
    path('footer', views.footer, name='footer'),
    path('contact_us', views.contact, name='contact_us'),
    path('services', views.services, name='services'),
    path('confirm', views.confirm, name='confirm'),
    path('regis', views.regis, name='regis'),
    path('userregister', views.register, name='userregister'),
    path('login', views.loginpage, name='login'),
    path('logout', views.logoutpage, name='logout'),
    path('loksewa', views.loksewa, name='loksewa'),
    path('marriage', views.marriage, name='marriage'),
    path('birth', views.birth, name='birth'),
    path('gallery', views.gallery, name='gallery'),
    path('downloads', views.downloads, name='downloads'),
    re_path(r'^download/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
]
