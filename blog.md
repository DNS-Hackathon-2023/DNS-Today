# DNS Today Blog
These are the steps we took, what we tried and what we uncovered. Less formal than the guide.

## Data
We gathered available data for analysis, this included:
- SIDN .nl ccTLD (one day of anonymized auth. name server query data
- todo


## One-off Active Measurements
Running NSD w/ dnstap on fpdns.se with wildcard subdomains.
- Select recursive resolver accepting multiple protocols:
    - Quad9: Do53, DoH, DoT
    - Quad8: Do53, DoH, DoT
- Create queries to map them at the authoritative name server
    - Do53:
        - sudo apt-get install dnsutils
        - dig @9.9.9.9 do53.quad9.fpdns.se
        - dig @8.8.8.8 do53.quad8.fpdns.se
    - DoH:
        - curl "https://dns.quad9.net:5053/dns-query?name=doh.quad9.fpdns.se"
        - curl "https://dns.google/resolve?name=doh.quad8.fpdns.se"
    - DoT:
        - sudo apt-get install knot-dnsutils
        - kdig -d @9.9.9.9 +tls-ca +tls-host=dns.quad9.net dot.quad9.fpdns.se
        - kdig -d @8.8.8.8 +tls-ca +tls-host=dns.google.com dot.quad8.fpdns.se
- Observe differences in the queries arriving at the authoritative side
    - todo
