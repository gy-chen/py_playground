import pyaudio
import wave
from . import *

RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"


def main():
    with get_input_stream() as stream:
        print("* recording")

        frames = []
        for i in range(RATE // CHUNK * RECORD_SECONDS):
            data = stream.read(CHUNK)
            if is_sound_large(data):
                print("Large sound?")
            print(get_record_seconds(RATE, len(frames) * CHUNK))
            frames.append(data)

        print("* done recording")

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pyaudio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


if __name__ == '__main__':
    main()
