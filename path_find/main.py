# Python Program that helps translate Speech to Text

import speech_recognition
import pyttsx3
import voices
from googletrans import Translator


translator = Translator()
# The Recognizer is initialized.
engine = pyttsx3.init()
UserVoiceRecognizer = speech_recognition.Recognizer()


def get_Language(argument):
    switcher = {
        0: "en",
        2: "es",
        3: "ja",
        4: "ko",
        5: "zh-CN",
        6: "hi",




    }
    return switcher.get(argument, "en")  # Default to English if the option is not found


def getLanguage(argument):
    switcher = {
        0: "en-IN",
        2: "es-ES",
        3: "ja-JP",
        4: "ko-KR",
        5: "zh-CN",
        6: "hi-IN",

    }
    return switcher.get(argument, "en-IN")  # Default to English (India) if the option is not found


def getSelection():
    while True:
        try:
            userInput = int(input())
            if userInput < 0 or userInput > 6:
                print("Not an integer! Try again.")
                continue
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput



while 1:
    try:
        print("0. ENGLISH")
        print("2. SPANISH")
        print("3. JAPANESE")
        print("4. KOREAN")
        print("5. CHINESE")
        print("6. HINDI")
        print("Select your language:")



        lang = getLanguage(getSelection())

        with speech_recognition.Microphone() as UserVoiceInputSource:
            UserVoiceRecognizer.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.5)

            # The Program listens to the user voice input.
            UserVoiceInput = UserVoiceRecognizer.listen(UserVoiceInputSource)
            UserVoiceInput_converted_to_Text = UserVoiceRecognizer.recognize_google(UserVoiceInput, language=lang)
            UserVoiceInput_converted_to_Text = UserVoiceInput_converted_to_Text.lower()
            print("Detected Text:", UserVoiceInput_converted_to_Text)
            print("0. ENGLISH")
            print("2. SPANISH")
            print("3. JAPANESE")
            print("4. KOREAN")
            print("5. Chinese")
            print("6. HINDI")
            print("choose a language you wanted to convert it to:")



            tran = getSelection()
            lang = get_Language(tran)
            #print("Selected Language:", lang)
            translated_text = translator.translate(UserVoiceInput_converted_to_Text, dest=lang)
            translation_result = translated_text.text
            print("Translated Text:", translation_result)
            voices = engine.getProperty('voices')
            if len(voices) > 0:
                desired_voice = voices[tran].id  # Use the first voice in the list
                engine.setProperty('voice', desired_voice)
            else:
                print("No voices available.")
            engine.setProperty('rate', 145)
            engine.say(translation_result)
            # play the speech
            engine.runAndWait()

            #engine.setProperty('voice', lang)  # Set the desired language voice
            #engine.say(translation_result)
            #engine.runAndWait()

    except KeyboardInterrupt:
        print('A KeyboardInterrupt encountered; Terminating the Program !!!')
        exit(0)

    except speech_recognition.UnknownValueError:
        print("No User Voice detected OR unintelligible noises detected OR the recognized audio cannot be matched to text !!! \n CAN YOU PLEASE DO IT AGAIN")
"""
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(f"Voice: {voice.name}")
    print(f"Voice: {voice.id}")"""

"""def translate_text(target: str, text: str) -> dict:
    Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print("Text: {}".format(result["input"]))
    print("Translation: {}".format(result["translatedText"]))
    print("Detected source language: {}".format(result["detectedSourceLanguage"]))

    return result


def getLanguage(argument):
    switcher = {
        0: "en-IN",
        5: "hi-IN",
        4: "zh-CN",
        3: "ko-KR",
        2: "ja-JP"
    }
    return switcher.get(argument, 0)

text = input("enter the text")

print("0.ENGLISH")
print("5.HINDI")
print("4.chinese")
print("3.KOREAN")
print("2.JAPANESE")
tran = input("select a language to convert in")
lang = getLanguage(tran)
translate_text(lang, text)"""

"""from googletrans import Translator

translator = Translator()

def getLanguage(argument):
    switcher = {
        0: "en",
        5: "hi",
        4: "zh-CN",
        3: "ko",
        2: "ja"
    }
    return switcher.get(argument, 0)

#print(getLanguage(0))
print("0.ENGLISH")
print("5.HINDI")
print("4.chinese")
print("3.KOREAN")
print("2.JAPANESE")
txt = input("select a language to enter the text")
text = input("enter the text")

print("0.ENGLISH")
print("5.HINDI")
print("4.chinese")
print("3.KOREAN")
print("2.JAPANESE")
tran = input("select a language to convert in")
language = getLanguage(tran)

print(language)
translated_text = translator.translate(text, dest=language)
print(translated_text.text)
"""
"""from googletrans import Translator

translator = Translator()
try:
    translated_text = translator.translate("Hello, how are you?", dest="es")
    print(translated_text.text)
except Exception as e:
    print("Translation failed:", e)"""
"""from googletrans import Translator

translator = Translator()

def getLanguage(argument):
    switcher = {
        0: "en",
        5: "hi",
        4: "zh-CN",
        3: "ko",
        2: "ja"
    }
    return switcher.get(argument, "en")  # Default to English if the option is not found

print("0.ENGLISH")
print("5.HINDI")
print("4.chinese")
print("3.KOREAN")
print("2.JAPANESE")
txt = int(input("select a language to enter the text: "))
text = input("enter the text: ")

print("0.ENGLISH")
print("5.HINDI")
print("4.chinese")
print("3.KOREAN")
print("2.JAPANESE")
tran = int(input("select a language to convert in: "))
lang = getLanguage(tran)
print(lang)
translated_text = translator.translate(text, dest=lang)
print(translated_text.text)"""

