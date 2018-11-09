from app import app
import urllib.request,json
from .models import source

Source = source.Source



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
