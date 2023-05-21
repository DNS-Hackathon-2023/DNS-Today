#!/bin/bash

# sudo apt-get install dnsutils knot-dnsutils
TESTDNSSERVER=10.10.12.211
TESTDOMAINNAME=do53.quad9.fpdns.se
DNSDOHPORT=443
DNSDOTPORT=853

# DNS over UDP/53
echo "- testing [UDP/53] to [${TESTDNSSERVER}] with domain [${TESTDOMAINNAME}]"
dig @${TESTDNSSERVER} ${TESTDOMAINNAME}
# DNS over TCP/53
echo "- testing [TCP/53] to [${TESTDNSSERVER}] with domain [${TESTDOMAINNAME}]"
dig @${TESTDNSSERVER} ${TESTDOMAINNAME} +tcp

# DNS over HTTPS
echo "- testing [DOH TCP/${DNSDOHPORT}] to [${TESTDNSSERVER}] with domain [${TESTDOMAINNAME}]"
curl -ki "https://${TESTDNSSERVER}:${DNSDOHPORT}/dns-query?name=${TESTDOMAINNAME}"
#curl "https://dns.google/resolve?name=doh.quad8.fpdns.se"

# DNS over TLS
echo "- testing [DOT TCP/${DNSDOTPORT}] to [${TESTDNSSERVER}] with domain [${TESTDOMAINNAME}]"
kdig -d @${TESTDNSSERVER} +tls-ca +tls-host=${TESTDNSSERVER} ${TESTDOMAINNAME}

