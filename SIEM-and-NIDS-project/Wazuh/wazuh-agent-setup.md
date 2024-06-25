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
