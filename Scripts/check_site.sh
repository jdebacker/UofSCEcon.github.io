#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

HTML_FILES=(
  index.html
  faculty.html
  research.html
  events.html
  phd_students.html
  job_market_candidates.html
  contact.html
)

echo "Checking HTML pages..."

echo
echo "1. Missing local links and assets"
perl -0ne '
  my $content = $_;
  $content =~ s{<!--.*?-->}{}gs;
  while ($content =~ /(?:href|src)="([^"]+)"/g) {
    my $u = $1;
    next if $u =~ m{^(https?:)?//};
    next if $u =~ m{^(mailto:|tel:|#|javascript:)};
    next if $u =~ /^data:/;
    next if $u =~ m{^/_internal/};
    $u =~ s/#.*$//;
    $u =~ s/\?.*$//;
    next if $u eq q{};
    print "$ARGV:$u\n" unless -e $u;
  }
' "${HTML_FILES[@]}" || true

echo
echo "2. Missing title, description, or h1"
for file in "${HTML_FILES[@]}"; do
  grep -q "<title>" "$file" || echo "$file: missing <title>"
  grep -q 'name="description"' "$file" || echo "$file: missing meta description"
  grep -q "<h1" "$file" || echo "$file: missing <h1>"
done

echo
echo "3. target=\"_blank\" links without rel"
rg -n '<a(?![^>]*\brel=)[^>]*target="_blank"' "${HTML_FILES[@]}" -P || true

echo
echo "4. Generic placeholder titles"
rg -n '<title>Darla Moore School of Business: </title>' "${HTML_FILES[@]}" || true

echo
echo "Check complete."
