## For Wazuh Manager at `/var/ossec/etc/`
```xml
<ossec_config>
  <integration>
    <name>virustotal</name>
    <api_key>YOUR API KEY HERE</api_key> <!-- Replace with your VirusTotal API key -->
    <rule_id>100200,100201,100202,100203,100204,100205,100206,100207,100208,100209,100210,100211,100212,100213,100214,100215,100216,100217,100218,100219,100220,100221</rule_id>
    <alert_format>json</alert_format>
  </integration>
</ossec_config>

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
