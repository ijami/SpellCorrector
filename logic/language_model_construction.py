import json

from hazm import word_tokenize

from Persian.persianTools import PersianTools
from models.language_model import LanguageModel
from normalization.normalizer import SCNormalizer


def construct_language_model_from_tabnak_collection(dictionary):
    file = open("data/tabnakNewsCollection.json", 'r')
    normalizer = SCNormalizer()
    language_model = LanguageModel(dictionary)
    i = 0
    for line in file:
        try:
            data = json.loads(line)
            content = data['title'] + " " + data['content']
            normalized_content = normalizer.normalize(content)
            word_tokenized = word_tokenize(normalized_content)
            for word in word_tokenized:
                word = word.replace("_", PersianTools().HalfSpace)
                language_model.add(word)
            i += 1
            if i % 1000 == 0:
                print(i)
        except:
            print("error accured reading json file")
    language_model.export_to_file()
    return language_model
