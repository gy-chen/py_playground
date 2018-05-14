import signal
import os
import logging


def exit_program(signal_number, current_stack_frame):
    logging.debug('signal_number: %s' % signal_number)
    logging.debug('current stack frame: %s' % current_stack_frame)
    logging.info('Exit the program')
    os._exit(0)


def set_exit_handler(signal_number=signal.SIGINT):
    logging.debug('Setup exit handler')
    signal.signal(signal_number, exit_program)
