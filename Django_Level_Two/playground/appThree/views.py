from django.shortcuts import render
from appThree.models import Topic, Webpage, AccessRecord
from appThree.forms import NewUserForm

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    fields_dict = {'access_records': webpages_list}
    return render(request, 'appThree/index.html', context = fields_dict)

def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print("ERROR. FORM INVALID")
    return render(request, 'appThree/users.html', {'form': form})
