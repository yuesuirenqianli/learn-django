from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('create/', views.create, name='create'),
    path('user/<int:by_id>', views.user, name='user'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('comment/<int:id>', views.comment, name='comment'),
    path('get_captcha', views.get_captcha, name='get_captcha')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
