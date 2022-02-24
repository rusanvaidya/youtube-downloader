from django.shortcuts import render, redirect

from pytube import YouTube
import os
# Create your views here.

def home(request):
    return render(request, 'index.html', {"file": None})


def download_audio(request):
    if request.method == 'POST':
        link = request.POST['link']
        yt = YouTube(link)
        Title = "Title: " + yt.title
        Author = "By: " + yt.author
        Thumbnail = yt.thumbnail_url  
        audio = yt.streams.get_by_itag('140')
        get_file = audio.download("downloads/audio")
        file_name, ext = os.path.splitext(get_file)
        audio_file = file_name+'.mp3'
        os.rename(get_file, audio_file)      
        audio_file = audio_file.split("/")[-1]
        return render(request, 'index.html', {"Title": Title, 'Author': Author, "file": audio_file, 'type': 'Audio', "thumbnail": Thumbnail})
    else:
        return redirect("/")

def download_video(request):
    if request.method == 'POST':
        link = request.POST['link']
        yt = YouTube(link)
        Title = "Title: " + yt.title
        Author = "By: " + yt.author    
        Thumbnail = yt.thumbnail_url   
        video = yt.streams.filter(progressive=True, res="720p")[0]
        video_file = video.download("downloads/video")
        video_file = video_file.split("/")[-1]
        return render(request, 'index.html', {"Title": Title, 'Author': Author, "file": video_file, 'type': 'Video', "thumbnail": Thumbnail})
    else:
        return redirect("/")