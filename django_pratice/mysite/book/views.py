from django.http.response import HttpResponse
from django.shortcuts import render

#def get_all_books():
#    return list1 

def list_all_books(request):
    response = "get all books"
    return HttpResponse(response)

# Create your views here.
