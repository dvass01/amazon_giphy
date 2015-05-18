from django.shortcuts import render
from amazon.amazon_wrapper import AMZN

# Create your views here.
def get_dvd_cover_url(request, phrase):
    this_AMZN = AMZN()

    return this_AMZN.get_image(phrase)
