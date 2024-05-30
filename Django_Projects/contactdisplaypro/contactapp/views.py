from django.shortcuts import render
from .models import ContactpageData

# Create your views here.
def ContactPage(request):
    if request.method == 'GET':
        return render(request, 'contactpage.html')
    else:
        ContactpageData(
            firstname = request.POST['fname'],
            lastname = request.POST['lname'],
            email = request.POST['email'],
            mobile = request.POST['mobile'],
            skill = request.POST['skill'],
            location = request.POST['loc']
        ).save()
        return render(request, 'contactpage.html')

def DisplayData(request):
    data = ContactpageData.objects.all()
    return render(request, 'displaycontact.html', {'data':data})