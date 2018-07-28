from django.urls import path, include
from django.conf.urls import url
from appSix import views

app_name = 'appSix'

urlpatterns = [
    path('', views.SchoolList.as_view(), name = 'list'),
    url(r'^(?P<pk>[-\w]+)/', views.SchoolDetailView.as_view(), name = 'detail')
]
