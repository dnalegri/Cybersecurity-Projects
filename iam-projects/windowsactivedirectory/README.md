# Windows Server 2022 with AD, DHCP, DNS, and Splunk Monitoring

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

## Initial Setup and Configuration

### Windows Server Static IPv4 IP, DNS IP, & DHCP Scope

> I am not going to walk through the installation process of downloading the Windows Server or adding roles (DHCP, DNS). Here I will show the process of how I configured the static IPv4 address of the Windows Server, DNS setup, and DHCP scope.
### DHCP Scope

> > Under the Windows Server network settings, I went to change adapter and clicked properties. I can configure the IPv4 address and DNS based on the virtual NAT I created in VMware Pro. Since my Windows server is acting as the DNS, the DNS IP is the same as IPv4.
> > > *Note*: *When I first created my Windows Server I was unaware that my DNS IP had to be the same as my server's IPv4 to be configured correctly with my single DC setup. I encountered connection errors due to setting my DNS address as 10.0.2.128 instead of the IPv4 of the server itself (10.0.2.10). I realized that the DNS server wasn't connecting correctly because I was using an IP that couldn't be resolved. After all, it didn't exist within my environment. You will see the obsolete DNS address in the screenshots below, but I will show how I updated it.*
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/d2439ecb-b266-419a-a291-026a5eafc5fb" />

> > > > Under tools and DHCP, I go to the manager and create a new scope.
<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/c342ead5-1a15-4093-9ffe-3a3014fbc0da" width="400"/>
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/9dcf94c0-1b09-4193-8084-d440c1f6e6c2" width="400"/>
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/f0354465-9819-4848-a5f2-e1eca52670c4" width="400"/>
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/028401e4-0036-40b0-a9e0-6d127b5ca1b8" width="400"/>
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/c7a45f0b-04bb-4934-98b6-b231a661fae6" width="400"/>
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/072990b1-3a03-409a-a4ae-d847c7d2134a" width="400"/>
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/41d1491c-bbfc-4f1d-93b6-d7abcf154f2f" width="400"/>
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/6a93cd3e-54d9-4d03-a313-cdeca2697551" width="400"/>
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/4363a0d8-67e0-487f-a362-285d44747a64" width="400"/>
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/5ae14b06-1c4e-4421-93b7-fc5a5f050c84" width="400"/>
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/171ebd8e-96c6-4332-af5f-7772b82d1a42" width="400"/>

>  I ensure that the DHCP Scope options include the correct DNS server (it didn't). So I updated the record 006.
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/fc036163-5dea-4758-aba9-915f12c309ca" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/fbf913b7-4bfc-42b7-b89e-82b04d64ef49" />

### DNS Manager
> For our DNS to resolve back to the name of our server, there must be an A record present.
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/01d42895-8728-4517-8bb8-7571aeb2b0db" width="600" />

> > On the client machine, I did a ping test to verify the DNS record and connection.
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/a8eee812-3a26-458e-a8b7-6ee98ccd9fc8" width="400" />

> Under the properties section I also unchecked the IPv6 address since it is not needed in this environment, and I put alternate forwarders for DNS queries that cannot resolve locally to another DNS server (Cloudflare & Google).
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/36ce715d-e7ac-43b8-8a56-518d30bae405"  width="400"/>
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/3ad68fe2-76b1-4254-adaf-38cd20eb1465" width="400" />

## Client Machine: Windows 10 Enterprise Installation, Domain Sign-in, IP Configuration

### Installing Windows 10 Enterprise

  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/3ff1b7cf-abf9-438c-917d-6363382d3483" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/9c9ad4d4-f296-4070-ae6d-76ad4f4874cb" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/fa5a8e1e-2260-4e14-9735-4e9a579246a7" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/a32f75f6-0f2c-479f-96df-6f366e997dc9" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/1c0a0702-ce0b-443d-99a6-697758981b7a" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/afd790b2-8c6d-4a81-a367-ed1bbb039475" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/df8191a6-1a41-4185-b59d-005e78ac5d73" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/1471c919-a22e-4d69-85ca-aff3916afed1" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/8ad86cd4-91fc-49d9-bdcd-df06a22a0738" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/08877cd7-0a26-466f-8b3a-989d88d7bd38" width="400" />

## DHCP IP Assignment Verification
> I want to make sure that the DHCP Scope I set up is correctly assigning addresses and that the machine is configured properly with the internal network. I use the *ipconfig /all* cmd to view this information and verify that it's correct.
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/42c3f0ac-0f14-431f-ba65-3e76824cc358" width="400" />

> > On the Windows Server, I also verify this under the DHCP Manager.
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/1c057126-26b7-438c-bb65-7747e9b0f626" width="400" />

## Creating Users and Groups
> To link the machine to the domain, I create a user account. Since this is a non-production environment and a homelab, I set the password to never expire for ease of access for myself.
> > *The entire theme of the users and groups is Game of Thrones as well.*
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/b694a2e6-ba79-458d-959e-8b53e1cadfa7" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/d5dfe299-a864-4dcb-b934-2f12ddee4d1a" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/1a1d990c-d481-4d6c-b7ee-cd17a0396f05" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/d6e9839b-820d-4f6e-9be0-c35b89ac62f6" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/a1c4b0bc-18ea-456f-b2ad-22504694bcf1" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/ac966626-fabc-46a4-999b-b7813d5a324b" width="400" />

> > Now on the machine I link the domain and test the implementation.
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/d1ca5486-c01d-40ba-9a50-d168d8f7f17c" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/fc29bc12-ad2c-4819-bc2c-a99cbfc9b5b8" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/4df944fc-28c2-4822-8b4e-3ed9dfe646c4" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/76fb9bff-15f5-4f3a-b862-f0a8c9694e6a" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/f473ec44-a260-41fb-864e-f45ae4a95361" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/585d62d4-73e6-41f7-b4b4-afa8581dd2c7" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/16281131-7f24-4362-8eaa-4a2b6ce21ed0" width="400" />
</div>

## Using Powershell to Create Users and Groups
> I created some users and groups the easy way through the Users and Computers tool in the Active Directory. A crucial skill for me to learn is Powershell for automation and scripting, and in this environment, I can give myself a foundation to learn through trial and error. I wanted to create a group called House Lannister and add some users to that group via Powershell. I also made sure to assign the password and password settings this way.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/e954617e-847d-4ab4-92e5-bc1871cfb664" width="400" />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/cb412170-ccf6-4af5-bb22-29bbb9b1fec8" width="400" />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/a84615f4-8e41-400f-9f44-8c1cec68c957" width="400" />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/3a56cf85-6b1c-49af-a5bf-272284f4f133" width="400" />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/91d2c5cf-0875-4247-bebf-e5a75073154a" width="400"/>




