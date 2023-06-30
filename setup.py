import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="sine",
    version="0.0.1",
    description="A package to read a file in a file format containing a list of frequency-duration pairs",
    long_description=long_description,

    author="try-an",
    keywords=["audio", "file format", "waves"],
    license="MIT",

    requires=["sounddevice", "numpy", "scipy"],
    packages=["sine"],
    scripts=["sinemake.py", "sineread.py", "sinesave.py"],

    url="https://github.com/try-an/sine"
)
