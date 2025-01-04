import os
import subprocess
import requests

# Environment variables
target = os.getenv("TARGET", "/path/to/code")
defectdojo_url = os.getenv("DEFECTDOJO_URL", "http://localhost:30080")
defectdojo_api_key = os.getenv("DEFECTDOJO_API_KEY", "your-api-key")

result_file = "/tmp/bandit_output.xml"
subprocess.run(["bandit", "-r", target, "-f", "xml", "-o", result_file], check=True)

# Upload to DefectDojo
headers = {"Authorization": f"Token {defectdojo_api_key}"}
files = {"file": open(result_file, "rb")}
data = {
    "scan_type": "Bandit Scan",
    "engagement": "engagement-id"
}
response = requests.post(f"{defectdojo_url}/api/v2/import-scan/", headers=headers, files=files, data=data)
print(f"DefectDojo response: {response.status_code}, {response.text}")
