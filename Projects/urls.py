from django.urls import path
from Projects import views
urlpatterns = [
    path('',views.index,name='index')
]
