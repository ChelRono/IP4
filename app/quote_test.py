import unittest
from app.models import quotes
Quotes = quotes.Quotes

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Quote class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quotes(39,'Bjarne Stroustrup','In C++ it\u2019s harder to shoot yourself in the foot, but when you do, you blow off your whole leg.','"http://quotes.stormconsultancy.co.uk/quotes/"}')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quotes))


if __name__ == '__main__':
    unittest.main()