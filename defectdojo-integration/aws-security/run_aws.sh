#!/bin/bash


echo "Running some AWS checks..."

# Example: get credential report
aws iam get-credential-report --output json > /tmp/iam_credential_report.json

echo "=== AWS REPORT START ==="
cat /tmp/iam_credential_report.json
echo "=== AWS REPORT END ==="
