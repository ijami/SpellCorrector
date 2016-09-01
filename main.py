from logic.corrector import Corrector
from logic.dictionary_construction import construct_dictionary_from_persiandict
from logic.language_model_construction import construct_language_model_from_tabnak_collection
from models.dictionary import SCDictionary
from models.language_model import LanguageModel

guide_string = "\n\n*********************** welcome to my spell checker project *****************************\n\n" \
               "Please enter on of choices:\n\n" \
               "1- Construct dictionary\n" \
               "2- Construct language model\n" \
               "3- Correcting a word\n"
number_of_choice = 3

dictionary = SCDictionary()
uodictionary.fetch_from_file()
language_model = LanguageModel(dictionary)
language_model.fetch_from_file()


while True:
    inp = input(guide_string)
    try:
        choice = int(inp)
        if choice < 1 or choice > number_of_choice:
            raise ValueError
    except ValueError:
        print("Your choice was not valid")
        continue

    if choice == 1:
        del dictionary
        dictionary = construct_dictionary_from_persiandict()
    elif choice == 2:
        del language_model
        language_model = construct_language_model_from_tabnak_collection(dictionary)
    elif choice == 3:
        while True:
            input_word = input("Enter a word to correct: (type exit to exit)")
            if input_word == "exit":
                break
            corrector = Corrector(dictionary, language_model)
            print(corrector.correct(input_word))
