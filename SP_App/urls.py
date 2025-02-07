from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path("sent-contact/",views.sent_contact,name="sent-contact")
]