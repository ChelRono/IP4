from random import random
from app import app
import urllib.request,json


from app.quotes_test import Quotes
from .models import quotes

Quotes = quotes.Quotes

base_url='  http://quotes.stormconsultancy.co.uk/popular.json'



def get_quotes(id):
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url.format(id)

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
        quote = quotes_item.get('quote')
        author = quotes_item.get('author')

        
        
        
        quotes_object = Quotes( quote,author)
        quotes_results.append(quotes_object)

    return quotes_results

def get_quote(quote):
    get_quotes_details_url = base_url.format(quote)

    with urllib.request.urlopen(get_quotes_details_url) as url:
        quotes_details_data = url.read()
        quotes_details_response = json.loads(quotes_details_data)

        quotes_object = None
        if quotes_details_response:
            id = quotes_details_response.get('id')
            author = quotes_details_response.get('author')
            quote = quotes_details_response.get('quote')
            permalink = quotes_details_response.get('permalink')
            

            quotes_object = Quotes(id,author,quote,permalink)

    return quotes_object

