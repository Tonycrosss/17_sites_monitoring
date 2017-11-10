import requests
import whois
import datetime
import argparse
from urllib.parse import urlparse


def load_urls4check(filepath):
    with open(filepath) as file_handler:
        urls_list = file_handler.readlines()
    return urls_list


def is_server_respond_with_200(url):
    response = requests.get(url)
    status_code = response.status_code
    return True if status_code == 200 else False


def get_domain_name(url):
    parsed_uri = urlparse(url)
    domain_name = parsed_uri.netloc
    return domain_name


def paid_time_status(exp_date):
    current_date = datetime.datetime.now()
    exp_date_month_ago = exp_date - datetime.timedelta(days=30)
    return bool(current_date < exp_date_month_ago)


def pretty_output(url, status_code, exp_status):
    print('-' * 50)
    print('Информация по сайту - {}'.format(url))
    print('Сайт отвечает на запрос статусом HTTP 200?: {}'.format(status_code))
    if exp_status:
        print('Сайт проплачен более чем на месяц')
    else:
        print('Сайт проплачен менее чем на месяц')
    print('-' * 50)


def get_domain_expiration_date(domain_name):
    domain_info = whois.whois('{}'.format(domain_name))
    if isinstance(domain_info.expiration_date, list):
        domain_expiration_date = domain_info.expiration_date[0]
    else:
        domain_expiration_date = domain_info.expiration_date
    return domain_expiration_date


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--filepath', type=str,
                        help='Enter the filepath, where data will be stored',
                        required=True)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    filepath = args.filepath
    url_list = load_urls4check(filepath)
    for url in url_list:
        status_code = is_server_respond_with_200(url)
        domain_name = get_domain_name(url)
        exp_date = get_domain_expiration_date(domain_name)
        exp_status = paid_time_status(exp_date)
        pretty_output(url, status_code, exp_status)


if __name__ == '__main__':
    main()
