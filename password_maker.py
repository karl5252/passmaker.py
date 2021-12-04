import random
import string
from dictionary_loader import DictLoader


class PasswordMaker:
    def __init__(self):
        self.number = 0
        self.special_char = ''
        self.noun = ""
        self.adjective = ""

    def _get_dict(self):
        self.number = random.randrange(0, 100)
        self.special_char = random.choice(string.punctuation)
        self.dictLoad = DictLoader()
        self.dictLoad.create_dictionary_file('a')
        self.dictLoad.create_dictionary_file('n')
        self.noun = self.dictLoad.load_dict_file('noun', "n")
        self.adjective = self.dictLoad.load_dict_file('adjective', "a")
        password_elements = (str(self.number), str(self.special_char), self.noun, self.adjective)
        return password_elements

    def ret_pass(self, max_length=30):
        while True:
            password_elements = self._get_dict()
            pass_length = len(''.join(password_elements))
            if pass_length <= max_length:
                break
        shuffled = list(password_elements)
        random.shuffle(shuffled)
        shuffled = ''.join(shuffled)
        shuffled = shuffled
        return f"{''.join(random.choice((str.upper, str.lower))(c) for c in shuffled)}"
