import speech_recognition as sr
from pydub import AudioSegment

from text import wav_to_text
from speed import speed_change
from volume import change_volume

# path = '/home/cody/Code/Python/speech_recognition/wavs/example1.wav'

path = input('Put link to wav file here...')


def option():
    option = input('Input option in console:\n1. speed)\n2. volume\n')
    try:
        match option:
            case 'speed':
                try:
                    speed = float(input('Choose speed...'))
                    speed_change(path=path, speed=speed)
                except Exception as e:
                    print(f"wrong data {e}")
            case 'volume':
                try:
                    volume = float(input('Choose volume...'))
                    change_volume(path=path, volume=volume)
                except Exception as e:
                    print(f"wrong data {e}")
    except:
        print('wrong option')

try:
    print(f'Text >>> {wav_to_text(path)}')
    option()
except:
    print("error path")