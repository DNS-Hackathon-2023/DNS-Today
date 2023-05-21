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
    - [curl list of publicly available DoH servers](https://github.com/curl/curl/wiki/DNS-over-HTTPS)
    - [DNSCrypt list of publicly available DNSCrypt and DoH servers](https://github.com/DNSCrypt/dnscrypt-resolvers)
- For network operators - processing sFlow data
    - use filter to only process DNS related traffic (udp/53 or tcp/853 or udp/853 or specific ip&port of public resolvers from lists above)
    - anonymise customer IPs (modify https://github.com/phaag/nfdump/blob/master/src/nfanon/nfanon.c)
- What common user OS/apps create what kinds of traffic?
- Detecting security anomalies? (flow data)
- How can technical end users find out how their DNS resolution is happening?

1. Create git repo (DONE)
2. Get data to analyze
    - SIDN
3. Writing guide in parallel (blog style?)

