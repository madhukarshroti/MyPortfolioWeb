from django.urls import path
from Certificates import views
urlpatterns = [
    path('',views.index,name='index')
]
