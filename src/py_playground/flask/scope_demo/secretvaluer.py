#coding: utf-8
import random

class SecretValuer:

    _instance = None

    def __init__(self):
        self._secret_value = 4413

    def get_secret_value(self):
        return self._secret_value

    def generate_secret_value(self):
        self._secret_value = random.randint(0, 9999)

singleton = SecretValuer()