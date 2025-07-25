from pytubefix import YouTube
from moviepy import AudioFileClip
#import speech_recognition as sr
import os

def download(url):
    #puxando a URL fornecida e fazendo o download do video completo e do audio em formato MP4 separado 
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True).get_highest_resolution()
    video_aud = yt.streams.filter(only_audio=True).first() #pegando o audio 
    video.download(output_path=r'Videos')
    audio = video_aud.download(output_path=r'Videos')
    
    #convertento somentente o audio em arquivo baixado para MP3 
    conversor_audio = os.path.splitext(audio)[0] + ".mp3"
    audioclip = AudioFileClip(audio)
    audioclip.write_audiofile(conversor_audio)
    audioclip.close()
    os.remove(audio)
    


    
    
    

    
download('https://www.youtube.com/watch?v=oPlXecD-gZM&list=PLxI8Can9yAHeHQr2McJ01e-ANyh3K0Lfq&index=2')