from pydub import AudioSegment

def speed_change_into(path, speed):
    sound = AudioSegment.from_file(path)
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

def speed_change(path, speed):
    sound = speed_change_into(path, speed)
    sound.export("new_speed.wav", format="wav")