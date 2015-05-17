import requests
import json
import collections
from collections import defaultdict
import random

class AmGiphy:
    def __init__(self):
        self.search_url = 'http://api.giphy.com/v1/gifs/search?api_key=dc6zaTOxFJmzC&q='


    def gif_search(self, phrase):
        results_array = []
        search_result = requests.get(self.search_url + phrase)
        if search_result.json() != []:
            gif_dict = search_result.json()
            print(gif_dict['data'][0]['images']['original']['url'])
            results_array.append(gif_dict['data'][0]['images']['original']['url'])
            return results_array
        else:
            print('Gif not found.')
            return None

    def get_random_word(self):
        word_dict = [line.strip() for line in open('words')]
        random_word = random.choice(word_dict)
        print(random_word)
        return random_word

gif = AmGiphy()
gif.gif_search(gif.get_random_word())
# gif.get_random_word()
