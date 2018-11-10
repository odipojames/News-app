import unittest
from app.models import article

Article = article.Article


class ArticleTest(unittest.TestCase):
    '''
    testing the behaviour of article
    '''
    def setUp(self):
        '''
        runs before each test
        '''
        self.new_article = Article('a','b','c','d','e','f')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
        '''
        testing whether the instances of article are started correctly
        '''
        self.assertEqual(self.new_article.author,'a')
        self.assertEqual(self.new_article.title, 'b')
        self.assertEqual(self.new_article.description, 'c')
        self.assertEqual(self.new_article.url, 'd')
        self.assertEqual(self.new_article.image, 'e')
        self.assertEqual(self.new_article.time, 'f')
