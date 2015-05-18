import requests
import json
import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))

class AmGiphy:
    def __init__(self):
        self.search_url = 'http://api.giphy.com/v1/gifs/search?api_key=dc6zaTOxFJmzC&q='


    def gif_search(self, phrase):
        results_array = []
        print(phrase)
        search_result = requests.get(self.search_url + phrase)
        # print(search_result.json)
        if search_result.json() != []:
            gif_dict = search_result.json()
            try:
                print(gif_dict['data'][0]['images']['original']['url'])
                results_array.append(gif_dict['data'][0]['images']['original']['url'])
                return results_array
            except:
                print("There were no results for your search.")
        else:
            print('Gif not found.')
            return None

    # def get_random_word(self):
    #     word_dict = [line.strip() for line in open('words')]
    #     random_word = random.choice(word_dict)
    #     print(random_word)
    #     return random_word

if __name__ == '__main__':
    # print(os.getcwd())
    from client.word_wrapper import RandWord
    gif = AmGiphy()
    phrase = RandWord()
    gif.gif_search(phrase.get_random_word())

# gif.get_random_word()
