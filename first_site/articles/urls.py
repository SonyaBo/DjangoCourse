from django.urls import path
from .views import article, article_comment,article_delete,article_update

urlpatterns = [
    path('', article, name='article'),
    path('comment/', article_comment , name='comment'),
    path('update/', article_delete , name='update'),
    path('delete/', article_update , name='delete'),
]