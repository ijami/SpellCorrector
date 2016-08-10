from Persian.persianConstants import PersianTools


class SCDictionary:

    def __init__(self):
        self.set = set()
        self.correct_form = {}
        self.persian_tools = PersianTools()
        self.dict_path = "dictionary.txt"

    def add(self, word):
        dict_word, correct = self.dictionary_normalize(word)
        if not dict_word == correct:
            self.correct_form[dict_word] = correct
        self.set.add(dict_word)

    def size(self):
        return len(self.set)

    def is_valid_word(self, word):
        return self.persian_tools.persian_regex.match(word)

    def contains(self, word):
        if word in self.set:
            return True
        return False

    def get(self, word):
        if word in self.set:
            if word in self.correct_form:
                return self.correct_form[word]
            return word
        return None

    def fetch_from_file(self):
        file = open(self.dict_path, 'r')
        for line in file.readlines():
            self.add(line)

    def export_to_file(self):
        file = open(self.dict_path, 'w')
        for word in self.set:
            file.write(word + "\n")

    def dictionary_normalize(self, word):
        if "‌" in word:
            return word.replace(self.persian_tools.HalfSpace, ""), word
        return word, word
