## internal imports
from subdomain_enum.crt_sh import crt_sh
from subdomain_enum.threatcrowd import threatcrowd

total_subdomains = set()

def get_subdomains(domain):
    try:
        for subdomain in crt_sh(domain):
            total_subdomains.add(subdomain)
        print('[+] Subdomain Enumeration via crt.sh completed successfully')
    except Exception as e:
        print('[!] Failed to fetch Subdomains from cert.sh')
        print('[!] {}'.format(str(e)))

    try:
        for subdomain in threatcrowd(domain):
            total_subdomains.add(subdomain)
        print('[+] Subdomain Enumeration via threatcrowd completed successfully')
    except Exception as e:
        print('[!] Failed to fetch Subdomains from threatcrowd')
        print('[!] {}'.format(str(e)))

    with open('temp_db/subdomains.txt', 'w') as f:
        f.truncate(0)
        for subdomain in total_subdomains:
            f.write(subdomain)
            f.write('\n')

    return total_subdomains
