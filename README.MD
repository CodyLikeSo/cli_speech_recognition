# Audio Recognizer

This project is a simple audio recognizer that can transcribe audio files in either English or Russian. It also allows you to adjust the volume and speed of the audio, and save the result as a new .wav file.

## Quick Use

1. Set up the virtual environment
```
(.venv) >>> 
    1. !python -m venv .venv
    2. !source .venv/bin/activate
```
2. Install required libraries
```
!pip install pydub DateTime speech_recognition
```
3. Download a .wav file from a website like [freesound.org](http://freesound.org) and take note of its path.
4. Run the `recognize.py` script, passing in the path to the .wav file as an argument.
```
!python recognize.py /path/to/audiofile.wav
```
5. To change the volume or speed of the audio, use the `--volume` and `--speed` flags, respectively.
```
!python recognize.py /path/to/audiofile.wav --volume 0.5 --speed 1.5
```
6. The transcription will be printed to the console, and a new .wav file with the transcription will be saved in the current directory.

## Supported Languages

The recognizer supports both English and Russian. To change the language, use the `--language` flag.
```
!python recognize.py /path/to/audiofile.wav --language ru
```

## Customization

You can customize the recognizer by modifying the `recognize.py` script. The script uses the `speech_recognition` library to transcribe the audio, and the `pydub` library to adjust the volume and speed.

The script first loads the audio file using `pydub`, then uses the `speech_recognition` library to transcribe it. The transcription is then printed to the console and saved as a new .wav file using `pydub`.

You can modify the script to add additional features or change the way it works. For example, you could add support for additional languages, or modify the way the volume and speed are adjusted.

I hope you find this project useful! If you have any questions or suggestions, please let me know.