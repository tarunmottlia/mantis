---
license: cc-by-4.0
language:
- en
pretty_name: India local business website gap 2026 (aggregated)
size_categories:
- 1K<n<10K
tags:
- india
- local-business
- google-maps
- small-business
- websites
- tabular
---

# India local business website gap 2026 (aggregated)

What share of active Google Maps business listings in Indian cities list a website, broken down by
city and business category. Published by [Mantis](https://mantisai.in?utm_source=github&utm_medium=guest&utm_campaign=gp) as the data companion to the report
**[India local business website gap 2026](https://mantisai.in/resources/india-local-business-website-gap-2026?utm_source=github&utm_medium=guest&utm_campaign=gp)**.

DOI: [10.5281/zenodo.24233108](https://doi.org/10.5281/zenodo.24233108) (Zenodo).

Only aggregate statistics are published here. The dataset has no business names, phone numbers, emails,
addresses, coordinates, place IDs or per-business rows.

## Files

| File | Rows | Columns |
|---|---|---|
| `india_city_category_website_gap_2026.csv` | 1,083 | `city, category, listings_count, share_with_website, share_without_website, method_date` |
| `india_city_website_gap_2026.csv` | 19 | `city, listings_count, share_with_website, share_without_website, method_date` |
| `eda_website_gap.ipynb` | — | pandas EDA: sample size, city ranking, category ranking, spread of each category across cities |
| `build_aggregates.py` | — | the script that turns the private snapshot into these aggregates (thresholds included) |

- `listings_count`: unique operational listings checked in that city (and category).
- `share_with_website`: fraction of those listings with anything in the Google listing's website field (0 to 1).
- `share_without_website`: `1 - share_with_website`.
- `method_date`: date the listings were scanned (ISO 8601).
- `category`: the listing's Google Places primary type, title-cased (for example `Hardware Store`). `Uncategorised` = no primary type on the listing.

## Method

- **Source**: a snapshot of the Mantis index, collected through the Google Places API (licensed access, not scraping).
- **Scan date**: 31 August 2026.
- **Coverage**: 19 Indian cities (Ahmedabad, Bengaluru, Chandigarh, Chennai, Coimbatore, Delhi, Faridabad, Gurugram,
  Hyderabad, Indore, Jaipur, Kolkata, Kota, Lucknow, Morena, Mumbai, Noida, Pune, Surat). Each city was scanned with a fixed set of category search phrases.
- **Sample size**: 96,287 unique listings with business status `OPERATIONAL`, deduplicated by place ID.
  82,481 of them fall in the 1,083 published city × category cells. The rest sit in suppressed small cells, but they still count in the city totals.
- **Thresholds**: cities with fewer than 400 listings are excluded (none were in this snapshot). City × category
  cells with fewer than 30 listings are suppressed.
- **Website rule**: a listing counts as "with website" whenever its website field is non-empty, including a
  Facebook page, a directory profile or a dead domain. The no-website share is therefore a conservative (low) estimate.

## Limits

- This is a sample of our index, not a census. The category mix in each city reflects the phrases we scanned.
  A city's rate partly reflects where and what we scanned, not only the city itself.
- The [live report](https://mantisai.in/resources/india-local-business-website-gap-2026?utm_source=github&utm_medium=guest&utm_campaign=gp) reads the current Mantis index
  (later and larger, more cities), so its figures differ somewhat from this 31 Aug 2026 snapshot.
- A listing with no website is not necessarily a business without an online presence (it may use social pages or marketplaces).

## Headline numbers (this snapshot)

- Pooled across 19 cities, 37.5% of listings checked show no website.
- The highest no-website share is in Morena (79.6%) and Kota (62.2%). The lowest is in Bengaluru (25.3%), Mumbai (27.0%) and Delhi (27.9%).
- Among categories with 300+ listings, the highest no-website shares are in Guest House (77.6%), Barber Shop (73.7%) and Hardware Store (73.3%).
  The lowest are in Finance (13.9%), Preschool (14.5%) and Jewelry Store (14.5%).

## License

The aggregate tables, notebook and script are released under **CC BY 4.0** by Mantis. The underlying listing data is
Google Maps content and is **not** included or redistributed.

## Citation

> Mantis (2026). *India local business website gap 2026* (aggregated dataset). Scanned 31 August 2026.
> https://doi.org/10.5281/zenodo.24233108

```bibtex
@misc{mantis_india_website_gap_2026,
  author = {{Mantis}},
  title  = {India local business website gap 2026 (aggregated dataset)},
  year   = {2026},
  doi    = {10.5281/zenodo.24233108},
  url    = {https://doi.org/10.5281/zenodo.24233108},
  note   = {Google Maps listings scanned 31 August 2026; CC BY 4.0}
}
```

Questions or corrections: open an issue on [tarunmottlia/mantis](https://github.com/tarunmottlia/mantis/issues), or see https://mantisai.in.

I'm Tarun, founder of Mantis.
