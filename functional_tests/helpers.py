import random
from my_dictionary.settings import BASE_DIR

AVAILABLE_WORDS_FILE = BASE_DIR+'/functional_tests/'+'available_words.txt'
USED_WORDS_FILE = BASE_DIR+'/functional_tests/'+'used_words.txt'


def get_random_line_from_file(file):
    with open(file, "r") as available_words:
        words = available_words.readlines()
        selected_word = random.choice(words)
    return selected_word


def append_word_in_file(word, file):
    with open(file, "a") as used_words:
        used_words.write(word)


def delete_word_from_file(word, file):
    with open(file, "r") as available_words:
        words = available_words.readlines()
        words.remove(word)
    with open(file, "w") as available_words:
        available_words.writelines(words)


def set_word_as_used(word):
    delete_word_from_file(word, AVAILABLE_WORDS_FILE)
    append_word_in_file(word, USED_WORDS_FILE)