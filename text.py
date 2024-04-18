import speech_recognition as sr

def wav_to_text(file_path):
    r = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = r.record(source)
        try:
            text = r.recognize_google(audio_data, language='ru')
            return text
        except:
            return "Could not recognize speech"