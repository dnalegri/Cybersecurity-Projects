# IP Blocker Script

This script fetches a list of malicious IP addresses from Feodo Tracker and adds firewall rules to block both inbound and outbound traffic for these IPs on a Windows machine.

## Prerequisites

- Python 3.x installed on your system
- Administrator privileges (required to modify firewall rules)

The script will:
 - Fetch the list of IP addresses from Feodo Tracker.
 - Delete any existing firewall rules named 'BadIP_Inbound' and 'BadIP_Outbound'.
 - Add new firewall rules to block both inbound and outbound traffic for the listed IP addresses.

## How It Works

1. **Fetching IP Addresses**:
    - The script sends a GET request to Feodo Tracker to download a CSV file containing the list of IP addresses.

2. **Processing the CSV**:
    - The script reads the CSV file, filters out comments, and validates the IP addresses.

3. **Managing Firewall Rules**:
    - Deletes any existing firewall rules named 'BadIP_Inbound' and 'BadIP_Outbound'.
    - Adds new firewall rules to block both inbound and outbound traffic for the valid IP addresses.

## Example Output

No rules match the specified criteria.

No rules match the specified criteria.

Added Rule to block IPs: 192.9.135.73,172.234.244.189,172.232.188.170,172.232.185.9

Ok.

Ok.
