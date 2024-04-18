import speech_recognition as sr
from pydub import AudioSegment
import json
import datetime

from text import wav_to_text
from speed import speed_change
from volume import change_volume

# path = '/home/cody/Code/Python/speech_recognition/wavs/example1.wav'

path = input('Put link to wav file here...')

def log_event(event, message):
    """Log an event using JSON format"""
    log_entry = {
        "timestamp": str(datetime.datetime.now()),
        "event": event,
        "message": message
    }
    log_entry_json = json.dumps(log_entry)
    with open('logs.json', 'a') as f:
        f.write(log_entry_json + '\n')

def option():
    option = input('Input option in console:\n1. speed)\n2. volume\n')
    try:
        match option:
            case 'speed':
                try:
                    speed = float(input('Choose speed...'))
                    log_event("INFO", f"Changing speed to {speed}")
                    speed_change(path=path, speed=speed)
                except Exception as e:
                    log_event("ERROR", f"Error changing speed: {e}")
                    print(f"wrong data {e}")
            case 'volume':
                try:
                    volume = float(input('Choose volume...'))
                    log_event("INFO", f"Changing volume to {volume}")
                    change_volume(path=path, volume=volume)
                except Exception as e:
                    log_event("ERROR", f"Error changing volume: {e}")
                    print(f"wrong data {e}")
    except:
        log_event("ERROR", "Invalid option")
        print('wrong option')

try:
    log_event("INFO", f'Transcribing wav file: {path}')
    print(f'Text >>> {wav_to_text(path)}')
    option()
except Exception as e:
    log_event("ERROR", f"Error processing wav file: {e}")
    print("error path")