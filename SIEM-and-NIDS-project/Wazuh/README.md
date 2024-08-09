# Wazuh-VirusTotal-Suricata Project

This project showcases the integration of Wazuh as a Security Information and Event Management (SIEM) system, VirusTotal for malware detection, and Suricata as a Network Intrusion Detection System (NIDS). The setup involves deploying Wazuh and Suricata on different virtual machines and configuring them to work together for comprehensive security monitoring.

## *Updated FIM rules now shown above*

## Overview

### Setup Summary
- **Wazuh Manager**: Deployed on an Ubuntu desktop in VMware Pro.
- **Wazuh Agent**: Deployed on a Kali Linux machine in VMware Pro.
- **Suricata**: Installed on the Kali Linux machine.

### Goals
- Implement Wazuh as a SIEM to monitor and manage security events.
- Use VirusTotal to detect and remove malware.
- Utilize Suricata to analyze network traffic and detect intrusions.

## Prerequisites
- VMware Pro for virtualization.
- Ubuntu Desktop for Wazuh Manager.
- Kali Linux for Wazuh Agent and Suricata.
- Basic knowledge of Linux commands and networking.
