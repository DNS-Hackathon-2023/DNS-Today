## LAB Overview
![Lab](https://github.com/DNS-Hackathon-2023/DNS-Today/blob/ac452d03af0918691bc80475ad3079a758ed31cc/DNS%20Today%20-%20TinyLab.png?raw=true)

## DNS Testing
in the lab we raised a DNS Server (NS1) that respond to 
53 UDP
53 TCP
443 TCP / DoH
853 TCP / DoT

## Client for testing:
dig - testing 53 tcp/udp
DoH - use dig
DoT - use kdig

## Arikme - L7 Visability
In Addition we raised Akime Server that get's pacap files and visualize the traffic:
url:       http://10.10.12.211:8005/ 
user:      admin 
Password:  admin

Home page 
https://github.com/arkime/arkime/blob/main/README.md
https://arkime.com/architecture

# Data Capture and display
1. on the host - create pipe
mkfifo /home/me/docker/datadump/ns1-pipe.tcpdump
2. on the host tcpdump only ns1 docker
tcpdump -i docker0 -w - host 172.18.0.2 > /home/me/docker/datadump/ns1-pipe.tcpdump
3. on the arkime docker process from the file pipe
docker-compose exec -it arkime /opt/arkime/bin/capture --copy -r /data/pcap/ns1-pipe.tcpdump

all done in containers on k8s-n1 docker host 10.10.12.211

## Additinal stuff / ElastiFlow - L4 Visability
PFSense / Firewall sends IPFIX / Netflow to collector
Using ElastiFlow to analyze L4 headers
