import argparse
import sine

parser = argparse.ArgumentParser(
    description="Convert a sine file into a .wav file",
    epilog="For more help, please visit the documentation"
)

parser.add_argument("filename", help="Name of the file that you want to convert")
parser.add_argument("output", help="Name of the converted .wav file")
args = parser.parse_args()

audio = sine.SineFile(args.filename)
audio.save_to_wav(args.output)
