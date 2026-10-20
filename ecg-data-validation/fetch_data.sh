#!/usr/bin/env bash
# Download the MIT-BIH records listed in records.txt into data/ (header, signal, annotation files).
set -euo pipefail
cd "$(dirname "$0")"
BASE=https://physionet-open.s3.amazonaws.com/mitdb/1.0.0   # PhysioNet open-data mirror (physionet.org is slow)
mkdir -p data
grep -v '^#' records.txt | awk 'NF {print $1}' | while read -r rec; do
    for ext in hea dat atr; do
        [ -f "data/$rec.$ext" ] || curl -sfo "data/$rec.$ext" "$BASE/$rec.$ext"
    done
    echo "$rec"
done
