import subprocess
import os
import requests

# Environment variables
target = os.getenv("TARGET", "http://example.com")
defectdojo_url = os.getenv("DEFECTDOJO_URL", "http://10.102.74.156:30080")
defectdojo_api_key = os.getenv("DEFECTDOJO_API_KEY", "your-api-key")

# Run Nuclei scan
output_file = "/tmp/nuclei_output.txt"
subprocess.run(["nuclei", "-u", target, "-o", output_file])

# Upload to DefectDojo
headers = {"Authorization": f"Token {defectdojo_api_key}"}
files = {"file": open(output_file, "rb")}
data = {
    "scan_type": "Nuclei Scan",
    "engagement": 1  # Update with actual engagement ID
}
response = requests.post(f"{defectdojo_url}/api/v2/import-scan/", headers=headers, files=files, data=data)

print(f"DefectDojo response: {response.status_code}, {response.text}")
