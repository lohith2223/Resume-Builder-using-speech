import speech_recognition as sr
import google.generativeai as genai
import os
from googletrans import Translator

# Set up Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/lohithyadav/Desktop/hr_chat_bot/ai/lohith-429808-9b56cb6afd25.json'

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize Gemini Pro API
genai.configure(api_key='AIzaSyBc_roClS6TVQaHK0dEyzPT4SR7EPmWv50')
model = genai.GenerativeModel('gemini-pro')

# Initialize translator
translator = Translator()


def record_audio():
    with sr.Microphone() as source:
        print("Speak now...")
        audio = recognizer.listen(source)
    return audio


def transcribe_audio(audio):
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Speech recognition could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results from speech recognition service; {e}"


def analyze_text(text):
    prompt = f"""
    Analyze the following text and categorize it into different sections of an ATS resume:

    {text}

    Categories should include:
    1. Name
    2. Email
    3. Contact
    4. Career Objective
    5. Education
    6. Project/Internship
    7. Skills
    8. Achievements

    For each category, provide the relevant information from the text without using stars (*) in the headings.
    """
    response = model.generate_content(prompt)
    return response.text


def translate_text(text, lang_code):
    try:
        translated = translator.translate(text, dest=lang_code)
        return translated.text
    except Exception as e:
        return f"Translation error: {e}"


def get_language_choice():
    print("Select language for the resume content:")
    print("1. English")
    print("2. Telugu")
    print("3. Hindi")
    choice = input("Enter the number corresponding to your choice: ")
    if choice == '1':
        return 'en'
    elif choice == '2':
        return 'te'
    elif choice == '3':
        return 'hi'
    else:
        print("Invalid choice. Defaulting to English.")
        return 'en'


def main():
    audio = record_audio()
    transcribed_text = transcribe_audio(audio)
    print("Transcribed text:", transcribed_text)

    analysis = analyze_text(transcribed_text)
    print("\nAnalysis and categorization:")
    print(analysis)

    lang_code = get_language_choice()
    translated_analysis = translate_text(analysis, lang_code)
    print("\nTranslated Resume Content:")
    print(translated_analysis)


if _name_ == "_main_":
    main()
