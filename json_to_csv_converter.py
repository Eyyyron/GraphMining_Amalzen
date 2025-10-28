import ijson
import csv
import json
import os

# CONFIGURATION
JSON_FILE = "arxiv-metadata-oai-snapshot.json"   # your input file name
OUTPUT_FILE = "raw_dataset(full).csv"          # output CSV name
MAX_ROWS = None                                 # preview limit; set to None for all records


# FUNCTION: flatten nested values for CSV safety
def flatten_value(v):
    """Convert nested lists/dicts into JSON text so CSV stays readable."""
    if isinstance(v, (dict, list)):
        try:
            return json.dumps(v, ensure_ascii=False)
        except Exception:
            return str(v)
    return v


# STEP 1: discover all available top-level fields
fields = set()

with open(JSON_FILE, "r", encoding="utf-8") as f:
    for i, record in enumerate(ijson.items(f, "", multiple_values=True)):
        fields.update(record.keys())
        if i >= 100:   # check first 100 items to learn the schema
            break

fields = sorted(fields)
print(f"Detected {len(fields)} columns:\n{fields}\n")


# STEP 2: stream through the file and write CSV
os.makedirs(os.path.dirname(OUTPUT_FILE) or ".", exist_ok=True)

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()

    with open(JSON_FILE, "r", encoding="utf-8") as f:
        for i, record in enumerate(ijson.items(f, "", multiple_values=True)):
            flat_record = {k: flatten_value(record.get(k, "")) for k in fields}
            writer.writerow(flat_record)

            if (i + 1) % 1000 == 0:
                print(f"Processed {i + 1} records...")

            if MAX_ROWS is not None and i >= MAX_ROWS - 1:
                break

print(f"\n Done! CSV saved as: {OUTPUT_FILE}")
