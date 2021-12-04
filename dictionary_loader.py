import os
from nltk.corpus import wordnet
import random
from os.path import exists


class DictLoader:
    ROOT_DIR = ''

    def __init__(self):
        self.ROOT_DIR = os.path.abspath(os.curdir)

    def check_if_file_exists(self, filename):
        """:param filename: name of the searched file
        :return TRUE or FALSE if file is not found"""
        path_to_file = f"{self.ROOT_DIR}/dict_{filename}.txt"
        file_exists = exists(path_to_file)
        return file_exists

    def create_dictionary_file(self, type_of_dict):
        """:param type_of_dict: holds the type of dictionary. it has to be either 'a' or 'n' """
        if type_of_dict == "a":
            file_name = 'adjective'
        else:
            file_name = 'noun'

        if not self.check_if_file_exists(file_name):
            file = open(f'dict_{file_name}.txt', 'a+')
            for synset in wordnet.all_synsets(f'{type_of_dict}'):
                # temp.extend(synset.lemma_names())
                file.writelines(synset.lemma_names())
                file.write(',')
            file.close()

    def rawcount(self, filename):
        f = open(filename, 'rb')
        lines = 0
        buf_size = 1024 * 1024
        read_f = f.raw.read

        buf = read_f(buf_size)
        while buf:
            lines += buf.count(b'\n')
            buf = read_f(buf_size)

        return lines

    def load_dict_file(self, filename, type_of_dict):
        if type_of_dict == 'a':
            temp_word = random.choice(open(f"{self.ROOT_DIR}/dict_{filename}.txt", "r").readline().split(","))
        elif type_of_dict == 'n':
            temp_word = random.choice(open(f"{self.ROOT_DIR}/dict_{filename}.txt", "r").readline().split(","))
        else:
            raise Exception(f"{type_of_dict} is not valid parameter. accepted parms are 'a' (adjective) or 'n' (noun) ")
        return temp_word.strip()
