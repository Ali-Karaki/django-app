from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counterGET', views.counterGET, name='counter'),
    path('counterPOST', views.counterPOST, name='counter')
]