from django.urls import path
from . import views

urlpatterns = [
    path('', views.comments, name='comments'),
    path('check-spam', views.check_spam, name='check_spam'),
    path('comments/<int:pk>/', views.delete_comment, name='delete-comment')
]