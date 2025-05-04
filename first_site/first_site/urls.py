
"""
URL configuration for first_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from articles.views import main, create, my_feed, create, profile, register,login, logout
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('my-feed/', my_feed),
    path('create/', create),
    path('profile/', profile),
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    path('<int:article_id>/', include('articles.urls'))
]
