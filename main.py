import sys
import threading
import tkinter as tk

import speech_recognition
import pyttsx3 as tts

from neuralintents import GenericAssistant

class Assistant:

    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty("rate", 150)

        self.assistant = GenericAssistant("intents.json", intent_methods=({"file": self.create_file}))

        self.root = tk.Tk()
        self.label = tk.Label(text="☺",font=("Arial",130, "bold"))
        self.label.pack()

        threading.Thread(target=self.run_assistant).start()


        self.root.mainloop()

    def create_file(self):
        with open("createfile.txt", "w") as f:
            f.write("Welcome to your new file")


    def run_assistant(self):
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)
                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()

                    if "hey lara" in text :
                        self.label.config(fg="red")
                        audio = self.recognizer.listen(mic)
                        text= self.recognizer.recognize_google(audio)
                        text = text.lower()
                        if text == "stop" :
                            self.speaker.say("Bye")
                            self.speaker.runAndWait()
                            self.speaker.stop()
                            self.root.destroy()
                            sys.exit()
                        else:
                            if text is not None:
                                response = self.assistant.request(text)
                                if response is not None:
                                    self.speaker.say(response)
                                    self.speaker.runAndWait()
                            self.label.config(fg="black")
        
            except:
                self.label.config(fg="black")
                continue



Assistant()