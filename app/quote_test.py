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
        self.new_quote = Quotes('Robert Sewell','41','If Java had true garbage collection, most programs would delete themselves upon execution.','http://quotes.stormconsultancy.co.uk/quotes/41')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quotes))


if __name__ == '__main__':
    unittest.main()