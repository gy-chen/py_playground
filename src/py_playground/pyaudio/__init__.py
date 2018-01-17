import audioop
import contextlib
import math
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100


@contextlib.contextmanager
def get_input_stream(chunk=CHUNK, format=FORMAT, channels=CHANNELS, rate=RATE):
    p = pyaudio.PyAudio()
    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=CHUNK)
    try:
        yield stream
    finally:
        stream.stop_stream()
        p.terminate()


def get_record_seconds(rate, data_size):
    if data_size <= 0:
        return 0
    return data_size / rate


def is_sound_large(data):
    return math.sqrt(abs(audioop.avg(data, 4))) > 10000
