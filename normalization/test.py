import json
import re

from hazm import word_tokenize
from hazm.Normalizer import Normalizer

normalizer = Normalizer()
sentence = 'سلام حال همه ‌ی ما خوب است'
normalized = normalizer.normalize(sentence)
print(normalized)

# data_file = open("../Jami/tabnakNewsCollection.json", 'r')
# for line in data_file:
#     data = json.loads(line)
#     for key in data:
#         print(key)
#     break

dictionary_file = open("../Jami/persiandict.txt")
i = 0
persianWordPattern = re.compile("^[\u0600-\u06FF\uFB8A\u067E\u0686\u06AF\u200C\u200F ]+$")
#persianVowels = re.compile()
for line in dictionary_file:
    data = line
    for word in word_tokenize(data):
        if persianWordPattern.match(word):
            pass
    i += 1
    if i == 10:
        break


