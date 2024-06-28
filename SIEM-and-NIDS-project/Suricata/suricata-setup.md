## Suricata Setup

### Installation and Configuration on Kali Linux
1. **Install Suricata:**
   ```sh
   sudo apt update
   sudo apt -y install suricata

2. **Enable and Start Suricata:**
   ```sh
    sudo systemctl enable suricata.service
    sudo systemctl start suricata.service
    sudo systemctl status suricata

> *After verifying that Suricata is active, stop the service.*

3. **Edit the Suricata Configuration File:**
   ```sh
   sudo nano /etc/suricata/suricata.yaml

- Set the HOME_NET variable to your machine's IP:
  ```sh
  home-net: "[192.168.0.0/24]"

- Ensure the interface is set to your machine's interface *(mine is eth0)* in the af-packet and pcap sections:
    ```sh
    af-packet:
  - interface: eth0
  pcap:
  - interface: eth0

- Enable community-id:
   ```sh
   vars:
  community-id: true

4. **Set Up Sources:**
   ```sh
   sudo suricata-update list-sources
   sudo suricata-update enable-source malsilo/win-malware
   sudo suricata-update enable-source etnetera/aggressive
   sudo suricata-update enable-source sslbl/ssl-fp-blacklist

5. **Reload the Configuration:**
    ```sh
    sudo suricata -T -c /etc/suricata/suricata.yaml -v

6. **Start Suricata Service:**
   ```sh
   sudo systemctl start suricata.service

7. **Verify Suricata Logs:**
   ```sh
   sudo tail -f /var/log/suricata/fast.log

8. **Test Suricata:**
   *Use a test site to generate an alert*
      ```sh
      curl http://testmynids.org/uid.index.html uid=0(root) gid=0(root) groups=0(root)
      sudo cat /var/log/suricata/fast.log

## Local Rule Configuration
1. **Add Local Rule:**
   ```sh
     sudo nano /etc/suricata/rules/local.rules
- Add the following rule to log ICMP pings:
   ```sh
   alert icmp any any -> $HOME_NET any (msg:"ICMP Ping"; sid:1; rev:1;)
2. **Include Local Rule in /etc/suricata/suricata.yaml:**
      ```sh
      default-rule-path: /var/lib/suricata/rules
    rule-files:
    -   suricata.rules
    - /etc/suricata/rules/local.rules
3. **Reload the Configuration:**
      ```sh
      sudo suricata -T -c /etc/suricata/suricata.yaml -v
4. **Test Local Rule by Pinging:**
   *From another machine, ping the Kali machine*
      ```sh
      ping -c 4 <KALI_IP>
      sudo tail -f /var/log/suricata/fast.log
6. **Install JQ and search the eve.json log for the alert:**
      ```sh
      sudo tail -f /var/log/suricata/eve.json | jq 'select(.event_type=="alert")'

## Documentation
> Below I will list the images of these steps, demonstrating the process, following the steps listed.

![1](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/5bbb25c8-ed56-40bc-a142-e62af3472ea4)
![2](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/86527527-b439-41be-9ab8-6bbb717f93d9)
![3](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/80b2fd9b-3a41-44e9-a54c-3442c0572551)
![4](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/7f70f031-f03a-476e-a2a8-e3911b670f40)
![5](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/887f7503-1b4e-43c1-b4a4-9e193eb5c5b0)
![6](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/ef8dd3c1-2e92-4302-b834-32fc49cfbacc)
![7](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/648a44ef-0617-4449-9df2-f56d46c969ca)
![8](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/b7d04371-08f6-45e8-9ce0-9ae6d7a558f4)
![9](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/920744df-0128-48cf-a0c0-cd2d86e8d735)
![10](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/d52dabe9-cda5-4f63-88fb-392a181d274f)
![11](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/24edb314-2b77-4fbd-a4af-ab0335e71eac)
![12](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/8d44cc62-a617-4ca1-a208-0f02e818881d)
![13](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/43653a0d-35c9-493a-8b9f-c020727a5048)
![14](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/180b4af4-40cf-4cce-b6bc-9dba71ecd274)
![15](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/2ed697a4-358e-4fc4-94b4-88f41d7b00b1)
![16](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/72ccf36b-9255-4f25-acbb-b8e61f272698)
![17](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/01eaf7b3-a10d-4047-b073-f19718c13974)
![18](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/546747d5-7141-460f-a3c9-e3e6a3b0ac83)
![19](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/4014eb5f-a9f6-4639-af22-44995328c266)
![21](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/a2d2279f-926b-4145-a673-2d048c0b6e13)
![22](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/f9c885ac-4899-48ba-92a4-492db01f37d2)
![23](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/b9d2525c-b784-41f2-bfbf-0274cb9b6d9b)
![24](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/eddfd976-c76d-4b52-a3d5-1b77376bf28c)
![25](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/58628d8b-0a05-4300-8efd-4886670d3730)
![26](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/a01acea9-7b3f-4240-a241-a77e1cfba400)
![27](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/0aa18379-89a6-44b9-a4e2-8156127d1cbc)
![28](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/481ddce3-b7f7-445f-b4f4-affb8bd209f7)
![29](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/f3eba485-f15f-48ca-9437-ef94e72a7764)
![30](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/e9e5caff-e0fb-4a71-a2db-12f3dae87c62)
