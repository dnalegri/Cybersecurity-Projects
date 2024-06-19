import requests, csv, subprocess, re

# A GET request to the website
response = requests.get("https://feodotracker.abuse.ch/downloads/ipblocklist.csv").text

# Delete existing firewall rules named 'BadIP_Inbound' and 'BadIP_Outbound'
delete_rule_inbound = ["netsh", "advFirewall", "firewall", "delete", "rule", "name=BadIP_Inbound"]
delete_rule_outbound = ["netsh", "advFirewall", "firewall", "delete", "rule", "name=BadIP_Outbound"]
subprocess.run(delete_rule_inbound, shell=False)
subprocess.run(delete_rule_outbound, shell=False)

# Validate IP address using regex
def is_valid_ip(ip):
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return ip_pattern.match(ip)

# Read and process CSV data, filtering out comments
mycsv = csv.reader(filter(lambda x: not x.startswith('#'), response.splitlines()))

# Collect all valid IPs
ip_list = []
for row in mycsv:
    ip = row[1]
    if ip and ip != "dst_ip" and is_valid_ip(ip):
        ip_list.append(ip)

# Create one rule to block all IPs for inbound and outbound traffic
if ip_list:
    ip_range = ','.join(ip_list)
    print("Added Rule to block IPs:", ip_range)

    # Add rule for outbound traffic
    add_rule_outbound = [
        "netsh", "advFirewall", "firewall", "add", "rule",
        "name=BadIP_Outbound",
        "Dir=Out", "Action=Block", f"RemoteIP={ip_range}"
    ]
    subprocess.run(add_rule_outbound, shell=False)

    # Add rule for inbound traffic
    add_rule_inbound = [
        "netsh", "advFirewall", "firewall", "add", "rule",
        "name=BadIP_Inbound",
        "Dir=In", "Action=Block", f"RemoteIP={ip_range}"
    ]
    subprocess.run(add_rule_inbound, shell=False)
