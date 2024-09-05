## Installing and Configuring Snort
Installation on Ubuntu desktop and going through the process of configuring it and also creating rules under ```/etc/snort/rules/local.rules```

### Tools used
- VMware Pro
- Ubuntu Desktop
- Snort
- Snorpy

## Objective
- Gain experience with IDS
- Configure custom rules
- Become familiar with Snort

# Installation
1. On the terminal of the Ubuntu desktop, first make things are updated by running ```sudo apt upgrade```. Then install snort using ```sudo apt install snort```.
During installation, a screen will prompt you to enter the CIDR IP address for the IDS. You can look this up by using the cmd *ip address* and just omit the last block.

<img src="https://github.com/user-attachments/assets/244695b4-5e1e-4028-983e-cf18ef797176" width=600 />

2. Next, check the version of snort to make sure it's installed.

<img src="https://github.com/user-attachments/assets/2bb92951-e1e2-4f68-90fa-89ce201c3ced" width=600 />

3. Now we will set the network adapter to be in promiscuous mode which will allow it to read each packet. The highlighted text will be different because it is the name of the network adapter your machine is using.

<img src="https://github.com/user-attachments/assets/a4f28524-5c84-4bd3-88af-3c87d57da25a" width=600 />


4. We need to set up the ```snort.conf``` file located in ```/etc/snort/```. Here is where we will set the HOME_NET variable IP and also the included rules.

<img src="https://github.com/user-attachments/assets/a712efd0-c2b0-4135-8e0c-b71ff3bead37" width=600 />

5. Now run snort in test mode to validate the configuration.
 <img src="https://github.com/user-attachments/assets/e837e411-37ed-47b7-969a-da6988e62ab0" width=600 />
 <img stc="https://github.com/user-attachments/assets/6dfb543a-1422-49e3-8c1a-eceef5ba2762" width=600 />
 <img src="https://github.com/user-attachments/assets/4edfe0ec-ca27-4571-9f83-72cd213cfed5" width=600 />

# Making rules
1. Navigate to ```/etc/snort/rules/``` edit the ```local.rules``` file. Our first rule will to alert of any ICMP pings.

<img src="https://github.com/user-attachments/assets/1e62e7f9-9bc5-482b-a111-bbeabf376f54" width=600 />

2. Test the rule by running snort

<img src="https://github.com/user-attachments/assets/799622ef-2268-461f-a90a-0ddd0d1b9e5a" width=600 />

- I ping the Ubuntu machine from my Windows machine.
  <img src="https://github.com/user-attachments/assets/c92386df-8f5a-4516-8bc2-5ab884801f62" width=600 />

- Snort alerts us with our rule.

<img src="https://github.com/user-attachments/assets/af14c08c-b166-41c1-8367-ba7af3c528a5" width=600 />

3. Make another rule for SSH login attempts.

   <img src="https://github.com/user-attachments/assets/3b09e607-8d5d-485a-9451-8535b47d47e9" width=600 />

    - The test of the rule below:
     <img src="https://github.com/user-attachments/assets/3687922d-85eb-4852-8076-b17d9e123ef4" width=600 />
     <img src="https://github.com/user-attachments/assets/2bb8b90b-f2a7-49fc-8d73-12f433be1a76" width=600 />

# Conclusion
This was a dive into snort and how to install, configure, and create custom rules. This project will be developed more in the future like how to forward logs to Splunk and so on. Here the knowledge of crafting your own rules and applying them was gained, as well as how to protect endpoints from potentially malicious traffic.
