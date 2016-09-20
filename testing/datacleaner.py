import os
import re

from hazm import word_tokenize
from hazm.Normalizer import Normalizer

from Persian.persianTools import PersianTools


def min_edit_dist(target, source):
    s1 = len(source)
    s2 = len(target)

    d = [[0 for _ in range(s2 + 1)] for _ in range(s1 + 1)]
    for i in range(0, s2 + 1):
        d[0][i] = i
    for i in range(1, s1 + 1):
        d[i][0] = i
        for j in range(1, s2 + 1):
            d[i][j] = min(d[i - 1][j] + 1,
                          d[i][j - 1] + 1,
                          d[i - 1][j - 1] + (1 if source[i - 1] != target[j - 1] else 0))
    return d[s1][s2]


def lcs(line1, line2):
    allowed_min_distance = 2
    s1 = len(line1)
    s2 = len(line2)

    d = [[0 for _ in range(s2 + 1)] for _ in range(s1 + 1)]
    match = [[([], []) for _ in range(s2 + 1)] for _ in range(s1 + 1)]

    for i in range(1, s1 + 1):
        for j in range(1, s2 + 1):
            if min_edit_dist(line1[i - 1], line2[j - 1]) <= allowed_min_distance:
                d[i][j] = d[i - 1][j - 1] + 1
                (m1, m2) = match[i - 1][j - 1]
                match[i][j] = (m1 + [line1[i - 1]], m2 + [line2[j - 1]])
            elif d[i][j - 1] > d[i - 1][j]:
                d[i][j] = d[i][j - 1]
                match[i][j] = match[i][j - 1]
            else:
                d[i][j] = d[i - 1][j]
                match[i][j] = match[i - 1][j]
    return match[s1][s2]


def normalize(line):
    normalizer = Normalizer()
    line = normalizer.normalize(line).replace(PersianTools().HalfSpace, "")
    line = re.sub("([\.»«:،٪\ufeff\u200f/\(\)])", " ", line)
    line = line.replace("  ", " ")
    return line


def clean_data():
    correct_base_path = "data/benchmark/fixed/correct/"
    wrong1_base_path = "data/benchmark/fixed/wrong/"
    dist_base_path = "data/benchmark/test/"
    files_name = os.listdir(correct_base_path)
    c = 0
    for file_name in files_name:
        correct_file_lines = open(correct_base_path + file_name, 'r').readlines()
        wrong_file_lines = open(wrong1_base_path + file_name, 'r').readlines()
        if len(correct_file_lines) != len(wrong_file_lines):
            print("this files is not matche: " + file_name)
            continue
        correct_name = dist_base_path + "c_" + file_name
        wrong_name = dist_base_path + "w_" + file_name
        correct_file = open(correct_name, 'w')
        wrong_file = open(wrong_name, 'w')
        for i in range(0, len(correct_file_lines)):
            correct_line = word_tokenize(normalize(correct_file_lines[i]))
            wrong_line = word_tokenize(normalize(wrong_file_lines[i]))
            correct_match, wrong_match = lcs(correct_line, wrong_line)
            correct_str = ""
            for x in correct_match:
                correct_str += x + " "
            wrong_str = ""
            for x in wrong_match:
                wrong_str += x + " "
            correct_str = correct_str.replace("_", "")
            wrong_str = wrong_str.replace("_", "")
            correct_file.write(correct_str + "\n")
            wrong_file.write(wrong_str + "\n")
