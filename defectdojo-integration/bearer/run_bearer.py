import os
import subprocess
import requests

# Environment variables
target = os.getenv("TARGET", "/some/code")
defectdojo_url = os.getenv("DEFECTDOJO_URL", "http://localhost:30080")
defectdojo_api_key = os.getenv("DEFECTDOJO_API_KEY", "your-api-key")

# Run Bearer Scan
result_file = "/tmp/bearer_output.json"
try:
    subprocess.run(["bearer", "scan", target, "--report-file", result_file], check=True)
    print("Bearer scan completed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Bearer scan failed: {e}")
    exit(1)

# Upload Scan Report to DefectDojo
try:
    with open(result_file, "rb") as report:
        headers = {"Authorization": f"Token {defectdojo_api_key}"}
        files = {"file": report}
        data = {
            "scan_type": "Bearer Scan",
            "engagement": 1  # Replace with the actual engagement ID
        }
        response = requests.post(f"{defectdojo_url}/api/v2/import-scan/", headers=headers, files=files, data=data)
        print(f"DefectDojo response: {response.status_code}, {response.text}")
except Exception as e:
    print(f"Failed to upload to DefectDojo: {e}")
