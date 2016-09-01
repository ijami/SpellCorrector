import re

from utils.singleton import Singleton


class PersianTools(Singleton):

    def __init__(self):
        self.HalfSpace = "‌"
        self.persian_regex = re.compile("^[\u200C\u200Fاًءاآأبپتثجچحخدذرزژسشصضطظعغفقکگلمنوؤهیئ]+$")
        self.persian_alphabet = 'اًءاآأبپتثجچحخدذرزژسشصضطظعغفقکگلمنوؤهیئ'

    def is_valid_persian_word(self, word):
        return self.persian_regex.match(word)
