import re

from utils.singleton import Singleton


class PersianTools(Singleton):

    def __init__(self):
        self.HalfSpace = "‌"
        self.persian_regex = re.compile("^[\u0600-\u06FF\uFB8A\u067E\u0686\u06AF\u200C\u200F ]+$")
