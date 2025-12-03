"""
convert_business_to_csv.py
CIS 4560 - Yelp Nevada Analysis
Author: Ruben Chagollan (rchagol6)

Description:
This script converts the Yelp Open Dataset (business subset)
from JSON format into CSV for easier loading into Hive and HDFS.
"""

import json
import csv

# Input and output filenames
INPUT_FILE = "yelp_academic_dataset_business.json"
OUTPUT_FILE = "yelp_business.csv"

# Columns we extract from JSON
FIELDNAMES = [
    "business_id",
    "name",
    "address",
    "city",
    "state",
    "postal_code",
    "latitude",
    "longitude",
    "stars",
    "review_count",
    "is_open",
    "categories"
]

def main():
    total = 0

    print("Starting conversion...")

    with open(INPUT_FILE, "r", encoding="utf-8") as fin, \
         open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as fout:

        writer = csv.DictWriter(fout, fieldnames=FIELDNAMES)
        writer.writeheader()

        for line in fin:
            if not line.strip():
                continue

            data = json.loads(line)
            
            # Extract necessary fields into a CSV row
            row = {col: data.get(col) for col in FIELDNAMES}

            writer.writerow(row)
            total += 1

            if total % 100000 == 0:
                print(f"Processed {total:,} rows...")

    print(f"Done! Wrote {total:,} rows to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
