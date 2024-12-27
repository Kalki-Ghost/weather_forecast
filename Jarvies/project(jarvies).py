import pyttsx3
import win32com.client


def say(text):
    engine = pyttsx3.init()
    engine.say(f" {text}")
    engine.runAndWait()


if __name__ == '__main__':
    print("Pycharm")
    say("Hello I am Jarvis AI")
