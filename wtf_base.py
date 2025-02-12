# Wiki Tele Foo Base Classes
#
# SUBJECT: Consuming wiki* resources
#
# AUTHOR: Sven Schrodt<sven@schrodt.club>
# SINCE: 2025-02-12
import requests
import urllib

class WTFHttpClient:
    response = None
    headers = {'User-Agent': 'Wiki Tele Foo Http Client; Version 0.23.42',
               'X-POST_FUCKUP': 'Http is down().debug()'}
    
    def __init__(self):
        pass
    
    def get(self, uri):
        return requests.get(uri, headers=self.headers)
        #url = 'https://de.wiktionary.org/w/api.php?action=query&list=search&srsearch=Fubar&format=json'
    


 

class WTFQueryBuilder:
    """ Building URIs to different Wiki* endpoints """
    format = 'json'
    language = 'de'
    endpoint = 'https://www.wikidata.org/w/api.php'
    
    # TODO: managing different URIs
    base_uri = 'https://{}.wiktionary.org/w/api.php?action={}&list=search&srsearch={}&format={}' # to be used by str.format()
    
    def __init__(self, search='Foo'):
       self.search = search
       self.__init_vars(action = 'query', format = self.format, language = self.language, search = 'Foo',  endpoint = self.endpoint)
    
    def build_query_generic(self, lemma: str, action: str = 'query', format: str = 'json', search: str = 'Foo',  endpoint: str = 'https://www.wikidata.org/w/api.php')->str:
        self.__set_vars(action = action, search = lemma,  endpoint = 'https://www.wikidata.org/w/api.php')
        return self.endpoint + '?' + urllib.parse.urlencode(self.params)
    
    def search_entities(self, lemma: str):  
        return self.build_query_generic(lemma = lemma, action ='wbsearchentities')
    
    def __set_vars(self, **kwargs):
        #__set_vars(action = action, search = lemma,  endpoint = 'https://www.wikidata.org/w/api.php')
        for key in kwargs:
            if key != 'endpoint':
                self.params[key] = kwargs[key]
    
    def __init_vars(self, **kwargs):
       
        self.params = {
            'action': kwargs['action'],
            'format': kwargs['format'],
            'language': kwargs['language'],
            'search': kwargs['search']
        }
        self.endpoint = kwargs['endpoint']
        # wbsearchentities
    
# lemma = 'Universum'

#qb = WTFQueryBuilder()
# uri = qb.build_full_query(lemma)
#uri = qb.search_entities('Orthopädie')
#print(uri)
#exit()
# client = WTFHttpClient()
# response = client.get(uri).json()
# print(response)
 
# action = 'query', format = 'json', language = 'de', search= 'Foo'