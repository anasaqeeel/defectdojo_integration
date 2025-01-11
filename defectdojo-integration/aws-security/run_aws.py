import boto3
import json
import os

# AWS Environment Variables
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID", "your-aws-access-key")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "your-aws-secret-key")
AWS_REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")

# DefectDojo API Placeholder
DEFECTDOJO_API_KEY = "your_api_key"
DEFECTDOJO_API_URL = "http://defectdojo/api/v2/import-scan/"
ENGAGEMENT_ID = 1  # Replace with actual engagement ID


def run_aws_checks():
    print("Running AWS checks...")

    # client for IAM
    client = boto3.client(
        "iam",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION,
    )

    # Fetch credential report
    response = client.get_credential_report()
    report_content = response["Content"].decode("utf-8")

    # Save the report to a file
    report_path = "/tmp/iam_credential_report.json"
    with open(report_path, "w") as file:
        file.write(report_content)

    print(f"Report saved to {report_path}")
    return report_path


def upload_to_defectdojo(report_path):
    print("Uploading report to DefectDojo...")
    headers = {"Authorization": f"Token {DEFECTDOJO_API_KEY}"}
    with open(report_path, "rb") as report_file:
        files = {"file": report_file}
        data = {
            "scan_type": "AWS IAM Credential Report",
            "engagement": ENGAGEMENT_ID,
        }
        response = requests.post(DEFECTDOJO_API_URL, headers=headers, files=files, data=data)

        if response.status_code == 201:
            print("Report uploaded successfully!")
        else:
            print(f"Failed to upload report: {response.status_code} - {response.text}")


if __name__ == "__main__":
    report_path = run_aws_checks()
    # Uncomment the next line to enable DefectDojo integration
    # upload_to_defectdojo(report_path)
