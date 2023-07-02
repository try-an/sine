import sine

def test_nokia_sine():
    with open("tests/examples/nokia.sine", "r", encoding="utf-8") as f: # the `encoding="utf-8"` is important, if it's not specified, it will raise an assertion error
        file = f.read()

    test = sine.SineFile("tests/examples/nokia.sine")

    assert type(test.audio) == sine.WaveForm
    assert test.reapeat == 2
    assert test.sample_rate == 48000
    assert test.text_content == file
    assert test.wave_type == "tri"

    # if all check have passed, the audio will play
    test.play()

def test_repeat_sine():
    with open("tests/examples/repeatsignal.sine", "r", encoding="utf-8") as f:
        file = f.read()

    test = sine.SineFile("tests/examples/repeatsignal.sine")

    assert type(test.audio) == sine.WaveForm
    assert test.reapeat == 10
    assert test.sample_rate == 8000
    assert test.text_content == file
    assert test.wave_type == "sine"

    # if all check have passed, the audio will play
    test.play()

if __name__ == "__main__":
    test_nokia_sine()
    test_repeat_sine()
