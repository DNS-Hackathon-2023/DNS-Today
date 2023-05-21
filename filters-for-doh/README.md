# DoH Filters

This is a collection of scripts designed to assist network operators in
observing DNS traffic on their network, even when it is obscured by encryption
protocols like DNS-over-HTTPS (DoH) and DNSCrypt. While traditional DNS and
DNS-over-TLS (DoT) are relatively easy to filter, DoH can hide among normal web
traffic, making it challenging to monitor DNS queries and responses.

This repository provides a solution by generating TCPDump filters based on
online lists of popular DoH and DNSCrypt URLs. By using these filters, network
operators can capture and analyze encrypted DNS traffic, gaining valuable
insights into the DNS activity within their network.

## Generating the filter
The script generate_filter.py uses argparse to let the user specify what the
resulting filter should contain with flags:
- --do53 to filter for traditional DNS traffic over port 53
- --dot to filter for DNS-over-TLS over port 853
- --doh to filter for DNS-over-HTTPS (commonly) over port 443 to known servers
- --dnscrypt to filter for encrypted DNS traffic (commonly) also over port 443 to known servers

These flags can be combined as such:
```
./generate_filter.py --do53 --doh
```

The filter will be printed to stdout and can be redirected to a file:
```
./generate_filter.py --do53 --doh > do53-doh.filter
```

## Running the filter
Simply run tcpdump with the -F flag specifying the filter file:

```
tcpdump -F do53-doh.filter
```
