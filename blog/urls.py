from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('admin/', admin.site.urls),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
]