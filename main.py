from logic.dictionary_construction import construct_dictionary_from_persiandict
from models.dictionary import SCDictionary

guide_string = "\n\n*********************** welcome to my spell checker project *****************************\n\n" \
               "Please enter on of choices:\n\n" \
               "1- construct dictionary\n" \
               "2- Fetch dictionary to memory\n"
number_of_choice = 2

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
        construct_dictionary_from_persiandict()
    elif choice == 2:
        dictionary = SCDictionary()
        dictionary.fetch_from_file()
