from django.shortcuts import render, HttpResponse
import urllib
#from urllib import urlopen
FACEBOOK_APP_ID = '1561949917396242'
FACEBOOK_API_SECRET = 'f4e881cb2b6400365d8e85fa88e2ab2d'
import urllib2
import requests


def status(request):

    at = 'CAAWMlc37vRIBAE6Dp5YAs0m4rwAtGaxzKh9mBVq7zg7dXOmvkmrreQMZBRY4WUIQkluttWvZBzkw73dg5Hh6OM35vqVXEj1TFQ77GP7H9lvZBBtUk0hRdH6nGM5bkPCTtMZAfod0DCsedcY1gktr02psAbdepXi2bYZB1SKE1sVNP4ZBXmHxB9JHKeASB5XSd9L2eoNhmNfIs1wBoM705CnfMaFFil9GIZD'
    post_data = [('message', 'lop'), ('access_token', at)]     # a sequence of two element tuples
    urldata = urllib.urlencode(post_data)
    #urlget = 'http://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=FACEBOOK_APP_ID&client_secret=FACEBOOK_API_SECRET&fb_exchange_token=at'
    url1 = 'https://graph.facebook.com/me/feed'
    result = urllib.urlopen(url1, urldata)
    #res = urllib2.urlopen(urlget)
    res = requests.get("https://graph.facebook.com/oauth/access_token",
              params={'grant_type': 'fb_exchange_token', 'client_id': FACEBOOK_APP_ID, 'client_secret': FACEBOOK_API_SECRET, 'fb_exchange_token': at})
    #con = res.read()
    content = result.read()
    return HttpResponse(content)
    #return HttpResponse(res)



