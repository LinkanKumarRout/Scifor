from django.shortcuts import render
from pytube import * 

# Create your views here.
def youtube_download(request):
    if request.method == 'POST':
        link = request.POST['link']
        video = YouTube(link)

        stream = video.streams.get_lowest_resolution()
        stream.download()
        return render(request, 'youtube.html')
    return render(request, 'youtube.html')