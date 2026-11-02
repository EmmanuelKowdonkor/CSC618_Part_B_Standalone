#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
python3 part_b.py
echo "SUCCESS: See results/part_b_per_query.csv and results/part_b_summary.json"
