from numpy import linspace, sin, pi, sqrt
from scipy.signal import square, sawtooth

def __numpy_audio_linespace(duration_miliseconds: int, sample_rate: int):
    wave_duration_seconds = duration_miliseconds/1000
    wave_duration_samples = int(sample_rate * wave_duration_seconds)
    return linspace(0, wave_duration_seconds, wave_duration_samples)

def create_sin_wave(frequency: int, duration_miliseconds: int, sample_rate: int):
    t = __numpy_audio_linespace(duration_miliseconds, sample_rate)
    return sin(2 * pi * frequency * t)

def create_square_wave(frequency: int, duration_miliseconds: int, sample_rate: int):
    t = __numpy_audio_linespace(duration_miliseconds, sample_rate)
    return (1/sqrt(2)) * square(2 * pi * frequency * t) # 1/sqrt(2) is the rms of a sine wave of amplitude 1

def create_saw_wave(frequency: int, duration_miliseconds: int, sample_rate: int):
    t = __numpy_audio_linespace(duration_miliseconds, sample_rate)
    return (1/sqrt(2)) * sawtooth(2 * pi * frequency * t)

def create_triangle_wave(frequency: int, duration_miliseconds: int, sample_rate: int):
    t = __numpy_audio_linespace(duration_miliseconds, sample_rate)
    return sawtooth(2 * pi * frequency * t, 0.5)
