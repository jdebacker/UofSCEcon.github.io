# UofSCEcon.github.io

Website for the Department of Economics at the University of South Carolina.

## Active pages

- `index.html`
- `faculty.html`
- `research.html`
- `events.html`
- `phd_students.html`
- `job_market_candidates.html`
- `contact.html`

## Maintenance check

Run the local HTML audit after content changes:

```sh
./Scripts/check_site.sh
```

The script checks for:

- missing local links and assets
- missing titles, meta descriptions, and `<h1>` headings
- `target="_blank"` links without a `rel` attribute
- placeholder page titles left over from the template
