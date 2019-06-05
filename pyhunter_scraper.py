from pyhunter import PyHunter
def scrape(domain,api_key):
    hunter = PyHunter(api_key)
    data2 = hunter.domain_search(domain)
    egg = "      "
    for i in range(len(data2['emails'])):
        phone = data2['emails'][i]['phone_number']
        email = data2['emails'][i]['value']
        print(email,egg,phone)
