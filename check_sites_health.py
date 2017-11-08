import requests


def load_urls4check():
    with open('./links.txt') as file_handler:
        urls_list = file_handler.readlines()
    return urls_list


def is_server_respond_with_200(url):
    response = requests.get(url)
    print(response)

def get_domain_expiration_date(domain_name):
    pass


def main():
    url_list = load_urls4check()
    for url in url_list:
        is_server_respond_with_200(url)


if __name__ == '__main__':
    main()
