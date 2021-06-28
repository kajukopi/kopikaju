from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list_blog, name='list_blog'),
    path('<id>', views.detail_blog, name='detail_blog'),
    path('(<id>/update', views.update_blog, name='update_blog'),
    path('(<id>/delete', views.delete_blog, name='delete_blog'),
]

