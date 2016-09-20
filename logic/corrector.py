from Persian.persianTools import PersianTools
from utils.singleton import Singleton


class Corrector(Singleton):

    def __init__(self, dictionary, language_model):
        self.dictionary = dictionary
        self.language_model = language_model


    def edit1(self, word):
        letters = PersianTools().persian_alphabet
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def edit2(self, word):
        return set((e2 for e1 in self.edit1(word) for e2 in self.edit1(e1)))

    def known(self, words):
        return set(w for w in words if self.dictionary.contains(w))

    def condidates(self, word):
        return self.known([word]) or self.known(self.edit1(word)) or self.known(self.edit2(word)) or [word]

    def score_function(self, word):
        return self.language_model.get_score(word)

    def correct(self, word):
        return max(self.condidates(word), key=self.score_function)
