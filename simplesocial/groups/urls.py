from django.urls import path
from . import views

app_name = 'groups'

urlpattern = [
        path('', views.ListGroups.as_view(), name = 'all'),
        path('new/', views.CreateGroup.as_view(), name = 'create'),
        path('posts/in/(?P<slug>)[-\W]+/', views.SingleGroup.as_view(), name = 'single'),
]
