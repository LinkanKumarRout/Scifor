from django.shortcuts import render
import requests

# Create your views here.
def details(request):
    data = requests.get('https://jsonplaceholder.typicode.com/posts')
    if data.status_code == 200:
        json_data = data.json()
        context = {
            'data':json_data
        }
        return render(request, 'index.html', context)

def change_data(request):
    if request.method == 'GET':
        return render(request, 'change_data.html')
    else:
        pass