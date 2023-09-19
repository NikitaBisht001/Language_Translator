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

