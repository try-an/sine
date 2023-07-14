import argparse
from sine.__special_chars import gs, us, eot, soh, stx, etx

# Example command:
# python sinemake.py "164-125 146-125 92-250 102-250 138-125 122-125 72-250 82-250 122-125 110-125 68-250 82-250 110-500 0-500" nokia.sine 2 48000 square

parser = argparse.ArgumentParser(
    description="Create sine files by specifying frequencies with a specific syntax. (Sine is a file format for creating frequency-duration pairs)",
    epilog="For more help, please visit the documentation"
)

parser.add_argument(
    "notes",
    help="The content of the sine file, use the syntax: '[frequency (hz)]-[duration (ms)] [frequency (hz)]-[duration (ms)] ...'"
)

parser.add_argument(
    "output",
    help="Name of the sine file"
)

parser.add_argument(
    "repeat",
    help="How many times will the audio repeat (if only once, just type 1)"
)

parser.add_argument(
    "samplerate",
    help="The audio's sample rate (usually 44100hz or 48000hz)"
)

parser.add_argument(
    "wavetype",
    help="Waveform used for the file (either sine, square, saw and tri)"
)

args = parser.parse_args()

notes = [note.split("-") for note in args.notes.split(" ")]

for index, note in enumerate(notes):
    notes[index] = us.join([chr(int(item)) for item in note])

notes = gs.join(notes)
header = f"{soh}SINFILE{us}{args.repeat}{us}{args.samplerate}{us}{args.wavetype}{stx}"
footer = f"{etx}SINFILE{eot}"

sine_file = header + notes + footer

with open(args.output, "w", encoding="utf-8") as f:
    f.write(sine_file)
