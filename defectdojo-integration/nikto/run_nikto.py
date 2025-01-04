import subprocess
import requests
import os

target = os.getenv("TARGET", "example.com")

# Run Nikto
command = ["nikto", "-h", target, "-o", "/tmp/nikto_output.xml", "-Format", "xml"]
subprocess.run(command)

# Upload to DefectDojo
api_key = os.getenv("DD_API_KEY", "your-defectdojo-token")
headers = {"Authorization": f"Token {api_key}"}
url = os.getenv("DD_URL", "http://defectdojo-service/api/v2/import-scan/")
files = {"file": open("/tmp/nikto_output.xml", "rb")}
data = {
    "scan_type": "Nikto Scan",
    "engagement": 1  # to be Replaced with actual engagement ID
}
response = requests.post(url, headers=headers, files=files, data=data)
print(response.json())
