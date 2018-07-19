from django.conf.urls import url
from appProTwo import views

urlpatterns = [
    url(r"^$", views.help, name = "help"),
]
