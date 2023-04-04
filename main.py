import speech_recognition as sr
import pyttsx3
import pyaudio

pa = pyaudio.PyAudio()
device_index = -1

for i in range(pa.get_device_count()):
    dev = pa.get_device_info_by_index(i)
    if dev['name'] == 'Your Microphone Name':
        device_index = dev['index']
        break

if device_index == -1:
    print("Microphone not found!")
else:
    print(f"Using Microphone: {device_index}")

r = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    print("Speak something:")
    audio = r.listen(source)

text = r.recognize_google(audio)
print(f"You said: {text}")

engine.say(f"You said: {text}")
engine.runAndWait()

