"""
# SINE

A file format containing a list of audio waves.

---

## What is it ?

The sine file format represents a list of
frequency-duration pairs to create sound.
When reading a file in this format,
you'll hear sine, triangle, square or saw waves playing at precise frequencies and durations.
You can create music, signals and so much more.
All that you need is an idea for a sound and a simple command.

---

## Commands

Sine puts 3 CLI tools when the package is installed: `sineread.py`, `sinemake.py` and `sinesave.py`.
(Don't ask why the extension is .py since the file is not binary 🙂)

For sineread the arguments are:

`sineread.py [-h] filename`

For sinemake:

`sinemake.py [-h] notes output repeat samplerate wavetype`

For sinesave:

`sinesave.py [-h] filename output`

It is recommended to run these commands with the prefix `python`, `py` or `python3`

For help on using these commands use the `-h` flag to display help for these commands

---

By try-an

"""


from .__waveform import (
    WaveForm
)

from .__sinefile import (
    SineFile
)