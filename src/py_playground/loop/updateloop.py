#coding: utf-8
import threading
import time
import traceback
from py_playground.win32 import power


class ACLineUpdateLoop(threading.Thread):

    SLEEP_TIME = 2

    def __init__(self):
        super().__init__()
        self._callback = None
        self._previous_acline_status = None

    @property
    def callback(self):
        return self._callback

    @callback.setter
    def callback(self, callback):
        self._callback = callback

    def run(self):
        while 1:
            try:
                power_status = power.SYSTEM_POWER_STATUS()
                power.GetSystemPowerStatus(power_status)
                if self._previous_acline_status is not None and power_status.ACLineStatus != self._previous_acline_status:
                    self._callback(power_status.ACLineStatus)
                self._previous_acline_status = power_status.ACLineStatus
                time.sleep(self.SLEEP_TIME)
            except:
                traceback.print_exc()
                return

if __name__ == '__main__':
    l1 = ACLineUpdateLoop()
    l1.daemon = True
    l1.callback = lambda x: print('AC status changed:', x)
    l1.start()
    l1.join()