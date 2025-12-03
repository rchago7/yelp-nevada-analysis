import json
import csv

INPUT_FILE = "yelp_academic_dataset_business.json"
OUTPUT_FILE = "yelp_business.csv"

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
    with open(INPUT_FILE, "r", encoding="utf-8") as fin, \
         open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as fout:
        
        writer = csv.DictWriter(fout, fieldnames=FIELDNAMES)
        writer.writeheader()
        
        for line in fin:
            line = line.strip()
            if not line:
                continue
            
            data = json.loads(line)
            row = {}

            for col in FIELDNAMES:
                row[col] = data.get(col, None)

            cats = data.get("categories", None)
            row["categories"] = cats

            writer.writerow(row)
            total += 1

            if total % 100000 == 0:
                print(f"Processed {total} businesses...")

    print(f"Done. Wrote {total} rows to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
