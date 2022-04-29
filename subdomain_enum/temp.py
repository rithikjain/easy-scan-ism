import requests

def get_sub_domains(domain):
    url = 'https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={}'.format(domain)
    fetch = requests.get(url)

    subdomains = []

    for subdomain in (fetch.json()).get('subdomains'):
        subdomains.append(subdomain)

    print(subdomains)

get_sub_domains("vit.ac.in")
