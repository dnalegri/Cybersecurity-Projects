# VirusTotal FIM Update

Updating the `localrules.xml` on the Wazuh manager and the `ossec.conf` on the Wazuh agent for more monitoring and coverage.

## Overview

### Setup Summary
- **Wazuh Manager**: Deployed on an Ubuntu desktop in VMware Pro.
- **Wazuh Agent**: Deployed on a Kali Linux machine in VMware Pro.
- **Suricata**: Installed on the Kali Linux machine.

### Goals
- Use VirusTotal to detect and remove malware.
- Utilize Suricata to analyze network traffic and detect intrusions.
- **Add more directories to enhance security posture and coverage.**

### Updating the Configuration on Kali Endpoint
1. Navigate to `/var/ossec/etc/ossec.conf` Add an entry within the <syscheck> block to configure a directory to be monitored in near real-time. In this case, I want to add several critical directories to ensure I'll be notified of any unauthorized changes or modifications:
```xml
  <directories realtime="yes">/home/dnalegri/Downloads,/etc,/usr/bin,/usr/sbin,/bin,/sbin,/boot,/var/www,/root,/usr/local/bin,/usr/local/sbin,/opt,/var/log</directories>
```

2. To prevent false positives with Suricata and Journal I add it to the exceptions (more on this below):
```xml
<!-- Ignore specific files or directories -->
      <ignore>/var/log/journal/</ignore>
      <ignore>/var/log/suricata/eve.json</ignore>
```
### Updating the Configuration on the Wazuh Manager (Ubuntu Desktop)
1. Navigate to `/var/ossec/rules/local_rules.xml`. Update the local_rules to the corresponding directories:
```xml
   <!-- New rules for additional directories -->
  <rule id="100202" level="7">
    <if_sid>550</if_sid>
    <field name="file">/etc</field>
    <description>File modified in /etc directory.</description>
  </rule>
  <rule id="100203" level="7">
    <if_sid>554</if_sid>
    <field name="file">/etc</field>
    <description>File added to /etc directory.</description>
  </rule>

  <rule id="100204" level="7">
    <if_sid>550</if_sid>
    <field name="file">/var/www</field>
    <description>File modified in /var/www directory.</description>
  </rule>
  <rule id="100205" level="7">
    <if_sid>554</if_sid>
    <field name="file">/var/www</field>
    <description>File added to /var/www directory.</description>
  </rule>

  <rule id="100206" level="7">
    <if_sid>550</if_sid>
    <field name="file">/usr/bin</field>
    <description>File modified in /usr/bin directory.</description>
  </rule>
  <rule id="100207" level="7">
    <if_sid>554</if_sid>
    <field name="file">/usr/bin</field>
    <description>File added to /usr/bin directory.</description>
  </rule>

  <rule id="100208" level="7">
    <if_sid>550</if_sid>
    <field name="file">/usr/sbin</field>
    <description>File modified in /usr/sbin directory.</description>
  </rule>
  <rule id="100209" level="7">
    <if_sid>554</if_sid>
    <field name="file">/usr/sbin</field>
    <description>File added to /usr/sbin directory.</description>
  </rule>

  <rule id="100210" level="7">
    <if_sid>550</if_sid>
    <field name="file">/boot</field>
    <description>File modified in /boot directory.</description>
  </rule>
  <rule id="100211" level="7">
    <if_sid>554</if_sid>
    <field name="file">/boot</field>
    <description>File added to /boot directory.</description>
  </rule>

  <rule id="100212" level="7">
    <if_sid>550</if_sid>
    <field name="file">/root</field>
    <description>File modified in /root directory.</description>
  </rule>
  <rule id="100213" level="7">
    <if_sid>554</if_sid>
    <field name="file">/root</field>
    <description>File added to /root directory.</description>
  </rule>

  <rule id="100214" level="7">
    <if_sid>550</if_sid>
    <field name="file">/usr/local/bin</field>
    <description>File modified in /usr/local/bin directory.</description>
  </rule>
  <rule id="100215" level="7">
    <if_sid>554</if_sid>
    <field name="file">/usr/local/bin</field>
    <description>File added to /usr/local/bin directory.</description>
  </rule>

  <rule id="100216" level="7">
    <if_sid>550</if_sid>
    <field name="file">/usr/local/sbin</field>
    <description>File modified in /usr/local/sbin directory.</description>
  </rule>
  <rule id="100217" level="7">
    <if_sid>554</if_sid>
    <field name="file">/usr/local/sbin</field>
    <description>File added to /usr/local/sbin directory.</description>
  </rule>

  <rule id="100218" level="7">
    <if_sid>550</if_sid>
    <field name="file">/opt</field>
    <description>File modified in /opt directory.</description>
  </rule>
  <rule id="100219" level="7">
    <if_sid>554</if_sid>
    <field name="file">/opt</field>
    <description>File added to /opt directory.</description>
  </rule>

  <rule id="100220" level="7">
    <if_sid>550</if_sid>
    <field name="file">/var/log</field>
    <description>File modified in /var/log directory (excluding Suricata).</description>
    <!-- Example to specifically include or exclude files or directories -->
    <ignore>/var/log/suricata</ignore>
    <ignore>/var/log/journal</ignore>

  </rule>

  <rule id="100221" level="7">
    <if_sid>554</if_sid>
    <field name="file">/var/log/</field>
    <description>File added to /var/log directory.</description>
    <ignore>/var/log/suricata</ignore>
 </rule>
</group>
```
3. Update the VirusTotal block in `/var/ossec/etc/ossec.conf`:
```xml
  <ossec_config>
  <integration>
    <name>virustotal</name>
    <api_key>YOUR API KEY HERE</api_key> <!-- Replace with your VirusTotal API key -->
    <rule_id>100200,100201,100202,100203,100204,100205,100206,100207,100208,100209,100210,100211,100212,100213,100214,100215,100216,100217,100218,100219,100220,100221</rule_id>
    <alert_format>json</alert_format>
  </integration>
</ossec_config>
```

4. Update the active-response block in `/var/ossec/etc/ossec.conf` to enable malicious file removal and trigger command `remove-threat.sh`. Uses the rule_ids we have set up:
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

  <!-- Additional configurations to handle VirusTotal flagged threats -->
  <active-response>
    <disabled>no</disabled>
    <command>remove-threat</command>
    <location>local</location>
    <rules_id>100200,100201,100202,100203,100204,100205,100206,100207,100208,100209,100210,100211,100212,100213,100214,100215,100216,100217,100218,100219,100220,100221</rules_id>
  </active-response>
</ossec_config>
```
4. Add the rules to trigger alerts in `local_rules.xml`:
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

  <!-- Additional rules for active response results -->
  <rule id="100094" level="12">
    <if_sid>657</if_sid>
    <match>Active response command executed successfully</match>
    <description>Active response command executed successfully on $(parameters.srcip)</description>
  </rule>

  <rule id="100095" level="12">
    <if_sid>657</if_sid>
    <match>Failed to execute active response command</match>
    <description>Failed to execute active response command on $(parameters.srcip)</description>
  </rule>
</group>
```

## Documenting the process

![wazuh FIM 1](https://github.com/user-attachments/assets/be407716-6d4c-4187-b5ba-926d1a796499)
![wazuh FIM 11](https://github.com/user-attachments/assets/4cce281c-0867-48c9-8b13-47ba3d10985a)
![wazuh FIM 2](https://github.com/user-attachments/assets/8e23ad57-4fe9-40f3-ac47-1b42d53980f5)
![wazuh FIM 4](https://github.com/user-attachments/assets/76154aa1-37a3-468c-830f-9c55e09ef589)
![wazuh FIM 6](https://github.com/user-attachments/assets/c8ea959f-d7e9-4542-9e40-c89152bd9473)

## False positive alerts with Suricata
*Note:* Before I decided to ignore the Suricata logs, thousands of alerts popped up in Wazuh regarding file modification within `eve.json`. This is a false positive because Suricata is just logging regular network activity and saving the file. I don't need to be alerted of that every single time. It completely clogged up the dashboard so that's why I added it to the exceptions.

![wazuh FIM 8](https://github.com/user-attachments/assets/5342eae8-56c7-4cb1-a1b2-5a5d3c0979ab)
