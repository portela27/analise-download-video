from pytubefix import YouTube
from moviepy import AudioFileClip
#import speech_recognition as sr
import os
import whisper 


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

    return conversor_audio
    
def trascrever_audio(audio_path):
    modelo = whisper.load_model("small")
    transcricao = modelo.transcribe(audio_path)
    print(transcricao["text"]) 

    with open("transcrição.txt", "w", encoding="utf-8") as f:
        f.write(transcricao["text"])  
    
    print("Transcrição salva em 'transcrição.txt'")




caminho_audio = download('https://www.youtube.com/watch?v=C1yHhp9-8s4')
trascrever_audio(caminho_audio)
