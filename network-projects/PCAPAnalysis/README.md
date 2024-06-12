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

## *Protocol Hierarchy & Conversations*
After configuring settings, I opened the file properties under the statistics tab to view the time this scan took place, for how long traffic was recorded, and the OS and version used. This isn't a necessary step however if you were receiving this file from a client, you could verify the time and date of the incident by using the information given in the file. Time is valuable and making sure the correct file was sent over before investigating is crucial.

- After configuring these settings, I went to the *Protocol Hierarchy* tab in settings. By viewing the protocols used in this file without diving in quite yet, I can see that based on some of these protocols, for example, HTTP, that is unencrypted traffic and I will be able to read the exchange.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/09a1981f-1b9a-431f-87aa-c6958a6874c9" width:200 />

- In the *Conversations* tab, I can view the conversations between endpoints and the amount of packets and bytes recorded. By doing this, I can see if there are abnormally high packets or bytes recorded and note the addresses they are coming from. Clicking on the Ipv4 tab, I note the top two IP addresses: _10.251.96.5_ and _10.251.96.4_. The other IPs to note are right below.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/f12a7186-d30b-4c30-95b9-6a6bbcac5235" width:200 />

- Clicking on the TCP tab, I can investigate which ports are being targeted by the top two IP addresses. I notice that a lot of ports are being hit towards the IP ending in _96.5_. The bytes seem to be the same across the board except for an outlier, 184 bytes on port 80 and 22. Not only that but throughout the entire conversation, the same source port **41675** is being used to connect to several destination ports which is indicative of port scanning behavior. This is unusual for standard client behavior which typically uses ephemeral/temporary ports to initiate a connection and then is released.
  - *Note:* I can infer that the IP of **10.251.96.5** has port 80 and 22 open based on the 184 bytes because this likely means that the destination host had responded with a SYN/ACK flag, whereas the others did not. The 184 bytes likely include the initial SYN packet from the scanner, the SYN/ACK response, and possibly the ACK packet from the scanner, confirming the connection attempt. For the other ports, the byte count remaining at 118 likely indicates no response or a RST (Reset) packet, suggesting these ports are closed.
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/d7a8a33e-8aa0-45cf-94ad-4b8553d675ab" width:200 />
- Another interesting thing to note is the use of port 4422 between these two suspicious IP addresses, as well as the number of packets.
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/ec5d7dae-1621-4644-af17-ce8a8ce27763" width:200 />

## *Following the stream*

- Examining the first GET request on packet 14, I right-click and select follow HTTP stream. Since this is using HTTP and isn't encrypted, I can read the interaction. I can see that **172.20.10.2** is an Ubuntu server.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/13a013f0-4c5b-43d9-b6a0-1ff4a934a86b" width:200 />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/4f18c2e9-0bc2-4424-b275-e2d53c1f0f35" width:200 />

- Scrolling down I see the first POST request on packet 30. Following this leads me to packet 38 and here I can see the username and password were entered all because HTTP is unencrypted (which is why as a user you want to avoid ever entering your login information on a website/server that uses HTTP and not HTTPS because this is highly vulnerable to MITM attacks).
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/f0ddeddf-59d5-4f01-9888-a8112467ee64" width:200 />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/36ff5d0c-90e7-4dbb-bdb0-ce021e8edcac" width:200 />

- Returning to the main window, I see the start of **10.251.96.4** targeting **10.251.96.5** on packet 117 and take note of the start time of the scan which is 2021-02-07 16:33:06. On packet 134, I see a SYN/ACK on port 80 indicating an open port. This is also seen for port 22 on packet 151.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/1a7c2af2-247e-44d6-840e-0709bdd385c4" width:200 />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/ff36ab5c-c7c9-4b9d-8eeb-f867ab17befa" width:200 />

- The scan ends on packet 2166 within a second, and the first communication is initiated shortly after via GET request. I follow the stream and take note of the user-agent.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/1b272dd3-40f4-4870-a74e-6935586aba4f" width:200 />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/0cde3ada-e2f1-43df-a713-bca0007fb34c" width:200 />

- The user-agent changes on packet 2215 and is indicated as gobuster which is a software used for brute forcing directories on web servers.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/ef455d34-8b09-437b-9fef-0845d07d8834" width:200 />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/107dc8cc-ab8a-4069-8462-4c7188f3f0c0" width:200 />

- gobuster starts crawling through the known directory alphabetically.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/25f957e1-d2fd-41be-82e8-727ec2f54c36" width:200 />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/8963db25-1b01-4194-b547-702e65f899bd" width:200 />

- A majority of the requests resulted in 404 not found, so I ran a query to see if any successful attempts were coming from that IP.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/72870a41-b4b3-4d38-adc6-6527f34e4aa8" />

- On packet 7725 a successful GET request was made for /info.php and the version of php was revealed to the attacker, prompting the potential to look for known exploits.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/da114bb4-6fa0-44c5-9b7c-0e34fe2d4124" width:200 />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/c8d6d41c-45ba-43f3-a8f7-17c44177a5de" width:200 />

- /info.php is successful again but from a different user-agent, possibly the attacker visiting this manually.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/637a43be-55b0-4031-939e-74042bf18c6a" width:200 />

- I see a GET request with /uploads/ on packet 13914. I followed this to see if there was POST request and found that on packet 13979 the user-agent changed again, and this time it's sqlmap, which is an automated utility for SQL injections.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/a72dd022-16e0-48a1-a1c3-1e5ba6f318e7" width:200 />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/c41dc471-d73c-4a33-bf42-490a4b539404" width:200 />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/656c6d6e-c705-44e1-a536-302176714ad7" width:200 />

- I noticed a strange POST request and examined it using a URL decoder to find that it looked like a SQL injection was taking place.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/34827652-345b-42a1-be72-af09ffd30266" width:200 />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/3ff16b6a-17c9-400b-a6c5-ae84912b9238" width:200 />

- Under this POST request, it looks like the attacker used upload.php to upload a web shell called dbfunctions.php. Then the attacker invokes their first commands like *whoami, id*.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/498d3022-e2d9-44dd-85d3-36556ef65253" wdith:200 />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/75d12062-6cd6-4020-97de-e52cb075cdd9" width:200 />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/4fbc8e58-f5b4-4e74-a8b1-9b4d539df0a1" width:200 />

- Following this unique stream that has Python, I copy and paste the info into the URL decoder to see what the attacker is attempting.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/a14b5d8e-0a01-4e8f-a69d-3bb6359abcb4" width:200 />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/1cd60c92-de95-49f2-9a14-496d9320e9ed" width:200 />

- I see that they are making a connection on port 4422 towards **10.251.96.4** calling the subprocess of bin. After the SYN/ACK handshake, the attacker has made a successful web shell connection and invokes discovery commands.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/8c78d46b-ebd9-45db-8926-e7a4f520d54a" width:200 />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/56b2ca9d-6995-4bc8-bd29-63b0a0a1e6ba" width:200 />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/11ed2489-e6c6-4210-8801-16d62c18c962" width:200 />

# **Findings Report**

- IP: 10.251.96.5
- Username: www-data
- hostname: bob-appserver

#

- Port scan activity
- Start: 2021-02-07 16:33:06 (UTC)
- End: 2021-02-07 16:33:06 (UTC)

#

- Source: 10.251.96.4:41675
- Destination: 10.251.96.5 (22/80 opened)

#

Applications used by 10.251.96.4
- App #1:
gobuster/3.0.1

Start time: 2021-02-07 16:34:05
End time: 2021-02-07 16:34:06

- App #2: sqlmap/1.4.7

Start time: 2021-02-07 16:36:17
End time: 2021-02-07 16:37:28

#

- Successful Web Shell Upload
- Name: dbfunctions.php
- Start time: 2021-02-07 16:40:39
- Source: 10.251.96.4
- Destination: 10.251.96.5

# 

- Commands ran by **10.251.96.4**:
(packets 16134, 16144, 16201) 
*id, whoami, python script for callback*

- (Packet 16203) Successful callback to 10.251.96.4:4422 via TCP
- (Packet 16205)reverse shell from 10.251.96.5
- Start: 16:42:35

- Commands ran from the reverse web shell via TCP:
*bash -i, whoami, cd, ls, python, rm db*

- **Last observed activity from 10.251.96.4 at 2021-02-07 16:45:56**

#

- Port range scanned: 1-1024
- Port scan conducted: TCP SYN
- PHP file that the attacker uploaded web shell: editprofile.php
- Web shell attacker uploaded: dbfunctions.php
- Parameter used to execute commands: cmd
- First command executed by the attacker: id
- Type of shell connection attacker obtains through command execution: reverse shell
- Port used for shell connection: 4422

