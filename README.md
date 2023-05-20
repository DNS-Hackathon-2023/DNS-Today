# DNS-Today
DNS Traffic Monitoring and Classification

Observing/Debugging todays DNS.
A guide for technical users and network operators.

What does DNS traffic look like today?
- Traditional DNS (dst udp/53)
- DNS-over-Encryption
    - DoT (RFC7858: tcp/853 DNS over TLS & udp/853 DNS over DTLS)
    - DoH (RFC8484: tcp/443 HTTP/2 & HTTPS)
    - DoQ (RFC9250: udp/853, possibly udp/443 for stub to recursive)
    - DNSCrypt (draft-denis-dprive-dnscrypt: udp/443 & tcp/443)
    - DNSCurve (udp/53)
- curl list of publicly available DoH servers
    - https://github.com/curl/curl/wiki/DNS-over-HTTPS#publicly-available-servers
    - parser for the above: https://gist.github.com/kimbo/dd65d539970e3a28a10628f15398247b
- DNSCrypt list of publicly available DNSCrypt and DoH servers
    - https://raw.githubusercontent.com/DNSCrypt/dnscrypt-resolvers/master/v3/odoh-relays.md
    - https://raw.githubusercontent.com/DNSCrypt/dnscrypt-resolvers/master/v3/odoh-servers.md
    - https://raw.githubusercontent.com/DNSCrypt/dnscrypt-resolvers/master/v3/onion-services.md
    - https://raw.githubusercontent.com/DNSCrypt/dnscrypt-resolvers/master/v3/opennic.md
    - https://raw.githubusercontent.com/DNSCrypt/dnscrypt-resolvers/master/v3/parental-control.md
    - https://raw.githubusercontent.com/DNSCrypt/dnscrypt-resolvers/master/v3/public-resolvers.md
    - https://raw.githubusercontent.com/DNSCrypt/dnscrypt-resolvers/master/v3/relays.md
    - https://raw.githubusercontent.com/DNSCrypt/dnscrypt-resolvers/master/v2/onion-services.md
    - https://raw.githubusercontent.com/DNSCrypt/dnscrypt-resolvers/master/v2/opennic.md
    - https://raw.githubusercontent.com/DNSCrypt/dnscrypt-resolvers/master/v2/parental-control.md
    - https://raw.githubusercontent.com/DNSCrypt/dnscrypt-resolvers/master/v2/public-resolvers.md
    - https://raw.githubusercontent.com/DNSCrypt/dnscrypt-resolvers/master/v2/relays.md
    - https://raw.githubusercontent.com/DNSCrypt/dnscrypt-resolvers/master/v1/dnscrypt-resolvers.csv
    - parsing the above: https://github.com/DNSCrypt/dnscrypt-proxy/wiki/stamps
- What common user OS/apps create what kinds of traffic?
- Detecting security anomalies? (flow data)
- How can technical end users find out how their DNS resolution is happening?

1. Create git repo (DONE)
2. Get data to analyze
    - SIDN
3. Writing guide in parallel (blog style?)

