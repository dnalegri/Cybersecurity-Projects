## Integration with Wazuh

1. **Add Suricata Logs to Wazuh Agent Configuration:**
    ```sh
    cd /var/ossec/etc/
    sudo nano /var/ossec/etc/ossec.conf
2. **Add the configuration:**
    ```xml
    <ossec_config>
      <localfile>
        <log_format>json</log_format>
        <location>/var/log/suricata/eve.json</location>
      </localfile>
    </ossec_config>
3. **Restart the Wazuh Agent:**
    ```sh
    sudo systemctl restart wazuh-agent

## Attack Emulation
1. **Ping the Kali Endpoint from the Wazuh Server:**
    ```sh
    ping -c 20 "<KALI_IP>"
## Visualize the Alerts
1. **View Alerts in the Wazuh Dashboard:**
   - Go to the Threat Hunting Module.
   - Add the following filter in the search bar to query the alerts:
     ```sh
     rule.groups:suricata

> Wazuh automatically parses data from /var/log/suricata/eve.json and generates related alerts on the Wazuh dashboard
## Documentation
> Below are the images from teh Wazuh agent dashboard, showing the successful integration of Suricata. The ICMP pings alerted in Wazuh.
![icmp ping suri 2](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/a70d050f-79cf-4752-af56-3ac7de897730)
![icmp ping suri](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/bf265090-a662-48ee-aa0e-97b4b2e6af38)
