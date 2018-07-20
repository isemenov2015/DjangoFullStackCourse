from django.conf.urls import url
from appThree import views

urlpatterns = [
    url(r"^$", views.index, name = "index"),
]
