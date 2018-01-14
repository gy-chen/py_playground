from . import get_keyboard_listener

listener = get_keyboard_listener()
with listener:
    listener.join()