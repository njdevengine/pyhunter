from pyhunter import PyHunter
from pandas.io.json import json_normalize

def scrape(domain,api_key):
    hunter = PyHunter(api_key)
    data = hunter.domain_search(domain)
    domain = data['domain']
    organization = data['organization']
    df = json_normalize(data['emails'])
