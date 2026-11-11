# Joe Bogdan Speaker Page

Speaker page for Joe Bogdan, Chief Learning Officer at C2H (Connecting Heads to Hearts), built for the C2H keynote speakers section at c2htransform.com.

- **Live:** https://joe-bogdan-speaker.netlify.app. Netlify deploys automatically on every push to `main`.
- **Audit:** see [`AUDIT.md`](AUDIT.md) for the UX/accessibility/performance audit, change log and open recommendations.

This repository is the single source of truth. The Netlify site and the Claude artifact preview are both published from `index.html` here.

## What's here

| Path | Purpose |
|---|---|
| `index.html` | The full page. Styles and scripts are inline, and fonts load from Google Fonts. |
| `img/joe-headshot-suit-{480,900}.webp` | Hero portrait (preloaded) |
| `img/joe-portrait-city-{480,900}.webp` | About section portrait |
| `img/joe-headshot-casual-{480,900}.webp` | Podcast card |
| `img/book-cover.webp` | *Better Has No Finish Line* cover |
| `img/c2h-wolf-80.webp` | C2H wolf mark (header, About, footer) |
| `img/favicon-64.png` | Browser tab icon |
| `img/og-joe-bogdan.jpg` | 1200×630 social share preview |
| `AUDIT.md` | Audit report |

## Design

- **Joe's palette leads the story sections:** deep teal `#06364A`, green `#7DC279` for headlines and accents, aqua `#01A09F` as the secondary accent, and white text.
- **C2H frames the page:** navy header, booking section and footer; Montserrat and Open Sans; 14 px radius.
- **One call-to-action color:** every primary button is Joe's green with deep-teal text.
- **Links:** links to c2htransform.com open in the same tab. External links open a new tab and say so to screen readers.
- **Works everywhere:** light and dark mode, phone through desktop, keyboard and screen readers (axe: 0 violations; Lighthouse accessibility 100), and reduced motion.

## Keeping the copies in sync

`index.html` here is the source. Netlify deploys it on every push to `main`. To refresh the Claude artifact preview:

```bash
python3 scripts/build-artifact.py
```

Then republish the generated file.

## Other files

| Path | Purpose |
|---|---|
| `_headers` | Netlify security headers (CSP and others) and 30-day image caching |
| `robots.txt`, `sitemap.xml` | Crawl instructions and the page URL for search engines |
| `thanks/index.html` | Confirmation page for inquiries sent without JavaScript |
| `AUDIT-2.md` | Deep audit (SEO, conversion, security, ops) and skills map |

## Speaking inquiries

The booking form is a Netlify Form named `speaking-inquiry`, intended for c2hinfo@c2htransform.com. Submissions appear under **Netlify → joe-bogdan-speaker → Forms**. Email alerts to c2hinfo@ are turned on there under **Form notifications**.

## Preview locally

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Adding it to c2htransform.com

The page carries its own header, footer, skip link and status region so it can stand alone. When it moves under `/speakers`:

1. Keep the site's own header and footer. Remove this page's `<nav class="nav">` (which includes the mobile menu `#mnav`) and its `<footer>`, and point the skip link at the site's main content.
2. Keep `<p class="sr" role="status" id="live">`. The copy buttons use it to announce "Copied".
3. Make links to other C2H pages open in the same tab. External links (BookBaby, Spotify, LinkedIn) can stay `target="_blank"`.
4. Booking inquiries are drafted to c2hinfo@c2htransform.com.
