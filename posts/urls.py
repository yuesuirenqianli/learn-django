from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('create/', views.create, name='create'),
    path('user/<int:by_id>', views.user, name='user'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('comment/<int:id>', views.comment, name='comment')
]
