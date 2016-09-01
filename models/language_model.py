from models.dictionary_normalized import DictionaryNormalized


class LanguageModel(DictionaryNormalized):

    def __init__(self, dictionary):
        super(LanguageModel, self).__init__()
        self.dictionary = dictionary
        self.model = {}
        self.language_model_path = "language_model.txt"

    def add(self, word):
        if self.dictionary.contains(word):
            normalized_word = self.dictionary_normalize(word)
            if normalized_word in self.model:
                self.model[normalized_word] += 1
            else:
                self.model[normalized_word] = 1

    def get_number(self, word):
        normalized_word = self.dictionary_normalize(word)
        if normalized_word in self.model:
            return self.model[normalized_word]

    def get_score(self, word):
        normalized_word = self.dictionary_normalize(word)
        smoothness = 0
        if normalized_word in self.model:
            return self.model[normalized_word] + smoothness
        else:
            return smoothness

    def export_to_file(self):
        file = open(self.language_model_path, 'w')
        for word in self.model:
            file.write(word + " " + str(self.model[word]) + "\n")

    def fetch_from_file(self):
        file = open(self.language_model_path, 'r')
        for line in file.readlines():
            sp = line.split(" ")
            word = sp[0]
            count = int(sp[1])
            self.model[word] = count
