from hazm import word_tokenize

from models.dictionary import SCDictionary
from normalization.normalizer import SCNormalizer


def construct_dictionary_from_persiandict():
    dictionary_file = open("data/persiandict.txt")
    dictionary = SCDictionary()
    normalizer = SCNormalizer()
    for line in dictionary_file:
        words = [x for x in line.split("\t") if (not x.isspace()) and x]
        for not_tokenized_word in words:
            for word in word_tokenize(not_tokenized_word):
                if dictionary.is_valid_word(normalizer.normalize(word)):
                    dictionary.add(word)

    dictionary.export_to_file()
    print(dictionary.size())
    del dictionary

