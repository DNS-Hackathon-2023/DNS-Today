# One-off Active Measurement 
Running NSD w/ dnstap on fpdns.se with wildcard subdomains.
- Select recursive resolver accepting multiple protocols:
    - Quad9: Do53, DoH, DoT
    - Quad8: Do53, DoH, DoT
- Create queries to map them at the authoritative name server

    Do53: 
    ```
    # sudo apt-get install dnsutils
    dig @9.9.9.9 do53.quad9.fpdns.se
    dig @8.8.8.8 do53.quad8.fpdns.se
    ```
    DoH:
    ```
    # sudo apt-get install curl
    curl "https://dns.quad9.net:5053/dns-query?name=doh.quad9.fpdns.se"
    curl "https://dns.google/resolve?name=doh.quad8.fpdns.se"
    ```
    DoT:
    ```
    # sudo apt-get install knot-dnsutils
    kdig -d @9.9.9.9 +tls-ca +tls-host=dns.quad9.net dot.quad9.fpdns.se
    kdig -d @8.8.8.8 +tls-ca +tls-host=dns.google.com dot.quad8.fpdns.se
    ```
- Observe differences in the queries arriving at the authoritative side

## Results
No noticable differences between client usage of protocols as seen from the authoritative side.
