#!/bin/bash
if [ -z "$TARGET" ]; then
  echo "No path specified for Bandit."
  exit 1
fi

echo "Running bandit on $TARGET..."
bandit -r "$TARGET" -f xml -o /tmp/bandit_output.xml

echo "=== BANDIT XML START ==="
cat /tmp/bandit_output.xml
echo "=== BANDIT XML END ==="
