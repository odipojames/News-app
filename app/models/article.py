class Article:
    '''
    class to define each article object
    '''
    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = urlToImage
        self.time = publishedAt
