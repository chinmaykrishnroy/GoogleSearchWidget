import speech_recognition as sr
from PySide6.QtCore import QThread, Signal


class VoiceSearchThread(QThread):
    voice_recognized = Signal(str)

    def __init__(self, ui):
        super().__init__()
        self.ui = ui

    def run(self):
        recognizer = sr.Recognizer()
        recognizer.dynamic_energy_threshold = True
        recognizer.energy_threshold = 200
        try:
            with sr.Microphone() as microphone:
                self.ui.searchInputText.clear()
                recognizer.adjust_for_ambient_noise(microphone, duration=0.3)
                self.ui.searchInputText.setPlaceholderText(u"Listening...")
                audio = recognizer.listen(microphone)
                self.ui.searchInputText.setPlaceholderText(u"Processing...")
                query = recognizer.recognize_google(audio)
                self.voice_recognized.emit(query)
        except sr.WaitTimeoutError:
            self.ui.searchInputText.setPlaceholderText(u"Listening timed out!")
            self.voice_recognized.emit("")
        except sr.UnknownValueError:
            self.ui.searchInputText.setPlaceholderText(
                "Could not understand audio")
            self.voice_recognized.emit("")
        except sr.RequestError as e:
            self.ui.searchInputText.setPlaceholderText(
                f"Could not request results; {e}")
            self.voice_recognized.emit("")
        except Exception as e:
            self.ui.searchInputText.setPlaceholderText("An error occurred")
            self.voice_recognized.emit("")
