#!/usr/bin/env python3

import requests
import argparse
import subprocess
import scrape_doh_providers


def aux_filter(ip, port):
    return [f"(dst host {ip} and dst port {port}) or",
            f"(src host {ip} and src port {port}) or"]


def filter_format(ipaddr):
    if "." in ipaddr: # IPv4
        if ":" in ipaddr: # Non-default port
            s = ipaddr.split(':')
            return aux_filter(s[0], s[1].replace(':',''))
        else:
            return aux_filter(ipaddr, "443")
    else: # IPv6
        if "]:" in ipaddr: # Non-default port
            ipaddr = ipaddr.replace("]:", "x")
            s = ipaddr.split('x')
            return aux_filter(s[0][1:], s[1].replace(':',''))
        else:
            return aux_filter(ipaddr[1:-1], "443")


def decode_stamp(stamp, prot):
    out = subprocess.check_output(['./dnsstamp_decoder.py', stamp]).decode('UTF-8')
    if prot not in out: # Check for DNSCrypt or DoH
        return None
    for line in out.splitlines():
        if "IP Addr" in line and len(line.split()) > 2:
            return line.split()[2]
    return None


def scrape_dnsstamps(url, prot):
    filter_list = []
    response = requests.get(url)
    for line in response.content.splitlines():
        if line.decode().startswith("sdns"):
            ip = decode_stamp(line.decode(), prot)
            if ip:
                filter_list += filter_format(ip)
    return filter_list


def get_do53():
    return "(port 53) or"

def get_dot():
    return "(tcp port 853) or"

def get_do443(prot):
    do443_filter = []
    if prot == "DoH":
        do443_filter += scrape_doh_providers.get_filter()
    with open(f"do443_dnsstamp_urls.txt", "r") as fp:
        for url in fp.read().splitlines():
            do443_filter += scrape_dnsstamps(url, prot)
    return list(set(do443_filter))


parser = argparse.ArgumentParser()
parser.add_argument('--do53', action='store_true', help='foo')
parser.add_argument('--dot', action='store_true', help='foo')
parser.add_argument('--doh', action='store_true', help='foo')
parser.add_argument('--dnscrypt', action='store_true', help='foo')
args = parser.parse_args()

if not (args.do53 or args.dot or args.doh or args.dnscrypt):
    exit("Missing at least one parameter: --do53, --dot, --doh, --dnscrypt")

tcpdump_filter = []
if args.do53:
    tcpdump_filter.append(get_do53())
if args.dot:
    tcpdump_filter.append(get_dot())
if args.doh:
    tcpdump_filter += get_do443("DoH")
if args.dnscrypt:
    tcpdump_filter += get_do443("DNSCrypt")

print("(")
for i, line in enumerate(tcpdump_filter):
    if i+1 < len(tcpdump_filter):
        print(line)
    else: # remove final "or"
        print(line[:-3])
print(")")
