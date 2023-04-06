import openai
import speech_recognition as sr
import pyttsx3

# Set up the OpenAI API client
openai.api_key = "<INSERT YOUR API KEY HERE>"

# Set up the speech recognition engine
r = sr.Recognizer()

# Set up the text-to-speech engine
engine = pyttsx3.init()

# Define a function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error while processing your request.")
        return ""

# Define a function to generate a response using OpenAI
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text.strip()

# Define a function to speak the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
while True:
    prompt = recognize_speech()
    if prompt:
        response = generate_response(prompt)
        speak(response)
