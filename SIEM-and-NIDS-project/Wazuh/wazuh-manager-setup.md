## Install Wazuh Manager on Ubuntu Desktop
1. **Run the assisted installation script:**
    ```sh
    curl -sO https://packages.wazuh.com/4.8/wazuh-install.sh && sudo bash ./wazuh-install.sh -a
2. **Access the Wazuh Dashboard:**

- Use the generated admin password to log in at your server IP:
    
  ```sh
    https://<wazuh-dashboard-ip>

*Note: The only error encountered during this process was initially installing Wazuh and getting a storage error. This was remedied by increasing the partition. The installation went as expected.*
## Documentation
With a successful install, the dashboard loads upon admin login. (Agent setup is after this process).

![wazuh install ubuntu 2](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/92483b7c-a7a7-4875-9d3a-be0031ded23c)
![wazuh install ubuntu 3](https://github.com/dnalegri/Cybersecurity-Projects/assets/164395911/b3da4ac4-a22a-4d9c-b18a-c7dcbf177954)
