from app import app
import urllib.request,json
from .models import source

Source = source.Source



# Getting api key
api_key = app.config['NEWS_API_KEY']
