import requests
import json
import whois
from urllib.parse import urlparse


def load_urls4check():
    with open('./links.txt') as file_handler:
        urls_list = file_handler.readlines()
    return urls_list


def is_server_respond_with_200(url):
    response = requests.get(url)
    print(response.status_code)


def get_domain_name(url):
    parsed_uri = urlparse(url)
    domain_name = parsed_uri.netloc
    return domain_name
    
    

# TODO: change to params
def get_domain_expiration_date(domain_name):
    domain_info = whois.whois('{}'.format(domain_name))
    print(domain_info.expiration_date)


def main():
    url_list = load_urls4check()
    for url in url_list:
        status_code = is_server_respond_with_200(url)
        domain_name = get_domain_name(url)
        exp_date = get_domain_expiration_date(domain_name)


if __name__ == '__main__':
    main()
