# Windows Server 2022 with AD, DHCP, DNS, and Splunk Monitoring (In Progress)
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
</div>

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

  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/3ff1b7cf-abf9-438c-917d-6363382d3483" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/9c9ad4d4-f296-4070-ae6d-76ad4f4874cb" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/fa5a8e1e-2260-4e14-9735-4e9a579246a7" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/a32f75f6-0f2c-479f-96df-6f366e997dc9" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/1c0a0702-ce0b-443d-99a6-697758981b7a" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/afd790b2-8c6d-4a81-a367-ed1bbb039475" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/df8191a6-1a41-4185-b59d-005e78ac5d73" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/1471c919-a22e-4d69-85ca-aff3916afed1" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/8ad86cd4-91fc-49d9-bdcd-df06a22a0738" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/08877cd7-0a26-466f-8b3a-989d88d7bd38" width="500" />

## DHCP IP Assignment Verification
> I want to make sure that the DHCP Scope I set up is correctly assigning addresses and that the machine is configured properly with the internal network. I use the *ipconfig /all* cmd to view this information and verify that it's correct.
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/42c3f0ac-0f14-431f-ba65-3e76824cc358" width="400" />

> > On the Windows Server, I also verify this under the DHCP Manager.
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/1c057126-26b7-438c-bb65-7747e9b0f626" width="400" />

## Creating Users and Groups
> To link the machine to the domain, I create a user account. Since this is a non-production environment and a homelab, I set the password to never expire for ease of access for myself.
> > *The entire theme of the users and groups is Game of Thrones as well.*
<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/b694a2e6-ba79-458d-959e-8b53e1cadfa7" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/d5dfe299-a864-4dcb-b934-2f12ddee4d1a" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/1a1d990c-d481-4d6c-b7ee-cd17a0396f05" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/d6e9839b-820d-4f6e-9be0-c35b89ac62f6" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/a1c4b0bc-18ea-456f-b2ad-22504694bcf1" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/ac966626-fabc-46a4-999b-b7813d5a324b" width="400" />

> > Now on the machine I link the domain and test the implementation.
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/d1ca5486-c01d-40ba-9a50-d168d8f7f17c" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/fc29bc12-ad2c-4819-bc2c-a99cbfc9b5b8" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/4df944fc-28c2-4822-8b4e-3ed9dfe646c4" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/76fb9bff-15f5-4f3a-b862-f0a8c9694e6a" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/f473ec44-a260-41fb-864e-f45ae4a95361" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/585d62d4-73e6-41f7-b4b4-afa8581dd2c7" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/16281131-7f24-4362-8eaa-4a2b6ce21ed0" width="500" />


## Using Powershell to Create Users and Groups
> I created some users and groups the easy way through the Users and Computers tool in the Active Directory. A crucial skill for me to learn is Powershell for automation and scripting, and in this environment, I can give myself a foundation to learn through trial and error. I wanted to create a group called House Lannister and add some users to that group via Powershell. I also made sure to assign the password and password settings this way.
> > *Note*: I will be adding more users and groups using Powershell. I want to create a script that has at least 50 users and import the CSV into Powershell. I will update this page as this project grows.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/e954617e-847d-4ab4-92e5-bc1871cfb664" width="800" />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/cb412170-ccf6-4af5-bb22-29bbb9b1fec8" width="800" />

1. **ConvertTo-SecureString**: This cmdlet converts plain text into an encrypted SecureString object, which is a secure way to handle passwords or other sensitive information in PowerShell.
2. **"hearmeroar1!"**: This is the plain text string that will be converted into a SecureString. In this case, "hearmeroar1!" is the password being converted.
3. **-AsPlainText**: This parameter indicates that the input string ("hearmeroar1!") should be treated as plain text before converting it to a SecureString. This is necessary because normally, ConvertTo-SecureString expects input in the form of a SecureString.
4. **-Force**: This parameter is used to suppress any prompts or warnings that would normally appear during the conversion process. It forces the cmdlet to execute without asking for confirmation.

<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/a84615f4-8e41-400f-9f44-8c1cec68c957" width="800" />
  
  **New-AdUser**: This is the cmdlet used to create a new Active Directory user.

  **-Name** "Tywin Lannister": This specifies the name of the new user. In this case, the user's name is "Tywin Lannister".

  **-SamAccountName "tlannister"**: This sets the Security Account Manager (SAM) account name, which is also known as the user logon name. Here, it is set to *"tlannister"*.

  **-AccountPassword $password**: This sets the user's password. The variable $password should contain a secure password object (created using Read-Host -AsSecureString or a similar method).

  **-PasswordNeverExpires $true**: This sets the password to never expire. The value $true indicates that the password will not expire.

  **-Description "Lord of Casterly Rock"**: This adds a description to the user's account.

  **-Enabled $true**: This enables the user account immediately upon creation. If set to $false, the account would be created but disabled.

  **-UserPrincipalName "tlannister@yellow.local"**: This sets the User Principal Name (UPN) for the account, which is often used as the login name.
  
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/3a56cf85-6b1c-49af-a5bf-272284f4f133" width="400" />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/91d2c5cf-0875-4247-bebf-e5a75073154a" width="400"/>

> Pictured above, I verified that the Group and Users were created correctly using the command *Get-ADGroup* and *Get-ADUser*

### Creating a File Share

> I wanted to implement RBAC principles and least privileged access by creating a file share that only one specific group can access. I used House Lannister as the group and created a file share called *Lannister Family Secrets* that had sensitive information that no one besides the Lannisters could access. 

  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/82424628-57b8-4568-90ad-436d418088f6" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/acf3e463-7180-4766-abe0-c7a42a59c3d8" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/7918dd91-3848-49b3-b614-93abb3efdf54" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/82e2378d-9090-4222-8185-1e1015a24df2" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/5d1ec6a3-4752-4c65-82cf-3dc9306c64dd" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/63d1eeac-7cde-4b29-8687-b04276672b3e" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/3d856c82-c51b-4650-a764-7b32c9a80d18" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/bd282410-af23-4f95-9fa9-8601a7a138ba" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/005ddf99-6e89-401d-af4e-97db0388971c" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/3bd24e42-f07b-4be0-b4a5-6c55b8f384b2" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/b3347d67-f0a8-4b48-bf6c-14eebfa70f4f" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/11f557db-a8a2-4c64-b59f-2dbcff66862a" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/a1e5780a-4c2b-4923-b0a3-f7d5699d3264" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/f0144cf9-1842-4a40-b091-9344564d5a76" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/2af320aa-c6fc-4985-8892-086343a7d1d5" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/55a494ea-c50a-424e-9251-0e94294d4ff3" width="500" />

  > After the share was created, I logged in to the user *tlannister* and searched for the file share to test the implementation. The implementation is successful because the user who is in the group with access permissions can view the file. 

  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/63f36891-bd74-4ccf-8a60-3355b8fe74c2" width="400" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/a4bf1e98-749c-4035-b445-a13c53dd19c2" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/6064a654-c688-4096-a8bd-43f28bd21d2a" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/2a3561d8-5906-423f-bbb3-fc24b2a744ed" width="400" />

 > I then logged into the *nstark* account which is not part of the Lannister Family Group. Furthermore, the file share was successfully configured because access was denied.
 <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/92765dc1-03cc-4b73-8f4e-65c6e752f9b9" width="400" />

## Installing Splunk Enterprise
 > Since the client machines have direct internet access, I downloaded the Splunk Enterprise installer and put it in a shared folder which I could access on the Windows Server. I proceeded with the installation.

  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/3e937f42-dfdf-48fb-b274-34b8b69712a2" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/0d8e9eaa-9ac0-44a3-b606-92dd4975924e" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/28a23598-a048-468d-a1ee-d4052b550542" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/6476917f-a2e3-4f58-a2ed-86d01ea26d4e" width="500" />

  > After install, I configured the data I wanted to ingest, which was the local data from the server and the Active Directory.
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/3f08564b-02ca-460c-9be2-2c84d3f737ec" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/8f9607dd-336e-42e6-9159-b3eebb2fa09e" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/c8af1de7-7819-43cc-b6fb-0f2ace1e0891" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/1aa104f1-91fc-4bc7-8ed5-38b87b671808" width="500" />
 
  > *Note:* I did go back onto this page and manually input the name of my target domain controller since Splunk was having a hard time finding it automatically.

  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/d2176c97-8a11-4cd6-88f2-5df988f03fa4" width="500" />
  <img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/c070e78c-11a2-4b6d-a648-2688d09ae325" width="500" />

### Splunk Queries
> I am going to dive deep and add a separate project that focuses on SIEM tools like Splunk and showcase queries, alerts, and dashboards there. But just to show a very basic and quick query, I will look for the recent user I created called **splunkadmin**. ALSO bare with me, I know this query is super bare bones and nothing deep for analyzing logs... I'm working on an SPL/Splunk project to explore queries, alerts, and dashboards.
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/e88d8dd4-dde6-4513-a89a-4ce4c97e3102" width="800" />
<img src="https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/25d3e90f-5f33-4413-b8be-33d9e80dcdda" width="500" />
