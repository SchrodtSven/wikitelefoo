 # Wiki Tele Foo

 Consuming Wiki* resources with Python 3.12+


 ## Usage
 ```python
from wtf_base import WTFQueryBuilder, WTFHttpClient
    
lemma = 'Universum'

qb = WTFQueryBuilder()
uri = qb.build_full_query(lemma)
uri = qb.search_entities('Orthopädie')
print(uri)

client = WTFHttpClient()
response = client.get(uri).json()
print(response)
 
# action = 'query', format = 'json', language = 'de', search= 'Foo'
 ```


 ## Setting up venv, activate it and opt. upgrade pip
 ```bash
svenschrodt@Thanos wikitelefoo % python3 -m venv .venv
svenschrodt@Thanos wikitelefoo % source .venv/bin/activate
(.venv) svenschrodt@Thanos wikitelefoo % 
(.venv) svenschrodt@Thanos wikitelefoo % pip install r- requirements.txt 
(.venv) svenschrodt@Thanos wikitelefoo % pip install --upgrade pip
 ```