#!/usr/bin/env python3

#
# Scrape Doh provider URLs from Curl's DNS-over-HTTPS wiki (https://raw.githubusercontent.com/wiki/curl/curl/DNS-over-HTTPS).
# Extended for DNS Hackathon 2023 Rotterdam

import re
import urllib.request
import dns.resolver
from tqdm import tqdm

HTTPS_URL_RE = re.compile(r'https://'
                          r'(?P<hostname>[0-9a-zA-Z._~-]+)'
                          r'(?P<port>:[0-9]+)?'
                          r'(?P<path>[0-9a-zA-Z._~/-]+)?')

PROVIDER_RE = re.compile(r'(\[([^\]]+)\]\(([^)]+))\)|(.*)')

# URLs that are not Doh URLs
do_not_include = ['my.nextdns.io', 'blog.cloudflare.com', 'https://blog.cloudflare.com/welcome-hidden-resolver', 'https://my.nextdns.io/start']


def get_doh_providers():
    found_table = False
    with urllib.request.urlopen('https://raw.githubusercontent.com/wiki/curl/curl/DNS-over-HTTPS.md') as fp:
        for line in fp:
            line = line.decode()
            if line.startswith('|'):
                if not found_table:
                    found_table = True
                    continue
                cols = line.split('|')
                provider_col = cols[1].strip()
                website = None
                provider_name = None
                matches = PROVIDER_RE.findall(provider_col)
                if matches[0][3] != '':
                    provider_name = matches[0][3]
                if matches[0][1] != '':
                    provider_name = matches[0][1]
                if matches[0][2] != '':
                    website = matches[0][2]
                if provider_name is not None:
                    provider_name = re.sub(r'([^[]+)\s?(.*)', r'\1', provider_name)
                    while provider_name[-1] == ' ':
                        provider_name = provider_name[:-1]
                if len(cols) < 3:
                    continue
                url_col = cols[2]
                doh_url_matches = HTTPS_URL_RE.findall(url_col)
                if len(doh_url_matches) == 0:
                    continue
                else:
                    for doh_url in doh_url_matches:
                        if doh_url[0] in do_not_include:
                            continue
                        yield {
                            'name': provider_name,
                            'website': website,
                            'url': 'https://{}{}{}'.format(doh_url[0], ':{}'.format(doh_url[1]) if len(doh_url[1]) != 0 else '', doh_url[2]),
                            'hostname': doh_url[0],
                            'port': doh_url[1] if len(doh_url[1]) != 0 else '443',
                            'path': doh_url[2],
                        }
            if found_table and line.startswith('#'):
                break
    return


def query(name):
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = ["1.1.1.1"]
    try:
        return resolver.resolve(name, "A")
    except:
        return None


def filter_format(ip, port):
    return [f"(dst host {ip} and dst port {port}) or",\
            f"(src host {ip} and src port {port}) or"]


def get_filter():
    filter_list = []
    for o in tqdm(get_doh_providers()):
        answers = query(o['hostname'])
        if answers:
            for answer in answers:
                filter_list += filter_format(answer.to_text(), o['port'].replace(':',''))
    return list(set(filter_list))

