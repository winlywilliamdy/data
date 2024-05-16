import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import datetime

def callback(indata, frames, time, status):
    if status:
        print(status, flush=True)
    audio_data.extend(indata.flatten())

def record_audio(sample_rate=48000, channels=1):
    global audio_data
    audio_data = []

    print("Press 'Enter' to start recording. Press 'Enter' again to stop recording.")
    # Wait for user to press 'Enter' to start recording
    input("Press 'Enter' to start recording...")
    print("Recording...")

    with sd.InputStream(callback=callback, channels=channels, samplerate=sample_rate):
        input("Press 'Enter' to stop recording...")

    print("Recording complete.")

    return np.array(audio_data)



def save_audio(filename, data, sample_rate=48000):
    print("Saving audio to:", filename)
    
    # Save audio to a file
    write(filename, rate=sample_rate, data=data)

    print("Audio saved.")

def start_record():
    start_time = datetime.datetime.now()
    output_filename = 'keylogger_{a}.wav'.format(a = start_time.strftime("%Y-%m-%d_%H:%M:%S"))

    # Record audio
    audio_data = record_audio()

    # Save audio to a file
    save_audio(output_filename, audio_data)