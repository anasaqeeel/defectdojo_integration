#!/bin/bash
if [ -z "$TARGET" ]; then
    echo "No target specified. Provide TARGET environment variable."
    exit 1
fi

echo "Running nmap on $TARGET..."
# produce XML output
nmap -sV "$TARGET" -oX /tmp/nmap_output.xml

echo "=== NMAP SCAN XML START ==="
cat /tmp/nmap_output.xml
echo "=== NMAP SCAN XML END ==="
