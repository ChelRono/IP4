from app import app
import urllib.request,json
from .models import quotes


Quotes = quotes.Quotes

# Getting the movie base url
base_url = app.config["QUOTE_URL"]

def get_quotes(category):
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url.format(category)

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
        quotes_list: A list of dictionaries that contain quote details

    Returns :
        quote_results: A list of quote objects
    '''
    quotes_results = []
    for quotes_item in quotes_list:
        id = quotes_item.get('id')
        author= quotes_item.get('author')
        quote = quotes_item.get('quote')
        poster=quotes_item.get('poster')
        

        if poster:
            quotes_object =Quotes (id,author,quote)
            quotes_results.append(quotes_object)

    return quotes_results
