


class Quotes:
    '''
    Quote class to define Movie Objects
    '''

    def __init__(self,id,author,quote,poster):
        self.author= author
        self.id =id
        self.quote = quote
        self.permalink='http://quotes.stormconsultancy.co.uk/quotes/'+poster
        