#!/bin/bash
if [ -z "$TARGET" ]; then
  echo "No target specified."
  exit 1
fi

echo "Running nuclei on $TARGET..."
nuclei -u "$TARGET" -o /tmp/nuclei_output.txt

echo "=== NUCLEI START ==="
cat /tmp/nuclei_output.txt
echo "=== NUCLEI END ==="
