from pynput import keyboard
from queue import Queue

pressed_chars = Queue()

def on_press(key):
    print('put key {}'.format(key.__dict__.get('char') or key.name))
    pressed_chars.put(key)

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def get_keyboard_listener():
    return keyboard.Listener(on_press=on_press, on_release=on_release)