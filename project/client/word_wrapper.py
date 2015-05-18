import random
from random import randint

class RandWord:
    def __init__(self):
        pass

    def get_random_word(self):
        word_array = []
        word_array = [line.strip() for line in open('words','r')]
        # for word in word_array:
        #     print(word)
        # print()
        random_word = random.choice(word_array)
        # print(random_word)
        return(random_word)

        # for line in open('words'):
        #     lines = lines + 1
        # print(lines)
        # print(randint(1, lines))

rand = RandWord()
rand.get_random_word()
