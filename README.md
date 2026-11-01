# Joe Bogdan Speaker Page

Speaker page for Joe Bogdan, Chief Learning Officer at C2H (Connecting Heads to Hearts), built for the C2H keynote speakers section at c2htransform.com.

## What's here

- `index.html`: the full page, self-contained (styles and scripts inline; fonts load from Google Fonts)
- `img/`: headshots, book cover, and the C2H wolf mark

## Design

- Joe's palette leads the story sections: deep teal `#06364A`, green `#7DC279` for headlines and accents, aqua `#01A09F` as the secondary accent, white text.
- C2H frames the page: navy header, booking section and footer; C2H blue only on C2H actions; Montserrat and Open Sans.
- Works in light and dark mode, and down to phone width.

## Preview locally

Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8000
```

## Adding it to c2htransform.com

The page includes its own header and footer so it can stand alone. When it goes under `/speakers`, drop the page's `<nav class="nav">` and `<footer>` and keep the site's own. Booking inquiries are drafted to c2hinfo@c2htransform.com.
