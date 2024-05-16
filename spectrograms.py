import numpy as np
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal

# Create a function to generate spectrogram
def generate_spectrogram(input_file, output_file):
    sample_rate, samples = wavfile.read(input_file)
    frequencies, times, spectrogram = signal.spectrogram(samples, fs=sample_rate)
    
    plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram))
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.title('Spectrogram')
    plt.colorbar()
    plt.savefig(output_file)
    plt.close()

# Specify the directory containing the WAV files
input_dir = "audio"
output_dir = "/Users/nabilajhidajat/Desktop/ASA/"
directory = "audio"
for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        file_path = os.path.join(directory, filename)


# Loop through all WAV files in the input directory and generate spectrogram
for file in os.listdir(input_dir):
    if file.endswith(".wav"):
        input_file = os.path.join(input_dir, file)
        output_file = os.path.join(output_dir, file.replace('.wav','spectrogram.png'))

        generate_spectrogram(input_file, output_file)