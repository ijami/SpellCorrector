import os


def test(corrector):
    correct_base_path = "data/benchmark/test/c/"
    wrong_base_bath = "data/benchmark/test/w/"
    sum = 0
    good = 0
    correct_files_name = os.listdir(correct_base_path)
    for correct_file_name in correct_files_name:
        wrong_file_name = "w" + correct_file_name[1:]
        correct_lines = open(correct_base_path + correct_file_name).readlines()
        print(wrong_file_name)
        wrong_lines = open(wrong_base_bath + wrong_file_name).readlines()
        for i in range(0, len(wrong_lines)):
            correct_words = correct_lines[i][0:-2].split(" ")
            wrong_words = wrong_lines[i][0:-2].split(" ")
            for j in range(0, len(wrong_words)):
                if correct_words[j] == wrong_words[j]:
                    continue
                correct = corrector.correct(wrong_words[j])
                sum += 1
                print("wrong word: " + wrong_words[j])
                print("recommended: " + correct)
                print("expected: " + correct_words[j])
                print("******************************************")
                if correct == correct_words[j]:
                    good += 1
    print("evaluation finished: ")
    print("number of correction: " + str(sum))
    print("number of good correction: " + str(good))
    print("number of bad correction: " + str(sum - good))
    print("percentage: %" + str(100.0 * good / sum))
