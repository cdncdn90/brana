from django.urls import path
 
from . import view
 
urlpatterns = [
    path('hello/', view.hello),
    path('balabala/', view.balabala),
]