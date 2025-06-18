from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


from .views import home, about, contact, detail_artikel
from .autentifikasi import akun_login, akun_register,user_logout
from berita.api import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('artikel/<slug:slug>', detail_artikel, name="detail_artikel"),
    
    path('dashboard/', include("berita.urls")),
    path('api/author/list', api_author_list),
    path('api/kategori/list', api_kategori_list),
    path('api/artikel/detail/<int:id_artikel>', api_artikel_detail),
    path('api/kategori/detail/<int:id_kategori>', api_kategori_detail),
    path('api/artikel/list', api_artikel_list),
    path('autentifikasi/akun_login', akun_login, name="akun_login"),
    path('autentifikasi/akun_register', akun_register, name="akun_register"),
    path('autentifikasi/login', user_logout, name="user_logout"),
    path('api-auth/', include('rest_framework.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)