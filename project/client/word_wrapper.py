import random
import os


class RandWord:
    def __init__(self):
        pass

    def get_random_word(self):
        word_array = []
        word_array = [line.strip() for line in open('client/words','r')]
        # for word in word_array:
        #     print(word)
        # print()
        random_word = random.choice(word_array)
        return(random_word)

        # for line in open('words'):
        #     lines = lines + 1
        # print(lines)
        # print(randint(1, lines))
if __name__ == '__main__':
    retval = os.getcwd()
    print(retval)

    rand = RandWord()
    rand.get_random_word()
