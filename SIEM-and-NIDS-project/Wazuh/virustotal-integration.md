## VirusTotal Integration

### Configuration on Kali Endpoint
1. Search for the `<syscheck>` block in the Wazuh agent configuration file `/var/ossec/etc/ossec.conf`. Make sure that `<disabled>` is set to `no`. This enables the Wazuh FIM to monitor for directory changes.
   ```xml
   <syscheck>
     <disabled>no</disabled>
   </syscheck>

2. Add an entry within the <syscheck> block to configure a directory to be monitored in near real-time. In this case, monitoring the `/home/dnalegri/Downloads` directory (dnalegri is my user):
   ```xml
   <directories realtime="yes">/home/dnalegri/Downloads</directories>
3. Make sure 'jq' is installed:
   ```sh
   sudo apt-get install jq
4. Create the `/var/ossec/active-response/bin/remove-threat.sh` active response script to remove malicious files from the endpoint
   > remove-threat.sh is listed in this folder
  
6. Change the `/var/ossec/active-response/bin/remove-threat.sh` file ownership and permissions:
   ```sh
   sudo chmod 750 /var/ossec/active-response/bin/remove-threat.sh
   sudo chown root:wazuh /var/ossec/active-response/bin/remove-threat.sh
7. Restart the Wazuh agent:
   ```sh
   sudo systemctl restart wazuh-agent

### Configuration on Wazuh Server
1. Add the following rules to the `/var/ossec/etc/rules/local_rules.xml` file on the Wazuh server. These rules alert about changes in the `/home/dnalegri/Downloads` directory that are detected by FIM scans:
```xml
<group name="syscheck,pci_dss_11.5,nist_800_53_SI.7,">
  <!-- Rules for Linux systems -->
  <rule id="100200" level="7">
    <if_sid>550</if_sid>
    <field name="file">home/dnalegri/Downloads</field>
    <description>File modified in /home/dnalegri/Downloads directory.</description>
  </rule>
  <rule id="100201" level="7">
    <if_sid>554</if_sid>
    <field name="file">home/dnalegri/Downloads</field>
    <description>File added to home/dnalegri/Downloads directory.</description>
  </rule>
</group>
```
2. Add the following configuration to the Wazuh server `/var/ossec/etc/ossec.conf` file to enable the VirusTotal integration. Replace <YOUR_VIRUS_TOTAL_API_KEY> with your VirusTotal API key. This allows a VirusTotal query to be triggered whenever any of the rules 100200 and 100201 are triggered:
```xml
<ossec_config>
  <integration>
    <name>virustotal</name>
    <api_key><YOUR_VIRUS_TOTAL_API_KEY></api_key> <!-- Replace with your VirusTotal API key -->
    <rule_id>100200,100201</rule_id>
    <alert_format>json</alert_format>
  </integration>
</ossec_config>
```
3. Append the following blocks to the Wazuh server `/var/ossec/etc/ossec.conf` file. This enables active response and triggers the remove-threat.sh script when VirusTotal flags a file as malicious:
```xml
<ossec_config>
  <command>
    <name>remove-threat</name>
    <executable>remove-threat.sh</executable>
    <timeout_allowed>no</timeout_allowed>
  </command>

  <active-response>
    <disabled>no</disabled>
    <command>remove-threat</command>
    <location>local</location>
    <rules_id>87105</rules_id>
  </active-response>
</ossec_config>
```
4. Add rules to alert about the active response results in `/var/ossec/etc/rules/local_rules.xml`:
```xml
<group name="virustotal,">
  <rule id="100092" level="12">
    <if_sid>657</if_sid>
    <match>Successfully removed threat</match>
    <description>$(parameters.program) removed threat located at $(parameters.alert.data.virustotal.source.file)</description>
  </rule>

  <rule id="100093" level="12">
    <if_sid>657</if_sid>
    <match>Error removing threat</match>
    <description>Error removing threat located at $(parameters.alert.data.virustotal.source.file)</description>
  </rule>
</group>
```
5. Restart the Wazuh manager to apply changes:
    ```sh
    sudo systemctl restart wazuh-manager

## Testing the Alert
To test the alert and trigger the VirusTotal integration, use the following command to download the EICAR test file into the monitored directory:
   ```sh
   sudo curl -Lo /home/dnalegri/Downloads/eicar.com https://secure.eicar.org/eicar.com && sudo ls -lah /home/dnalegri/Downloads/eicar.com
```
This command will:
- Use curl to download the EICAR test file from the specified URL.
- Save the file into the `/home/dnalegri/Downloads` directory, which is being monitored by Wazuh.
- List the details of the downloaded file to confirm its presence.

By placing the EICAR test file in this directory, it should trigger the Wazuh File Integrity Monitoring (FIM) alert, which will then invoke the VirusTotal integration to check the file. If VirusTotal flags the file as malicious, the configured active response script remove-threat.sh will attempt to remove it, and the corresponding alerts will be generated in Wazuh.

## Documentation
> Below is the EICAR test visualized in Wazuh. They were effectively removed from the Kali endpoint as per the configuration.

![fim test](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/888403a2-4d4e-4c1c-9f30-88674cf9cf06)
