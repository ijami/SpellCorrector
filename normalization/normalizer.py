from hazm.Normalizer import Normalizer


class SCNormalizer:

    def __init__(self):
        self.normalizer = Normalizer()

    def normalize(self, word):
        return self.normalizer.normalize(word)
