from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content': "Hello, I'm from app Three!"}
    return render(request, 'appThree/index.html', context = my_dict)
