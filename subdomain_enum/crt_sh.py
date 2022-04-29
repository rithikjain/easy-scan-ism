import requests
import bs4
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BeautifulSoup = bs4.BeautifulSoup

def crt_sh(domain):
    query = 'https://crt.sh/?q={}'.format(domain)
    fetch = requests.get(query)
    soup = BeautifulSoup(fetch.text, 'html.parser')
    subdomains = set()

    tables = soup.find_all('table')
    table_with_subdomains = tables[1]
    rows = table_with_subdomains.find_all('tr')
    
    for row in rows[2:]:
        columns = row.find_all('td')
    
        total = []
        for x in columns:
            if (x.get('style')==None) and (x.find_all('a') == []):
                total.append(x)
        subdomains_only_column = total[-1]
        for subdomain in subdomains_only_column:
            if type(subdomain) == bs4.element.NavigableString:
                subdomains.add(subdomain)
    
    subdomain_list = list(subdomains)

    return subdomain_list