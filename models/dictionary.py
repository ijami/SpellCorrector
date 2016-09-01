from models.dictionary_normalized import DictionaryNormalized


class SCDictionary(DictionaryNormalized):

    def __init__(self):
        super(SCDictionary, self).__init__()
        self.set = set()
        self.correct_form = {}
        self.dict_path = "dictionary.txt"

    def add(self, word):
        normalized_word = self.dictionary_normalize(word)
        if not word == normalized_word:
            self.correct_form[normalized_word] = word
        self.set.add(normalized_word)

    def size(self):
        return len(self.set)

    def contains(self, word):
        normalized_word = self.dictionary_normalize(word)
        if normalized_word in self.set:
            return True
        return False

    def get(self, word):
        normalized_word = self.dictionary_normalize(word)
        if normalized_word in self.set:
            if normalized_word in self.correct_form:
                return self.correct_form[normalized_word]
            return normalized_word
        return None

    def fetch_from_file(self):
        file = open(self.dict_path, 'r')
        for word in file.read().split():
            self.add(word)

    def export_to_file(self):
        file = open(self.dict_path, 'w')
        for word in self.set:
            file.write(self.get(word) + "\n")


