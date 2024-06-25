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

- Set the HOME_NET variable:
  ```sh
  home-net: "[192.168.0.0/24]"

- Ensure the interface is set to eth0 in the af-packet and pcap sections:
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

