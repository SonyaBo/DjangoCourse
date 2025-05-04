from django.shortcuts import render, path
from views import topics, subscribe, unsubscribe, topics_id
urlpatterns = [
    path('', topics, name='topics'),
    path('<topic_id>/',topics_id , name='topics_id'),
    path('<topic_id>/subscribe/',subscribe  , name='subscribe'),
    path('<topic_id>/unsubscribe/', unsubscribe, name='unsubscribe'),
]