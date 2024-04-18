from pydub import AudioSegment
import math

def change_volume(path, volume):
    audio = AudioSegment.from_wav(path)
    new_audio = audio.set_frame_rate(audio.frame_rate) \
                        .set_channels(audio.channels) \
                        .apply_gain(20*math.log10(volume))

    new_audio.export("new_volume.wav", format="wav")
