# -*- coding:utf-8 -*-
'''
Created on 2016. 9. 20.

@author: mskim
'''


import urllib
import urllib2


def authentication(url):
    auth_handler = urllib2.HTTPBasicAuthHandler()
    auth_handler.add_password(realm="Basic Authentication", uri=url, user="nips", passwd="nips8144")
    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)
    
def request(url, params, auth=False):
    '''
    @param url: http://203.242.188.230/solr/select
    @param parameters: dict type
    '''
    if auth:
        authentication(url)
    req = urllib2.Request(url, data=urllib.urlencode(params))
    response = urllib2.urlopen(req)
    return response.read()

def search(q):
    url = 'http://solr06.nips.local:8160/solr_kr/simpat'
    res = eval(request(url, params={'wt':'python', 'q':q, 'fq':'pd:[* TO 20110511]'}))
    if res['response']['numFound'] > 0:
        return res['response']['docs']
    else:
        return None