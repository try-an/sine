import argparse
import sine

parser = argparse.ArgumentParser(
    description="Play a sine file",
    epilog="For more help, please visit the documentation"
)
parser.add_argument("filename", help="Name of the sine file that you want to play")
args = parser.parse_args()

audio = sine.SineFile(args.filename)
audio.play()
