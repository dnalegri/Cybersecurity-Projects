## Installing Wazuh Agent on Kali Linux

1. **Download and install the Wazuh Agent:**
    ```sh
    wget https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent_4.8.0-1_amd64.deb
    sudo WAZUH_MANAGER='YOUR_WAZUH_SERVER_IP' WAZUH_AGENTNAME='kali' dpkg -i ./wazuh-agent_4.8.0-1_amd64.deb

- If encountering "invalid server address" error:
    ```sh
    sudo nano /var/ossec/etc/ossec.conf
    # Ensure the server IP is correctly listed.
2. **Start the Wazuh Agent Service:**
    ```sh
    sudo systemctl start wazuh-agent
    sudo systemctl status wazuh-agent

## Documentation
> The installation process is listed below as well as the implementation was successful as I was able to pull up the Wazuh dashboard and view the newly active agent. *Note: The dashboard doesn't show FIM because it was not configured yet. FIM test is located in the VirusTotal integration repository.*
![wazuh install ubuntu 5 kali agent](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/584f029f-ebff-4915-982f-9b041f61371f)
![wazuh install ubuntu 6 kali agent](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/3b01be77-f2ad-416a-a16b-ed5f67ce02af)
![wazuh install ubuntu 5](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/6714fea9-93a1-47ae-9475-4ed1b229530b)
![wazuh install ubuntu 6](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/020160b9-f9f9-401a-a016-66ce514232b6)
