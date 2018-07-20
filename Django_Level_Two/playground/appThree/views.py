from django.shortcuts import render
from appThree.models import Topic, Webpage, AccessRecord, User

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    fields_dict = {'access_records': webpages_list}
    return render(request, 'appThree/index.html', context = fields_dict)

def users(request):
    users_list = User.objects.order_by("surname")
    fields_dict = {"users_list": users_list}
    return render(request, 'appThree/users.html', context = fields_dict)
