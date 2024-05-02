import speech_recognition as sr
import os
import sys 
import webbrowser
import pyttsx3
import vosk

def talk(words):
    # print(words)
    # os.system("say"+ words)
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
talk("Спроси у меня что либо")
def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio =r.listen(source)
    try:
        zadanie = r.recognize_vosk(audio).lower()
        print("Вы сказали"+ zadanie)
    except sr.UnknownValueError:
        talk("Вас не поняли")
        zadanie = command()
    return zadanie

def makeSomething(zadanie):
    if 'открой сайт' in zadanie:
        talk("открываю")
        url ='https://music.yandex.ru/users/DiamondOwl961/playlists'
        webbrowser.open(url)
    elif 'стоп' in zadanie:
        talk("Да конечно без проблем")
        sys.exit()

while True:
    makeSomething(command())
