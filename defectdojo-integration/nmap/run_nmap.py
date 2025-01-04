import subprocess
import requests
import os

# Define target
target = os.getenv("TARGET", "scanme.nmap.org")

# Run Nmap
command = ["nmap", "-sV", target, "-oX", "/tmp/nmap_output.xml"]
subprocess.run(command)

# Upload to DefectDojo
api_key = os.getenv("DD_API_KEY", "your-defectdojo-token")
headers = {"Authorization": f"Token {api_key}"}
url = os.getenv("DD_URL", "http://defectdojo-service/api/v2/import-scan/")
files = {"file": open("/tmp/nmap_output.xml", "rb")}
data = {
    "scan_type": "Nmap Scan",
    "engagement": 1  # Replace with actual engagement ID
}
response = requests.post(url, headers=headers, files=files, data=data)
print(response.json())
