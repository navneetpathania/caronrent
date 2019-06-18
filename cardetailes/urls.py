from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index),
    path('add',views.addcars),
    path('delete/<id>',views.deletecars),
    path('edit/<id>',views.editcars),
    path('upload/',views.upload)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)