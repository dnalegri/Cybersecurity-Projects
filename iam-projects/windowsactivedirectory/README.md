# Windows Server 2022 Network Topology with AD, DHCP, DNS, and Splunk Monitoring

## Overview

This project sets up a homelab to simulate an enterprise environment using Windows Server 2022. It includes a single Domain Controller (DC) with Active Directory (AD), DHCP, and DNS services, and integrates Splunk for Security Information and Event Management (SIEM) alerts. This setup showcases Identity and Access Management (IAM) controls, with users and groups themed around Game of Thrones characters. Additionally, it provides an environment for practicing PowerShell scripting and Splunk Processing Language (SPL).

## Topology Diagram

<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/ea65bda1-aa75-46ac-8da0-06276118dd3f" width:200 />

## Components

### VMware NAT Network

- **Subnet**: 10.0.2.0/24
- **Gateway IP**: 10.0.2.1

### Windows Server 2022

- **Roles**:
  - Active Directory Domain Controller (AD DC)
  - DHCP Server
  - DNS Server
  - Splunk Enterprise
- **IP Address**: 10.0.2.10

### Client Machines

- **Role**: Domain-joined client
- **IP Addresses**: Assigned by DHCP (e.g., 10.0.2.129, 10.0.2.130)

### Splunk Monitoring

- **Installed On**: Windows Server 2022
- **Functionality**:
  - Monitoring Active Directory events
  - Dashboards and Alerts for various AD activities

## Network Configuration Details

### VMware NAT Settings

- **Subnet IP**: 10.0.2.0
- **Subnet Mask**: 255.255.255.0
- **Gateway IP**: 10.0.2.1

#### Advanced Settings

- **Allow active FTP**: Enabled
- **Allow any organizationally unique identifier (OUI)**: Enabled

### DHCP Settings (Windows Server)

- **Starting IP**: 10.0.2.129
- **Ending IP**: 10.0.2.254
- **Broadcast Address**: 10.0.2.255
- **Max Lease Time**: 8 hours
