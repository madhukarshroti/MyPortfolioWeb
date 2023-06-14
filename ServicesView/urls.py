from django.urls import path
from ServicesView import views
urlpatterns = [
    path('',views.index,name='index')
]
