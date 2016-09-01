from Persian.persianTools import PersianTools


class DictionaryNormalized:

    def __init__(self):
        self.persian_tools = PersianTools()

    def dictionary_normalize(self, word):
        if self.persian_tools.HalfSpace in word:
            return word.replace(self.persian_tools.HalfSpace, "")
        return word
