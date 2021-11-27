import random

import string

from dictionary_loader import DictLoader


# def cleanup(word):
#     undesirables = "[ ],'"
#     my_list = list(word)
#     for char in my_list:
#         if char in undesirables:
#             my_list.remove(char)
#     new_word = ''.join(my_list)
#     return new_word


if __name__ == '__main__':
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)
    dicter = DictLoader()
    dicter.create_dictionary_file('a')
    dicter.create_dictionary_file('n')

    noun = dicter.load_dict_file('noun', "n")
    adjective = dicter.load_dict_file('adjective', "a")

    password_elements = (str(number), str(special_char), noun, adjective)
    shuffled = list(password_elements)
    random.shuffle(shuffled)
    shuffled = ''.join(shuffled)
    shuffled = shuffled
    print(f"password with easy version: {shuffled}")
    print(f"how come this is easy to remember?! \n{''.join(random.choice((str.upper, str.lower))(c) for c in shuffled)}")

#
    # password = f"{adjective}{noun}{str(number)}{special_char}"
    # password = cleanup(password)
    # print(f"without shuffling elements: {''.join(random.choice((str.upper, str.lower))(c) for c in password)}")
    # print(f"your new password is: {password}")
#    check passwords with https://www.passwordmonster.com/
