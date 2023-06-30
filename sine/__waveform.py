import sounddevice as sd
from scipy.io.wavfile import write
from numpy import array
from .__waves import (
    create_sin_wave,
    create_saw_wave,
    create_square_wave,
    create_triangle_wave
)

class WaveForm:
    """# `WaveForm` object

    ---

    A class that stores audio waves such as sine, square, and others,
    having properties such as the sample rate and the
    raw audio data, where you can save and play the audio.

    ---
    
    ## Properties
    
    `audio_data`: a numpy array containing floats representing the audio of the waveform
    
    `sample_rate`: an integer (usually 48 000 or 44 100)
    representing the number of audio samples per second
    
    ## Methods
    
    `play_audio`: play the `audio_data` array
    
    `save_audio`: save the `audio_data` array to a .wav file
    
    ## Constructor's arguments:
    
    `wave_type`: either 'sine', 'square', 'saw', 'tri' or 'custom',
    the arguments that follow (*args) are the informations about the wave
    
    `*args`: if the wave type is not 'custom', the arguments are:
    frequency (in hz) and duration (in ms), if it is 'custom',
    then the argument is just the audo data
    
    `sample_rate`: set's the sample rate attribute"""

    def __init__(self, wave_type: str, *args, sample_rate: int):
        """Basic class for wave forms"""
        self.sample_rate = sample_rate
        self.audio_data = []

        match wave_type:
            case "sine":
                self.audio_data = create_sin_wave(args[0], args[1], sample_rate)
            case "square":
                self.audio_data = create_square_wave(args[0], args[1], sample_rate)
            case "saw":
                self.audio_data = create_saw_wave(args[0], args[1], sample_rate)
            case "tri":
                self.audio_data = create_triangle_wave(args[0], args[1], sample_rate)
            case "custom":
            # custom is an exception for storing other audio,
            # such as a composition of other waveform objects
                self.audio_data = args[0]

        self.audio_data = array(self.audio_data)

    def play_audio(self):
        sd.play(self.audio_data, self.sample_rate, blocking=True)
        sd.stop()

    def save_audio(self, filename: str):
        write(filename, self.sample_rate, self.audio_data)
