## Integration with Wazuh

1. **Add Suricata Logs to Wazuh Agent Configuration:**
    ```sh
    cd /var/ossec/etc/
    sudo nano /var/ossec/etc/ossec.conf
2. **Add the configuration:**
    ```sh
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
