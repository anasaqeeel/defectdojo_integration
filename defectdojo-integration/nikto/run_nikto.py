import subprocess
import requests

# Define target
target = "example.com"

# Run Nikto
command = ["nikto", "-h", target, "-o", "/tmp/nikto_output.xml", "-Format", "xml"]
subprocess.run(command)

# Print the report
with open("/tmp/nikto_output.xml", "r") as file:
    nikto_output = file.read()
print("Nikto Output:\n", nikto_output)

# Upload to DefectDojo
api_key = "your_api_key"
headers = {"Authorization": f"Token {api_key}"}
url = "http://localhost:8080/api/v2/import-scan/"
files = {"file": open("/tmp/nikto_output.xml", "rb")}
data = {
    "scan_type": "Nikto Scan",
    "engagement": 1  # Replace with actual engagement ID
}
response = requests.post(url, headers=headers, files=files, data=data)
print(response.json())
