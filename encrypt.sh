#!/usr/bin/env bash
# Re-encrypt the built index.html into docs/ for the password-gated GitHub Pages preview.
# Usage:  STATICRYPT_PASSWORD='the-password' ./encrypt.sh
# The password is NEVER stored in the repo — pass it via the env var each time.
set -euo pipefail
cd "$(dirname "$0")"

: "${STATICRYPT_PASSWORD:?Set STATICRYPT_PASSWORD to the preview password}"

python3 build.py

npx --yes staticrypt index.html \
  -d docs \
  --remember 14 \
  --config staticrypt.config.json

# keep the preview out of search indexes
perl -0pi -e 's/<head>/<head>\n        <meta name="robots" content="noindex, nofollow" \/>/ if !$done++' docs/index.html
printf 'User-agent: *\nDisallow: /\n' > docs/robots.txt
touch docs/.nojekyll

echo "docs/ rebuilt. Commit & push to update the GitHub Pages preview."
