# UX / UI Audit: Joe Bogdan Speaker Page

- **Site:** https://joe-bogdan-speaker.netlify.app (repo `kcastille3324/Joe-Speaker-Page-`, single page `index.html`)
- **Audited:** 1 November 2026
- **Method:**
  - axe-core 4.10 (WCAG 2.0/2.1/2.2 A and AA plus best practices) at desktop (1440, light and dark), tablet (820) and mobile (390).
  - Lighthouse 12.2.1, mobile and desktop presets.
  - Scripted keyboard and interaction tests in Chromium.
  - Image, font, heading and landmark inventories.
  - Manual review against the C2H brand rules and Joe's palette.

## Results at a glance

| Metric | Before | After |
|---|---|---|
| axe violations (any viewport) | 4 rule types, 28 nodes | **0** |
| Lighthouse Accessibility (mobile / desktop) | 98 / 98 | **100 / 100** |
| Lighthouse Performance (mobile / desktop) | 76 / 91 | **81 / 99** |
| LCP (mobile / desktop) | 4.4 s / 1.4 s | **3.7 s / 0.9 s** |
| Page weight (mobile / desktop) | 437 KiB / 522 KiB | **257 KiB / 216 KiB** |
| CLS | 0.003 | 0.005 (still "good") |
| Best Practices / SEO | 100 / 100 | 100 / 100 |
| Section navigation on phones and tablets | None | Menu |

## 1. Audit report

Severity: **Critical** blocks a task or breaks the law outright. **High** is a WCAG A/AA failure or major friction. **Medium** causes noticeable friction or a best-practice gap. **Low** is polish.

| # | Page / area | Issue | Category | Severity | Recommendation | Status |
|---|---|---|---|---|---|---|
| 1 | Header, < 980 px | Section links are hidden on phones and tablets with no replacement. Visitors can only scroll or tap "Book Joe". | Usability & Navigation | High | Add a Menu button that opens the same section links | **Fixed** |
| 2 | Ticker, hero, podcast | The ticker, route lines, compass and waveform move indefinitely. The ticker pauses on mouse hover only, so keyboard and touch users can't stop it (WCAG 2.2.2, Level A). | Accessibility | High | Add a pause control | **Fixed** |
| 3 | Whole page | No way to skip past the header (WCAG 2.4.1, Level A) | Accessibility | High | Add a skip link | **Fixed** |
| 4 | Stats, ticker, booking | Content sat outside any landmark. The booking section, the main conversion point, was outside `<main>` (axe `region`, 25 nodes). | Accessibility | High | Wrap the hero through booking in one `<main>` | **Fixed** |
| 5 | Philosophy, podcast, footer | Broken heading outline: the Philosophy section had no heading, the page jumped from H1 to H4, the podcast card's H3 came before its section's H2, and the footer used H4s | Accessibility | High | Rebuild the outline: H2 per section, H3 below | **Fixed** |
| 6 | Philosophy and Talks eyebrows, dark mode | Aqua `#01A09F` on surface `#073449` is 4.09:1, below the 4.5:1 AA minimum (1.4.3) | Accessibility | High | Use the lighter link token in dark mode | **Fixed** |
| 7 | Whole page, mobile | Mobile LCP 4.4 s. Photos were served at 2–3× their display size, below-the-fold images loaded eagerly, the 36 px logo was a 32 KiB PNG, and the font stylesheet blocked rendering and loaded unused weights. | Performance | High | srcset images, lazy loading, smaller logo, non-blocking fonts | **Fixed**. Some cost remains; see #17. |
| 8 | Talks explorer | `role="tabpanel"` on `<article>` isn't an allowed role (axe, Lighthouse) | Accessibility | Medium | Use `<div>` | **Fixed** |
| 9 | Header logo | The `aria-label` didn't match the visible wordmark (2.5.3 Label in Name) | Accessibility | Medium | Name the link from its visible text | **Fixed** |
| 10 | Booking form | Error messages weren't linked to their fields, invalid fields weren't flagged, focus stayed on the button after the draft appeared, and "Copied" wasn't announced | Accessibility | Medium | Add `aria-describedby` and `aria-invalid`, move focus to the result, add a status live region | **Fixed** |
| 11 | Social sharing | `og:image` was WebP, which LinkedIn, Facebook and iMessage don't reliably support. No Twitter card. | Content / Conversion | Medium | 1200×630 JPG plus a `summary_large_image` card | **Fixed** |
| 12 | Hero H1 | Two block spans gave the accessible text "JoeBogdan" | Accessibility / Content | Low | Add a space between the spans | **Fixed** |
| 13 | Breadcrumbs | Links were 18 px tall, under the 24 px target size (2.5.8) | Accessibility | Low | Add 3 px of vertical padding | **Fixed** |
| 14 | Philosophy loop | The decorative slogan inside the tab list was read out of context | Accessibility | Low | Mark it `aria-hidden` | **Fixed** |
| 15 | Motto, sign-off | Montserrat 800/900 italic was faked by thickening the 700 italic | Visual hierarchy | Low | Load the real italic weights | **Fixed** |
| 16 | Mobile menu panel (new) | Hero text showed faintly through the 98%-opaque panel. Found during verification. | Visual | Low | Make the panel solid | **Fixed** |
| 17 | Whole page, mid-range phones | About 1 s of style and layout work plus 0.36 s of rendering under 4× CPU throttling. Causes: backdrop blur on the nav and floating cards, stacked gradients, the 3D book, and constant animations. This keeps mobile FCP and LCP at 3.7 s. | Performance | Medium | Remove the blur from the floating cards and the mobile header, and pause animations when off-screen | **Fixed** (decision 2) |
| 18 | Testimonials | Five-star icons suggest ratings the quoted people never gave | Content | Medium | Remove the stars | **Fixed** (decision 3) |
| 19 | Booking | No real submission. The form drafts an email the visitor has to send, so some inquiries will be lost. | Conversion | Medium | Use Netlify Forms (built into the host, no new dependency) with email alerts to C2H | Proposed |
| 20 | Content accuracy | Some details can't be verified from public sources: two ticker entries (Air Force Services Center, JBMDL Building Leaders 2025), the CLO role description, the condensed testimonials, and the Talks focus-area tags | Content | Medium | Keep the ticker entries and the CLO line (both backed by C2H documents); restore testimonials word for word | **Fixed** (decision 4) |
| 21 | Hero, tablet 760–979 px | The single-column layout leaves a large empty area on the right and pushes the photo below the fold | Responsiveness / Layout | Medium | Two-column hero at tablet width with a smaller H1 | **Fixed** (decision 5) |
| 22 | Breadcrumbs, logo, C2H links | They open new tabs without warning. Once hosted on c2htransform.com, internal links should open in the same tab. | Usability | Low | Same-tab for internal C2H links, plus "(opens in new tab)" text for external ones | **Fixed** (decision 6) |
| 23 | CTAs | Two primary button colors: green "Book Joe to speak" (Joe's brand) and blue "Book Joe" (C2H). This was deliberate under the brand split. | Consistency | Low | Standardize: every primary CTA is green | **Fixed** (decision 7) |

Checked and passing: no horizontal overflow at any viewport, no console errors, alt text on all content images, decorative SVGs hidden, visible focus rings in both themes, reduced-motion support, labeled form controls, keyboard tabs with arrow keys, CLS under 0.01, Best Practices 100, SEO 100.

## 2. Change log

Every change is in `index.html` unless noted. Each commit covers one concern.

| Commit | Fix | Files |
|---|---|---|
| `d59be42` | Performance: 480w/900w WebP variants with `srcset`/`sizes` for three photos; hero image preloaded with `fetchpriority=high`; lazy loading below the fold; 145×160 PNG logo replaced with an 80 px WebP (32 KiB → 5 KiB) and a 64 px PNG favicon; Google Fonts loaded without blocking render and trimmed to the weights in use, including real 800/900 italics; 1200×630 JPG `og:image` and Twitter card | `index.html`, `img/*-480.webp`, `img/*-900.webp`, `img/c2h-wolf-80.webp`, `img/favicon-64.png`, `img/og-joe-bogdan.jpg`; removed `img/c2h-wolf.png` and the full-size photo files |
| `df1ed8a` | Accessibility: skip link; single `<main>` from hero through booking; heading outline rebuilt; `<article>` → `<div>` for tab panels; logo name; decorative loop slogan hidden; dark-mode eyebrow contrast; breadcrumb targets 24 px; form error association, focus moved to the draft, live region for copy feedback | `index.html` |
| `de6bb9d` | Navigation and motion: Menu button below 980 px (`aria-expanded`, closes on link, Escape or outside click, returns focus); "Pause motion" toggle that freezes every decorative animation and is hidden when reduced motion is on | `index.html` |
| `b5f67a7` | Mobile menu panel made fully opaque | `index.html` |
| `1795399` | Logo link named from its visible text plus a hidden ", home page" (Label in Name) | `index.html` |
| `03a453f` | H1 reads "Joe Bogdan" instead of "JoeBogdan" | `index.html` |

Brand colors, logo, copy, layout structure and existing behavior are unchanged. No dependencies were added.

**Re-verification on the live site after deploy:**
- axe: 0 violations at all four viewports.
- No horizontal overflow and no console errors.
- Lighthouse: Accessibility 100 on mobile and desktop; Performance 81 mobile and 99 desktop.
- Scripted interaction checks all passed:
  - skip link moves focus to `<main>`
  - Menu opens, focuses its first link, closes on Escape and returns focus, and closes and scrolls to the section when a link is tapped
  - Pause motion freezes the ticker
  - arrow keys move between talks
  - "Request this talk" pre-selects the topic on the form
  - submitting empty fields shows linked errors and focuses the first one
  - a valid submission drafts the inquiry to c2hinfo@c2htransform.com and moves focus to it

## 2b. Decisions (approved by the client, 1 November 2026)

| Commit | Decision | What changed |
|---|---|---|
| `1e0d8c4` | **7. One CTA color: green** | The header "Book Joe", the "Draft my inquiry" submit and "Open in email app" moved from C2H blue to Joe's green. Form focus and selected-chip states follow the teal/green palette. The C2H blue button styles and color tokens were removed from the page. |
| `2d4b394` | **3. No stars; 4. Exact quotes** | Star rows removed. The Aaron Stubbs and AJ Kehl quotes were restored word for word from waypointbetter.com/about. The Gronski excerpt is marked with a leading ellipsis. The ticker entries stay: the JBMDL Building Leaders poster and the C2H travel sheet for AFSVC Child & Youth Programs both name Joe. The CLO line stays. |
| `8d772b8` | **6. Link behavior** | 12 links to c2htransform.com open in the same tab. 9 external links still open a new tab and include "(opens in new tab)" for screen readers. |
| `e120fb8` | **2. Mobile rendering** | The floating hero cards and the header below 980 px lose their blur effect. Animations pause while their section is off-screen. The design looks unchanged. |
| `69691d2` | **5. Tablet hero** | From 760 to 979 px the hero uses two columns with a smaller H1 and compact floating cards, so Joe's portrait stays above the fold. |

After these changes: axe found 0 violations at all four viewports, nothing overflows horizontally, there were no console errors, and every interaction check passed again.

## 3. Open recommendations (need approval)

Items 2–7 below were decided and implemented (see 2b). Only item 1 remains open.

1. **Real inquiry submissions (Conversion, Medium).** The form only drafts an email today. Every planner who doesn't press send is a lost lead. The site is on Netlify, which can capture form submissions and email them to c2hinfo@c2htransform.com without new code libraries. *Expected impact:* fewer lost leads and a record of every inquiry. *Needs:* approval of where submissions go and who gets notified.
2. **Mobile rendering cost (Performance, Medium).** Removing the backdrop blur from the two floating hero cards, simplifying the hero to one gradient plus the route lines, and pausing animations off-screen should bring mobile LCP from 3.7 s toward about 2.5 s, which Lighthouse rates "good". *Trade-off:* the floating cards lose their frosted-glass look.
3. **Testimonial stars (Content, Medium).** The stars imply a rating no one gave. Removing them keeps the quotes honest. *Impact:* credibility with careful readers.
4. **Content verification (Content, Medium).** Have Joe confirm the ticker entries, the CLO description, the condensed testimonials and the focus-area tags.
5. **Tablet hero (Layout, Medium).** A two-column hero from 760 px with a smaller H1 would keep Joe's photo above the fold on iPads. *Needs:* design sign-off, because it changes the layout.
6. **Link targets on c2htransform.com (Usability, Low).** When the page moves under `/speakers`, C2H links should open in the same tab and only external links (BookBaby, Spotify, LinkedIn) should open new tabs.
7. **One primary CTA color (Consistency, Low).** Confirm the rule: Joe-green for Joe actions and C2H-blue for C2H actions. The alternative is all C2H blue.

## 4. Executive summary

The page was in good shape before the audit: no layout breakage, no console errors, and Best Practices and SEO both at 100. Its gaps were accessibility structure, mobile navigation and mobile load time. All Critical and High issues are fixed and verified on the live Netlify deploy. axe now finds no violations at desktop, tablet or mobile in either theme, and Lighthouse accessibility is 100. The three biggest improvements:

1. Phone and tablet visitors can now reach every section through a new Menu.
2. The page meets WCAG 2.2 AA in the areas tested: skip link, landmarks, heading outline, contrast, a pause control for motion, and accessible form errors.
3. Page weight dropped from 522 KiB to 216 KiB on desktop and from 437 KiB to 257 KiB on mobile. Desktop LCP is down to 0.9 s and mobile LCP from 4.4 s to 3.7 s.

The remaining mobile cost comes from decorative effects, and real form capture is the biggest open conversion win. Both need a design or business decision, so they are proposed in section 3 rather than applied.
