#!/bin/bash

if [ -z "$TARGET" ]; then
  echo "No path specified for Bearer."
  exit 1
fi

echo "Running bearer scan on $TARGET..."
bearer scan "$TARGET" --report-file /tmp/bearer_output.json

echo "=== BEARER JSON START ==="
cat /tmp/bearer_output.json
echo "=== BEARER JSON END ==="
