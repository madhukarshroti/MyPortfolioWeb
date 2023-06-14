from django.contrib import admin
from django.urls import path,include
from MyPortfolio import views
from django.conf.urls.static import static
from django.conf import settings


admin.site.site_header="Madhukar Login Method"
admin.site.site_title="Warning || Madhukar's Panel"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('Message-Handler/', views.MessageHandler.as_view(), name='MessageHandler'),
    path('project-detail/<int:myid>', views.ProjectHandle, name='ProjectHandle'),
    # path('',include('Projects.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
