import os
import requests

H1_API_TOKEN = os.getenv("H1_API_TOKEN", "YOUR_TOKEN")
DD_API_KEY = os.getenv("DD_API_KEY", "YOUR_DD_API_KEY")
DD_URL = os.getenv("DD_URL", "http://defectdojo-service")

def fetch_hackerone_reports():
    # Example: Fetch HackerOne reports
    headers = {"Authorization": f"Bearer {H1_API_TOKEN}"}
    response = requests.get(f"{DD_URL}/api/v2/reports", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch reports")

def import_into_defectdojo(reports):
    headers = {"Authorization": f"Token {DD_API_KEY}"}
    for report in reports:
        response = requests.post(f"{DD_URL}/api/v2/import-scan/", headers=headers, json=report)
        print(f"Imported report: {response.status_code}")

if __name__ == "__main__":
    reports = fetch_hackerone_reports()
    import_into_defectdojo(reports)
