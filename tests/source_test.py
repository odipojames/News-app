import unittest
from app.models import Source

Source = source.Source


class SourceTest(unittest.TestCase):
    '''
    testing the behaviour of source
    '''
    def setUp(self):
        '''
        method runs before each test
        '''
        self.new_source = Source('abc-news','ABC News', 'blabla blabla', 'en')
    def test_source_instance(self):
        '''
        testing whether the sources instantiate correctly
        '''
        self.assertTrue(isinstance(self.new_source,Source))
    def test_init(self):
        '''
        testing the instance created called new_source
        '''
        self.assertEqual(self.new_source.id, 'abc-news')
        self.assertEqual(self.new_source.name, 'ABC News')
        self.assertEqual(self.new_source.description, 'blabla blabla')
        self.assertEqual(self.new_source.language, 'en')

if __name__ == '__main__':
    unittest.main()
