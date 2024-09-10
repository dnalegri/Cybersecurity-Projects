## Integrating Splunk with Snort
I will be walking through the process of forwarding alert logs to Splunk. You will need to create an account on the Splunk website and then you can download the forwarder and extract it.
1. Move the splunkforwarder to the ```/opt``` directory. Install using ```sudo apt install```

<img src="https://github.com/user-attachments/assets/e229e056-b5b4-441f-8a9a-fb0f0f01f635" width=600 />

2. Navigate to ```/opt/splunkforwarder/bin```
<img src="https://github.com/user-attachments/assets/33b9e330-4aaf-4ec5-b9c8-e2c070d08d43" width=600 />

3. Start splunk using ```sudo ./splunk start --accept-license```. Create the username and password. It will be successfully installed with the message below.
<img src="https://github.com/user-attachments/assets/a6db1f24-37a2-4719-adf1-ef622efe2fc8" width=600 />
<img src="https://github.com/user-attachments/assets/fade46da-1411-4524-bc10-4a23cdc54c87" width=600 />

4. Add the forward server. For my lab, I will be using a host machine to view the logs. You may also use an actual server but in my case, it's technically a receiving indexer. Be sure to add the correct IP.
   - *Note*: I used ipconfig on my host machine and accidentally entered in the wrong IP on my Ubuntu forwarder (*Whoops*) ! It's okay because this can be modified using
   -  ```/opt/splunkforwarder/bin/splunk remove forward-server <old_indexer_IP>:<port>```
   -  and then, ```/opt/splunkforwarder/bin/splunk add forward-server <new_indexer_IP>:<port> -auth <username>:<password>```
   -   You can also verify your forward server with the cmd: ```/opt/splunkforwarder/bin/splunk list forward-server```

<img src="https://github.com/user-attachments/assets/d4443dbe-2d7a-432c-976f-5d626455bdf4" width=600 />

5. Navigate to ```/opt/splunkforwarder/etc/system/local```. Edit the outputs.conf file and make sure the IP matches your forward server and the port.
<img src="https://github.com/user-attachments/assets/aa2f097b-2483-4f99-9378-0aafd5143ae7" width=600 />

- It will look  like this:
```
  [tcpout]
  defaultGroup = default-autolb-group

  [tcpout:default-autolb-group]
  server = 192.168.0.0:9997

  [tcpout-server://192.168.0.0:9997]
```
6. We will add the monitor.
   - *Note:* At first I wanted full alerts but this led to Splunk not receiving data so I changed it to ```/snort/snort.alert.fast```
     <img src="https://github.com/user-attachments/assets/3f64b269-c98b-4091-82ce-b0c2c7869007" width=600 />

8. Configure the inputs.conf file next. Navigate to ```/opt/splunkforwarder/etc/apps/search/local```
<img src="https://github.com/user-attachments/assets/1426d03f-b668-4174-96ce-2ca2fee3e55a" width=600 />

- For my configuration, I want the snort.alert.fast logs, so it will look like this (this can also be modified if you are having an error and not receiving the data):

  <img src="https://github.com/user-attachments/assets/e1983bf2-82e1-4e81-b2c2-ff8e0888a43d" width=600 />

## Viewing Splunk logs
On your host/forward server, you will need to install Splunk Enterprise. Login there and navigate to forwarding and receiving. Under receiving, make sure the port you set (default port 9997) is set to receive data, otherwise you will not receive anything. In case of any firewall issues blocking the data, you can set an incoming rule for port 9997 and that specific IP of your forwarding machine.

- A successful integration will display your forwarding machine under **Data Summary** in the Search & Reporting tab.
  <img src="https://github.com/user-attachments/assets/5df72d71-2cc6-4d90-b510-a6c64bfd6216" width=600 />
  <img src="https://github.com/user-attachments/assets/71fc56c2-5e7d-4ec6-b123-2f9cb30702b4" width=600 />
  <img src="https://github.com/user-attachments/assets/6f7cb86e-d4d5-4970-87c3-04dc795997f4" width=600 />

# Conclusion
  - Now I can view the alerts under ``index=main sourcetype=snort_alert_fast``
    <img src="https://github.com/user-attachments/assets/4ad8940c-e8eb-42cb-870f-78fbf7f8f10a" width=800 />
