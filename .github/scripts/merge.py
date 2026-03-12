import json
from pathlib import Path

folder = Path("geojson-israel-municipalities")
output_file = Path("all_municipalities.geojson")

features = []
files_processed = 0

for file in folder.rglob("*.geojson"):
    try:
        with open(file, encoding="utf-8") as f:
            data = json.load(f)

            if data.get("type") == "Feature":
                features.append(data)
            elif data.get("type") == "FeatureCollection":
                features.extend(data.get("features", []))

        files_processed += 1
    except Exception as e:
        print(f"Error in file {file.name}: {e}")

print(f"Processing {files_processed} files → {len(features)} municipalities")

merged = {"type": "FeatureCollection", "features": features}

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(merged, f, ensure_ascii=False, separators=(",", ":"))

size_mb = output_file.stat().st_size / (1024 * 1024)
print(f"✅ Created: {output_file} ({size_mb:.1f} MB)")
