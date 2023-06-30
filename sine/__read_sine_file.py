import re
from .__waveform import WaveForm
from .__special_chars import stx, etx, us, gs

def __read_file(path: str):
    if path[-5:] != ".sine":
        raise NameError("File must end in \".sine\"'")

    with open(path, "r", encoding="utf-8") as sine_file:
        file = sine_file.read()

    return file

def __parse_notes(notes: list):
    frequencies = []
    durations = []
    for group in notes:
        frequencies.append(ord(group[0])) # 1st character is the frequency
        # 2nd character is \x1f (the unit saperator)
        durations.append(ord(group[2])) # 3rd character is the duration

    return list(zip(frequencies, durations))

def __compose_audio(frequency_duration_pairs: list, wave_type: str, sample_rate: int, reapeat_amount: int):
    composed_audio = []
    for frequency, duration in frequency_duration_pairs:
        current_waveform = WaveForm(wave_type, frequency, duration, 1, sample_rate=sample_rate)
        composed_audio.extend(current_waveform.audio_data)

    return composed_audio * reapeat_amount

def read_sine_file(file_path: str):
    sine_file = __read_file(file_path)
    split_file = re.split(f"{stx}|{etx}", sine_file)

    header = split_file[0]
    header = header.split(f"{us}")

    if len(header) < 4:
        raise IndexError("File must have these header properties: \"SINEFILE\", reapeat amount, sample rate, and the wave type")

    reapeat = int(header[1])
    sample_rate = int(header[2])
    wave_type = header[3]

    note_characters = split_file[1]
    note_characters = note_characters.split(f"{gs}")

    frequency_duration_pairs = __parse_notes(note_characters)
    audio = __compose_audio(frequency_duration_pairs, wave_type, sample_rate, reapeat)

    return (sine_file, reapeat, wave_type, sample_rate, frequency_duration_pairs, audio)
