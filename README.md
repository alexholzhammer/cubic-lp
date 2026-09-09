# cubic-lp

Landing page for **Cubic Outdoor Living** — a single-purpose page advertising the
*White Stripes* case study and collecting emails to send it (double opt-in → PDF).

Dark, minimal, one message per section:

**Hero → In detail (gallery) → What's inside → Quote → Craft pause → Built for planners → Email capture**

## Files

| File | Purpose |
|------|---------|
| `index.html` | The deliverable — a single self-contained file (images + logo inlined as data URIs). Open it directly in a browser. |
| `src.html` | Editable source, with `{{TOKEN}}` placeholders for the assets. |
| `build.py` | Inlines the local assets into `src.html` and writes `index.html`. |
| `hero-landscape.jpg` / `hero-vertical.jpg` | Hero images (converted from the original `.avif`). |
| `t1–t4.jpg` | Gallery images, downscaled from `project-tile-*.jpg`. |
| `our-story.jpg` | Full-bleed image for the craft/pause section. |
| `Logo.svg` | Cubic wordmark (white). |

## Working on it

```bash
# edit src.html, then rebuild the self-contained index.html
python3 build.py

# preview locally
python3 -m http.server 8000
# open http://localhost:8000/index.html
```

## Client preview (password-gated)

Live at **https://alexholzhammer.github.io/cubic-lp/** — GitHub Pages, served
from `main` `/docs`. `docs/index.html` is a StatiCrypt-encrypted copy of the
page: visitors get a password prompt, wrong password shows nothing. `noindex`
meta + `robots.txt` keep it out of search.

The repo is **public** (required for Pages on the free plan), so the source
files here are visible — only the deployed preview URL is gated.

To update the preview after editing the page:

```bash
STATICRYPT_PASSWORD='verge-dune-cobalt-quartz' ./encrypt.sh
git add -A && git commit -m "update preview" && git push
```

Change the password by passing a different `STATICRYPT_PASSWORD` (it is never
stored in the repo — only a salt is, in `staticrypt.config.json`).

## Not done yet

- Footer (logo, legal links, socials)
- Mobile pass
- Wire the email form to a real ESP / double-opt-in backend — the current submit
  handler is a front-end simulation only (see the script at the bottom of `src.html`).
- Replace the placeholder quote ("John Doe · Eggersmann Studios") with a real one.
