import requests
import json
# Replace with your actual VirusTotal API key
api_key = "<api_key_here>"

# Base URL for the VirusTotal API
base_url = "https://www.virustotal.com/api/v3/files/"

# Get user input for the file hash
file_hash = input("Enter the file hash (SHA-256, SHA-1, or MD5): ")

# Construct the full URL for the API request
url = f"{base_url}{file_hash}"

# Set the headers, including the API key for authentication
headers = {
    "x-apikey": api_key,
    "accept": "application/json"
}

# Make the GET request to VirusTotal API
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract last_analysis_stats
    last_analysis_stats = data.get('data', {}).get('attributes', {}).get('last_analysis_stats', {})

    # Print the last_analysis_stats
    print(json.dumps(last_analysis_stats, indent=4))
else:
    # Handle errors
    print(f"Error: {response.status_code}")
    print(response.text)
