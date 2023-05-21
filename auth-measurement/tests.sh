#!/bin/bash

# sudo apt-get install dnsutils knot-dnsutils

# DNS over UDP/53
dig @9.9.9.9 do53.quad9.fpdns.se
dig @8.8.8.8 do53.quad8.fpdns.se

# DNS over HTTPS
curl "https://dns.quad9.net:5053/dns-query?name=doh.quad9.fpdns.se"
curl "https://dns.google/resolve?name=doh.quad8.fpdns.se"

# DNS over TLS
kdig -d @9.9.9.9 +tls-ca +tls-host=dns.quad9.net dot.quad9.fpdns.se
kdig -d @8.8.8.8 +tls-ca +tls-host=dns.google.com dot.quad8.fpdns.se

