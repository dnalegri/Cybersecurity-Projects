## Scenario 

The SOC received an alert in their SIEM for ‘Local to Local Port Scanning’ where an internal private IP began scanning another internal system. 
## Objective
Investigate the network activity and determine if the activity is malicious.

### Skills Learned

- Understanding of network protocols (TCP/IP, UDP, HTTP, HTTPS, DNS, SMTP, etc.)
- Use of network analysis tools (Wireshark)
- Recognizing signs of malicious activity (unusual IP addresses, unexpected ports, anomalous traffic patterns)
- Correlating packet data with other security events or logs (firewall logs, SIEM alerts)

### Tools Used
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaI0kHcffdn_K0v5v1t1diINym7CLhPKIHtw&s" />

- VMware Workstation (Kali Linux)
- [Wireshark](https://www.wireshark.org/)
- [BTLO pcap file](https://blueteamlabs.online/home/challenge/network-analysis-web-shell-d4d3a2821b)


# Investigation & Analysis

## *Important Settings*

<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/33059922-794c-4139-8dbf-bf87d7481619" width:200 />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/74269d20-5fd2-4595-8ebb-f1884959f022" width:200 />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/c4198d61-73ee-4595-aedb-7bdda5327ef8" width:200 />

## *Start*
After configuring settings, I opened the file properties to view the time this scan took place, for how long traffic was recorded, and the OS and version used. This isn't a necessary step however if you were receiving this file from a client, you could verify the time and date of the incident by using the information given in the file. Time is valuable and making sure the correct file was sent over before investigating is crucial.

- After configuring these settings, I went to the *Protocol Hierarchy* tab in settings. By viewing the protocols used in this file without diving in quite yet, I can see that based on some of these protocols, for example, HTTP, that is unencrypted traffic and I will be able to read the exchange.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/09a1981f-1b9a-431f-87aa-c6958a6874c9" width:200 />

- In the *Conversations* tab, I can view the conversations between endpoints and the amount of packets and bytes recorded. By doing this, I can see if there are abnormally high packets or bytes recorded and note the addresses they are coming from.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/84936ee9-7fe8-4285-acc7-2fefe2a813da" width:200 />
