# from app import app
import urllib.request,json
from .models import source,article

Source = source.Source
Article = article.Article


# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the NEWS base url
source_url = app.config["NEWS_SOURCES_URL"]

#getting the json file
def get_source():
    '''
    function to get the json response for the request made
    '''
    get_source_url = source_url.format(api_key)
    print (get_source_url)

    with urllib.request.urlopen(get_source_url)as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)

    return source_results


def process_results(source_list):
    '''
    function to transform the source results into objects
    '''
    source_results = []
    for source in source_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        language = source.get('language')

        if name:
            source_object =  Source(id,name,description,language)
            source_results.append(source_object)

    return source_results



def get_article(id):
    '''
    function to return response to the article json
    '''
    get_article_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_articles(article_results_list)

    return article_results

      #processing the article json
def process_articles(article_list):
    '''
    function to convert the article result into objects
    '''
    article_results = []
    for article in article_list:
        author = article.get('author')
        title = article.get ('title')
        description = article.get('description')
        url = article.get('url')
        image = article.get('urlToImage')
        time = article.get('publishedAt')

        if title:
            article_object = Article(author,title,description,url,image,time)
            article_results.append(article_object)

    return article_results

def get_category(name):
    '''
    function that gets the response to the category json
    '''
    get_category_url = 'https://newsapi.org/v2/everything?q={}&sortBy=relevancy&apiKey={}'.format(name,api_key)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_cartegory_response = json.loads(get_category_data)

        get_cartegory_results = None

        if get_cartegory_response['articles']:
            get_cartegory_list = get_cartegory_response['articles']
            get_cartegory_results = process_articles(get_cartegory_list)

    return get_cartegory_results



# def search_article(source_name):
#     search_article_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
#     with urllib.request.urlopen(search_article_url) as url:
#         search_article_data = url.read()
#         search_article_response = json.loads(search_article_data)
#
#         search_article_results = None
#
#         if search_article_response['sources']:
#             search_article_list = search_article_response['sources']
#             search_article_results = process_results(search_article_list)
#
#
#     return search_article_results
