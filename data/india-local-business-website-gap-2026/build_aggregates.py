"""Build the aggregated India website-gap tables from a Mantis Places snapshot.

Input : a Mantis places.ndjson snapshot (Google Places API results; NOT redistributed).
Output: city x category and city-level aggregate CSVs only. No names, phones, emails,
        addresses, coordinates, place IDs or any per-business row leave this script.
Usage : python3 build_aggregates.py /path/to/places.ndjson
"""
import csv, json, sys, collections, os

MIN_CITY = 400   # cities with fewer checked listings are dropped (small samples swing)
MIN_CELL = 30    # city x category cells with fewer listings are suppressed

src = sys.argv[1]
out = os.path.dirname(os.path.abspath(__file__))
seen, cell, city = set(), collections.Counter(), collections.Counter()
cell_w, city_w, dates = collections.Counter(), collections.Counter(), []
for line in open(src, encoding="utf-8"):
    r = json.loads(line)
    if r.get("scanned_country") != "in" or r.get("business_status") != "OPERATIONAL":
        continue
    if r["place_id"] in seen:
        continue
    seen.add(r["place_id"])
    c = r["scanned_city"].strip().lower()
    k = (c, (r.get("primary_type") or "unknown").strip().lower())
    has = 1 if (r.get("website") or "").strip() else 0
    cell[k] += 1; cell_w[k] += has; city[c] += 1; city_w[c] += has
    dates.append(r["scanned_at"][:10])

method_date = max(dates)
first_date = min(dates)
RENAME = {"bangalore": "Bengaluru", "gurgaon": "Gurugram", "unknown": "Uncategorised"}
pretty = lambda s: RENAME.get(s) or s.replace("_", " ").replace("-", " ").title()
keep = {c for c, n in city.items() if n >= MIN_CITY}

with open(os.path.join(out, "india_city_category_website_gap_2026.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["city", "category", "listings_count", "share_with_website", "share_without_website", "method_date"])
    rows = [(pretty(c), pretty(t), n, round(cell_w[(c, t)] / n, 4))
            for (c, t), n in cell.items() if c in keep and n >= MIN_CELL]
    for c, t, n, s in sorted(rows, key=lambda x: (x[0], -x[2])):
        w.writerow([c, t, n, f"{s:.4f}", f"{1 - s:.4f}", method_date])

with open(os.path.join(out, "india_city_website_gap_2026.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["city", "listings_count", "share_with_website", "share_without_website", "method_date"])
    for c in sorted(keep, key=lambda c: city_w[c] / city[c]):
        s = city_w[c] / city[c]
        w.writerow([pretty(c), city[c], f"{s:.4f}", f"{1 - s:.4f}", method_date])

print(json.dumps({"india_operational_unique": len(seen), "cities_all": len(city),
                  "cities_kept": len(keep), "listings_in_kept_cities": sum(city[c] for c in keep),
                  "cells_kept": len(rows), "listings_in_kept_cells": sum(r[2] for r in rows),
                  "scan_window": [first_date, method_date],
                  "overall_share_with_website": round(sum(city_w.values()) / len(seen), 4)}))
