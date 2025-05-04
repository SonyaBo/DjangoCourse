from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def topics(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Topics")

def topics_id(request: HttpRequest, topics_id: int) -> HttpResponse:
    return HttpResponse(f"Topics with #{topics_id}.")

def subscribe(request: HttpRequest, topics_id: int) -> HttpResponse:
    return HttpResponse(f"Topics with #{topics_id} subscribe.")

def unsubscribe(request: HttpRequest, topics_id: int) -> HttpResponse:
    return HttpResponse(f"Topics with #{topics_id} unsubscribe.")
