from .__waveform import WaveForm
from .__read_sine_file import read_sine_file

class SineFile:
    """# `SineFile` object

    ---

    A class that stores a sine file and it's informations.

    ---
    
    ## Properties
    
    `text_content`: the file's raw content

    `reapeat`: an int that represents how many times the file will repeat

    `wave_type`: a string showing the type of wave that's being played

    `sample_rate`: an int that represents the sample rate of the file

    `notes`: a list contaning tuples that represent frequency-duration pairs

    `audio`: a `WaveForm` object containing the raw audio

    ## Methods
    
    `play`: play the file
    
    `save_to_wav`: save the audio to a .wav file

    `save_to_sine`: save the text content to a .sine file
    
    ## Constructor's arguments:
    
    `path`: the path to the sine file you want to make an object of"""

    def __init__(self, path: str):
        """Read a sine file from a file path and create a `SineFile` object,
        letting you play and save the audio of the object (into a .wav or .sine file)

        ---

        # Arguments

        `path`: just like it's name, it's the path
        to the sine file

        ---

        For more about the `SineFile` object,
        please see the docstring of the class or look at the documentation"""

        info = read_sine_file(path)
        self.text_content = info[0]
        self.reapeat = info[1]
        self.wave_type = info[2]
        self.sample_rate = info[3]
        self.notes = info[4]
        self.audio = WaveForm("custom", info[5], sample_rate=self.sample_rate)

    def play(self):
        """Play the audio file"""
        self.audio.play_audio()

    def save_to_wav(self, filename: str):
        """Save the audio to a .wav file"""
        self.audio.save_audio(filename)

    def save_to_sine(self, filename: str):
        """Save object to a .sine file"""
        if filename[-5:] != ".sine":
            raise NameError("File must end in \".sine\"'")

        with open(filename, "w", encoding="utf-8") as sine_file:
            sine_file.write(self.text_content)
