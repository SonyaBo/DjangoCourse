from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def main(request: HttpRequest) -> HttpResponse:
    var = "Something"
    return render(request,'index.html',{"str":var})

def my_feed(request: HttpRequest) -> HttpResponse:
    return HttpResponse("My feed")

def create(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Create page')

def profile(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Profile')

def register(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Register')

def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Login')

def logout(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Logout')


def article(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"This is article #{article_id}.")

def article_comment(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Comment article #{article_id}.")


def article_update(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Update article #{article_id}.")


def article_delete(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Delete article #{article_id}.")
