# Deep Audit #2: Joe Bogdan Speaker Page

- **Site:** https://joe-bogdan-speaker.netlify.app (repo `kcastille3324/Joe-Speaker-Page-`, commit `ccd2702`)
- **Date:** 11 November 2026
- **Scope:** everything in Audit #1, plus:
  - SEO and structured data
  - AI-search visibility
  - security headers and caching
  - HTML validity
  - link health
  - keyboard order
  - Windows High Contrast
  - 400% zoom reflow
  - text-spacing override
  - no-JavaScript behavior
  - print
  - copy and brand voice
  - conversion for event planners
  - measurement and operations

## How it was tested

| Check | Tool | Result |
|---|---|---|
| Lighthouse 12.2 (mobile) | Chromium, simulated slow 4G | Performance 98, Accessibility 100, Best Practices 100, SEO 100. LCP 2.0 s, CLS 0.002 |
| Lighthouse 12.2 (desktop) | Chromium | 99 / 100 / 100 / 100. LCP 0.8 s |
| axe-core 4.10, WCAG 2.2 AA | 4 viewports, light and dark | 0 violations |
| W3C Nu HTML + CSS validator | `vnu-jar` | **2 real issues** (below). The CSS "errors" are the validator not understanding `env()`/`max()`, so they are false positives. |
| Link check | curl over all 21 hrefs | All resolve. BookBaby returns 403 and LinkedIn 999 because they block bots, not because the links are broken. |
| Keyboard walk | 50 Tab stops | Logical order, skip link first, focus never lands on hidden elements |
| 400% zoom (320×256 CSS px) | Playwright | **16 px horizontal overflow** in the talk explorer |
| WCAG 1.4.12 text spacing | Injected spacing CSS | No visible clipping |
| Windows High Contrast (`forced-colors`) | Playwright emulation | **Selected states disappear** |
| JavaScript disabled | Playwright | **4 of 5 talks unreachable; Menu button inert; form inert** |
| Print | `emulateMedia('print')` | No print styles |
| Response headers | curl | HSTS only. **No CSP, nosniff, referrer or permissions policy. Images not cached.** |
| Crawl files | curl | **No `robots.txt` or `sitemap.xml`; no canonical; no JSON-LD** |

## Scorecard

| Area | Score | Verdict |
|---|---|---|
| Accessibility | 92 | Strong. Three edge cases remain (zoom, high contrast, no-JS). |
| Performance | 97 | Excellent. Only repeat-visit caching is left. |
| Visual design and brand | 90 | Distinctive and consistent. |
| **SEO and AI discoverability** | **68** | Needs work. Search engines can read the page but get almost no structured information about Joe, the book or the podcast. |
| Security and hosting hygiene | 70 | Missing standard security headers. |
| **Conversion (event-planner readiness)** | **60** | **Biggest gap.** Planners can't see Joe speak and can't find the logistics they need, and the form doesn't actually submit. |
| **Measurement and operations** | **20** | No analytics, no uptime monitoring, no record of inquiries. |
| Code maintainability | 75 | One 1,000-line file with 25 inline styles, and a manual artifact-sync step. |

## Findings

Severity: **High** means it fails WCAG AA or loses leads. **Medium** is a meaningful gap. **Low** is polish.

**Needs Joe** means the item needs content or assets from Joe. **Needs decision** means the item needs a decision or an account from you.

### A. Accessibility

| # | Issue | Evidence | Severity | Fix |
|---|---|---|---|---|
| A1 | The talk explorer overflows 16 px at 320 px width, which is the width of 400% zoom (WCAG 1.4.10 Reflow) | `.tablist` and `.panel` right edge at 336 px in a 320 px viewport | High | `minmax(0,1fr)` columns, plus letting tab text wrap |
| A2 | In Windows High Contrast, the selected talk tab, loop node and format chip look the same as unselected ones | Both render with a black border on white | Medium | `@media (forced-colors: active)` rules using `Highlight` and a thicker border |
| A3 | With JavaScript off, 4 talks stay hidden, the Menu button does nothing and the form does nothing | No-JS run | Low | Show all panels and hide the Menu button until JS loads; a real form submit fixes the form (C1) |
| A4 | `<figcaption>` sits inside a `<div>` in the Gronski quote | Nu validator error | Low | Move it to be a direct child of `<figure>` |
| A5 | `aria-label` on a plain `<div>` (the Three Cs) is ignored by screen readers | Nu validator warning | Low | Add `role="group"` or make it a list |
| A6 | The form-field focus ring is a faint glow plus a 1.5 px border | Visual check | Low | Add a 2 px solid focus outline |
| A7 | Footer links are 25 px tall, the breadcrumbs 28 px and the copy buttons 40 px: they pass the 24 px AA minimum but are under the 44 px touch guideline | Measured | Low | Add vertical padding |

### B. SEO and AI-search visibility

| # | Issue | Evidence | Severity | Fix |
|---|---|---|---|---|
| B1 | No structured data, so Google and AI assistants get no machine-readable facts about Joe, the book, the podcast or C2H | 0 JSON-LD blocks | High | JSON-LD for `Person` (jobTitle, worksFor C2H, sameAs LinkedIn, Facebook and waypointbetter.com), `Book` (ISBN 9798317821920, 344 pp., BookBaby, published 2026-02-09), `PodcastSeries`, `Organization` (C2H) and `BreadcrumbList` |
| B2 | No canonical URL. Once the page also lives on c2htransform.com there will be two copies competing in search. | No `rel="canonical"` | High | Canonical points to the final C2H URL. The Netlify copy points there too, or redirects. |
| B3 | Title is 23 characters with no search terms ("Joe Bogdan, C2H Speaker") | `<title>` | Medium | e.g. "Joe Bogdan, Leadership Keynote Speaker & Author \| C2H" (about 55 characters) |
| B4 | Meta description is 184 characters, so Google truncates it | Measured | Medium | Trim to about 155 characters, leading with keynote topics and booking |
| B5 | No `robots.txt` and no `sitemap.xml` | Both 404 | Medium | Add both |
| B6 | Missing `og:url`, `og:site_name`, `twitter:title` and `twitter:description` | Head scan | Low | Add them |
| B7 | Lives on a `netlify.app` subdomain with no link authority | Domain | Medium (needs decision) | Move to `c2htransform.com/speakers/joe-bogdan`, or a custom domain such as `joebogdan.com` |
| B8 | Headings don't use the phrases planners search for ("leadership keynote speaker", "military leadership speaker", "HR keynote") | H2 scan | Low | Fold one phrase into the Talks H2 and the About H2 without changing meaning |
| B9 | No FAQ content for AI assistants and Google to quote | Content | Medium (needs Joe) | Planner FAQ (see C4) with `FAQPage` schema |

### C. Conversion: what an event planner needs

| # | Issue | Severity | Fix |
|---|---|---|---|
| C1 | **The form doesn't submit.** It drafts an email the planner has to send, so leads leak. | High (needs decision) | Netlify Forms (built into the host, works without JS) sends to c2hinfo@, plus an auto-reply to the planner. Resend is connected here if branded emails are wanted. |
| C2 | **No video of Joe speaking.** A sizzle reel or keynote clip is the first thing bookers look for. | High (needs Joe) | 60–120 s highlight reel near the top of Talks |
| C3 | No photos of Joe on stage. All three photos are studio headshots. | Medium (needs Joe) | 2–4 event photos, e.g. the JBER Chiefs Induction and the AFSVC Global Leadership Conference |
| C4 | No planner logistics: talk lengths, virtual vs in-person, travel base, AV needs, customization, availability, fee range | Medium (needs Joe) | "Planning details" block plus a 5–6 question FAQ |
| C5 | Talks list topics but not outcomes ("attendees leave able to…") | Medium (needs Joe) | Three outcomes per talk |
| C6 | The testimonials are about mentoring and coaching. None is from an event organizer about a talk. | Medium (needs Joe) | 2–3 organizer quotes, e.g. AFSVC or JBER |
| C7 | No downloadable one-sheet, press kit or headshots for event marketing | Medium | One-page PDF one-sheet, a headshot pack and short and long bios. The page needs the `downloads` capability, or host the PDF on Netlify. |
| C8 | The book links go to BookBaby only. Many readers expect Amazon. | Low (needs Joe) | Add an Amazon link if the book is listed there |

### D. Measurement and operations

| # | Issue | Severity | Fix |
|---|---|---|---|
| D1 | No analytics, so there's no way to know visits, sources or inquiry clicks | High (needs decision) | Privacy-friendly analytics (Netlify Analytics, or Plausible / GA4) plus events for "Request this talk", "Draft inquiry", "Get the book" and Spotify |
| D2 | No uptime or error monitoring | Low | Sentry uptime monitor (Sentry is connected in this session) |
| D3 | No privacy notice, which will be needed once analytics or forms collect data | Medium (with D1 and C1) | Link to C2H's /privacy |

### E. Security, hosting and code

| # | Issue | Severity | Fix |
|---|---|---|---|
| E1 | Only HSTS is sent. There is no CSP, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy` or `frame-ancestors`. | Medium | Netlify `_headers` file |
| E2 | Images are served with `max-age=0`, so repeat visitors re-download everything | Medium | `Cache-Control: public, max-age=2592000` for `/img/*` |
| E3 | 25 inline `style=""` attributes, and the artifact copy is kept in sync by hand | Low | Move them to classes; add `scripts/build-artifact.py` |
| E4 | No print stylesheet (planners print and forward speaker pages) | Low | `@media print`: hide nav, ticker, animations and the form, and show URLs |

### F. Copy and brand voice

Measured against the C2H voice rules: trusted advisor, direct; no motivational-speaker tone, no exclamation marks, no lines that could sit on an airport poster.

- **Passes:** the body copy, bio, talks and booking steps are plain and concrete.
- **Tension, kept as Joe's own messaging:**
  - "Leadership is a responsibility. Excellence is a commitment. Growth is a continuous pursuit."
  - "Keep growing. Keep inspiring."
  - "Bring better to your next event."

  These lean toward slogan. They're Joe's words, so I didn't change them. Flagged for Joe and C2H to decide.
- **Lines I wrote that Joe should approve:**
  - the Serve / Recognize / Improve descriptions
  - the Three Cs one-liners
  - the CLO sentence
  - the talk focus tags
  - the book summary

## Skills and tools needed, mapped to the work

Everything listed here is available in this session unless marked otherwise.

| Workstream | Skill / tool | What it does here |
|---|---|---|
| SEO foundation | `searchfit-seo:seo-audit` (used for this report) | Checklist for B1–B9 |
| | `searchfit-seo:schema-markup` / `generate-schema` | Writes and validates Person, Book, PodcastSeries, Organization, Breadcrumb and FAQ JSON-LD (B1, B9) |
| | `searchfit-seo:technical-seo` | robots, sitemap, canonical and migration plan to c2htransform.com (B2, B5, B7) |
| | `searchfit-seo:on-page-seo` | Title, description and keyword-aware headings (B3, B4, B8) |
| | `searchfit-seo:ai-visibility`, `small-business:seo-ai-visibility` | How Joe appears in ChatGPT, Claude and Perplexity answers, and entity consistency |
| Accessibility and UX | `design:accessibility-review` | Formal WCAG 2.2 pass on A1–A7 |
| | `design:design-critique`, `anthropic-skills:landing-page-visual-design-auditor` | Speaker-page layout and hierarchy once video and stage photos arrive |
| Copy and brand | `brand-voice:brand-voice-enforcement` | Checks copy against the C2H voice (F) |
| | `anti-ai-writing:anti-ai-writing` | Removes generic-sounding phrasing from my drafted lines |
| | `design:ux-copy`, `anthropic-skills:landing-page-copy` | Talk outcomes, FAQ, planner details (C4, C5) |
| | `anthropic-skills:professional-bio` | Short, medium and long bios for the press kit (C7) |
| Conversion assets | `anthropic-skills:speaking-one-sheet` | The downloadable one-sheet (C7) |
| | Canva / Adobe connectors | Design the one-sheet PDF and social cards. Canva needs authorization. |
| | `anthropic-skills:website-marketing-pitch-optimizer` | Planner-focused conversion pass |
| Lead capture | Netlify connector + `netlify-forms` coding context | Real form submissions (C1) |
| | Resend connector | Branded confirmation email to the planner and an alert to C2H |
| | `small-business:speed-to-lead`, `lead-triage` | Follow-up playbook for inquiries |
| Measurement | `product-tracking-skills` (model → plan → implement) | Analytics events for D1 |
| | `growthbook:experiments` | A/B test the hero CTA wording later |
| | Sentry connector | Uptime monitor (D2) |
| Engineering | `security-review`, `engineering:code-review`, `simplify` | `_headers`/CSP (E1), inline-style cleanup (E3) |
| | `engineering:deploy-checklist` | Pre-launch checklist for the move to c2htransform.com |
| Video (C2) | None can create footage | Needs real keynote recordings. Canva's video tools can cut a reel from clips Joe supplies. |

Optional: SearchFit.ai (from the SEO skill's publisher) offers ongoing SEO and AI-visibility monitoring. It isn't required for any fix above.

## Recommended roadmap

**Phase 1: technical. I can do these now, with no content needed from Joe.** About 1 session.
- A1 Reflow fix · A2 High Contrast · A3 no-JS fallbacks · A4–A7 markup and targets
- B1 JSON-LD · B2 canonical · B3/B4 title and description · B5 robots and sitemap · B6 social tags
- E1 security headers · E2 image caching · E4 print styles

Expected results: SEO health from 68 to about 90, rich-result eligibility (Person, Book, Breadcrumb), repeat visits served from cache, and the reflow, high-contrast and no-JS gaps closed.

**Phase 2: lead capture and measurement. Needs your decision.**
- C1 Netlify Forms plus auto-reply · D1 analytics plus events · D3 privacy link · D2 uptime monitor

**Phase 3: proof and planner content. Needs Joe.**
- C2 sizzle reel · C3 stage photos · C6 organizer testimonials · C5 talk outcomes · C4 logistics and FAQ (then B9 FAQ schema) · C7 one-sheet and press kit · C8 Amazon link · F copy sign-off

**Phase 4: move to the C2H domain.**
- B7 publish under c2htransform.com/speakers/joe-bogdan, with the canonical and a redirect from Netlify
