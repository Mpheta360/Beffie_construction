from django.urls import path
from django.conf.urls import include, url
from users.views import dashboard
from . import views

urlpatterns = [
    path('', views.home),
    path('services', views.service),
    path('products', views.details),
    path('about', views.about),
    path('contact', views.contact),
    path('contact', views.product),
    path('login', views.login),
    path('logout', views.out),
    path('sign-up', views.lowani),
    path('blocks', views.block),
    path('slabs', views.slab),
    path('pavers', views.paver),
    path('our-gallery', views.gallery),
    path('why-choose-us', views.choose),
    path('loved-products', views.lovedproducts),
    path('dashboard', views.dashboard),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)
