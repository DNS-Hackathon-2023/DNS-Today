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
- Create queries to map them at the authoritative name server
    - do53.quad9.fpdns.se
    - doh.quad9.fpdns.se
    - dot.quad9.fpdns.se
- Observe differences in the queries arriving at the authoritative side
