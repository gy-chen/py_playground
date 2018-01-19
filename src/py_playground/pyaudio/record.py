import enum
import logging
from . import *

logging.basicConfig(level=logging.DEBUG)

RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"


def record(record_seconds=RECORD_SECONDS):
    with get_input_stream() as stream:
        print("* recording")

        frames = []
        for i in range(RATE // CHUNK * record_seconds):
            data = stream.read(CHUNK)
            if is_sound_large(data):
                print("Large sound?")
            print(get_record_seconds(RATE, len(frames) * CHUNK))
            frames.append(data)

        print("* done recording")

    save_record(frames)


class StopRecordException(Exception):
    pass


class RecordStatus(enum.Enum):
    WAIT = enum.auto()
    RECORDING = enum.auto()
    IDLE = enum.auto()
    STOP = enum.auto()


class LargeSoundActivateRecorder:
    """Start record when detect large sound and stop recording when no large sound detected for specific seconds

    """

    def __init__(self, chunk=CHUNK, rate=RATE, stop_record_seconds=1):
        self._chunk = chunk
        self._rate = rate
        self._stop_record_seconds = stop_record_seconds
        self._reset()

    def record(self):
        with get_input_stream(chunk=self._chunk, rate=self._rate) as stream:
            try:
                while True:
                    data = stream.read(self._chunk)
                    if is_sound_large(data):
                        self._on_sound_large(data)
                    else:
                        self._on_sound_not_large(data)
            except StopRecordException:
                recorded = self._recorded_sounds
                logging.debug("done recording")
                logging.debug("recorded %s seconds" % get_record_seconds(self._rate, len(recorded) * self._chunk))
                self._reset()
                return recorded

    def _on_sound_large(self, data):
        logging.debug('on_sound_large')
        if self._status == RecordStatus.WAIT:
            self._status = RecordStatus.RECORDING
            self._recorded_sounds.append(data)
        elif self._status == RecordStatus.IDLE:
            self._status = RecordStatus.RECORDING
            self._recorded_sounds.extend(self._idle_sounds)
            self._recorded_sounds.append(data)
            self._idle_sounds = []

    def _on_sound_not_large(self, data):
        logging.debug('on_sound_not_large')
        if self._status == RecordStatus.RECORDING:
            self._status = RecordStatus.IDLE
            self._on_idle(data)
        elif self._status == RecordStatus.IDLE:
            self._on_idle(data)

    def _on_idle(self, data):
        logging.debug('on_idle')
        self._idle_sounds.append(data)
        idle_seconds = get_record_seconds(self._rate, len(self._idle_sounds) * self._chunk)
        logging.debug('idle %s seconds' % idle_seconds)
        if idle_seconds >= self._stop_record_seconds:
            self._status = RecordStatus.STOP
            self._recorded_sounds.extend(self._idle_sounds)
            raise StopRecordException()

    def _reset(self):
        self._status = RecordStatus.WAIT
        self._recorded_sounds = []
        self._idle_sounds = []


if __name__ == '__main__':
    recorder = LargeSoundActivateRecorder()
    data = recorder.record()
    save_record(data)
