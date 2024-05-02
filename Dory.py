import speech_recognition as sr
import pyttsx3

# Инициализация движка синтеза речи
engine = pyttsx3.init()

# Инициализация распознавателя речи
r = sr.Recognizer()

# Функция для обработки голосовых команд
def process_command(text):
    if "открой" in text.lower():
        # Открыть файл
        print("Opening file...")
    elif "save file" in text.lower():
        # Сохранить файл
        print("Saving file...")
    elif "format text" in text.lower():
        # Форматировать текст
        print("Formatting text...")
    elif "стоп" in text.lower():
        # Выйти из приложения
        print("Exiting application...")
        return False
    else:
        print("I didn't understand the command.")
    return True

# Основной цикл приложения
while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        text = r.recognize_google(audio,language="ru-RU")
        print(f"You said: {text}")

        # Обработка голосовой команды
        if not process_command(text):
            break
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")