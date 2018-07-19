from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'insert_me': "Hello, I'm from ProTwo/index.html"}
    return render(request, 'ProTwo/index.html', context = my_dict)

def help(request):
    my_dict = {'help_me': "Hello, I'm from ProTwo/help.html"}
    return render(request, 'ProTwo/help.html', context = my_dict)
