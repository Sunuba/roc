import pyttsx3


class Speak:
    def __init__(self):
        self.speaker = pyttsx3.init(driverName='sapi5')
        self.speaker.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

    def speak(self, text):
        self.speaker.say(text)
        self.speaker.runAndWait()
