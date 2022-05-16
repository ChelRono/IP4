from app import app
import urllib.request,json

from app.quotes_test import Quotes
from .models import quotes

Quotes = quotes.Quotes

base_url='  http://quotes.stormconsultancy.co.uk/popular.json'

def get_quotes(popular):
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url.format(popular)

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = None

        if get_quotes_response:
            quotes_results_list = get_quotes_response
            quotes_results = process_results(quotes_results_list)


    return quotes_results

def process_results(quotes_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    quotes_results = []
    for quotes_item in quotes_list:
        author = quotes_item.get('author')
        id=quotes_item.get('id')
        quotes = quotes_item.get('quotes')
        
        quotes_object = Quotes(author,id, quotes)
        quotes_results.append(quotes_object)

    return quotes_results
