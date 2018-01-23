import audioop
import contextlib
import collections
import math
import pyaudio
import wave

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
                    frames_per_buffer=chunk)
    try:
        yield stream
    finally:
        stream.stop_stream()
        p.terminate()


def save_record(data, file="output.wav", channels=CHANNELS, format=FORMAT, rate=RATE):
    if isinstance(data, collections.Iterable):
        data = b''.join(data)
    wf = wave.open(file, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(pyaudio.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(data)
    wf.close()


def get_record_seconds(rate, data_size):
    if data_size <= 0:
        return 0
    return data_size / rate


def is_sound_large(data):
    return math.sqrt(abs(audioop.avg(data, 4))) > 10000


if __name__ == '__main__':
    import io


    def test_save_record_to_file_like_object():
        f = io.BytesIO()
        save_record([], f)
        return f.getvalue()


    wav_content = test_save_record_to_file_like_object()
