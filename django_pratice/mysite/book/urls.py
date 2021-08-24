from django.urls import path
from django.urls.resolvers import URLPattern 
from . import views 

urlpatterns=[

    path('listall',views.list_all_books),
]

