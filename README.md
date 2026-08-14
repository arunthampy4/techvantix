# TechVantix — techvantix.com

Modern, animated, SEO/GEO/AEO-optimized website for **TechVantix**, a digital
marketing, web development and AI automation agency.

## Stack

Pure static HTML + CSS + vanilla JavaScript. No build step, no framework,
no dependencies — upload the files to any hosting and it works.

## Structure

```
index.html                      Homepage (hero, services, why us, AI & search, process, FAQ, contact)
services/
  seo-geo-aeo.html              SEO, GEO & AEO
  web-development.html          Website Design & Development
  ai-chatbot-automation.html    AI Chatbots & Automation
  paid-advertising.html         Meta & Google Ads
  social-media-marketing.html   Social Media Marketing
  lead-generation.html          Lead Generation Campaigns
css/style.css                   Design system (dark theme, teal brand accent)
js/main.js                      Scroll reveals, counters, rotator, accordion, mobile nav, form
assets/                         SVG logo + favicon
404.html · robots.txt · sitemap.xml · llms.txt
```

## SEO / GEO / AEO features built in

- Unique titles, meta descriptions and canonical URLs on every page
- JSON-LD structured data: `Organization`, `WebSite`, `Service`,
  `BreadcrumbList`, `FAQPage` (rich results + AI answer engines)
- Semantic HTML5, single `h1` per page, logical heading hierarchy
- `sitemap.xml`, `robots.txt` (AI crawlers explicitly allowed), `llms.txt`
- Open Graph + Twitter Card tags for social sharing
- FAQ content written in question/answer format for AEO and AI Overviews
- Fast: no frameworks, no heavy libraries, respects `prefers-reduced-motion`

## Before going live — checklist

1. **Stats:** the four counters in the homepage hero are placeholders
   (marked `TODO` in `index.html`). Replace with your real numbers.
2. **Logo:** the header uses a text+SVG recreation of the brand logo. To use
   the official PNG instead, drop it into `assets/` and swap the `.logo`
   markup in the header/footer for an `<img>`.
3. **OG image:** `og:image` currently points at the logo PNG on the live
   WordPress site. For best social sharing, create a 1200×630 cover image,
   upload it as `assets/og-cover.png` and update the `og:image` /
   `twitter:image` tags on all pages.
4. **Contact form:** the form opens the visitor's email app pre-filled
   (mailto to info@techvantix.com) — works with zero backend. For silent
   in-page submission, connect a form service (e.g. Formspree/Web3Forms) by
   changing the handler in `js/main.js`.
5. **Google Search Console:** after launch, verify the domain and submit
   `https://techvantix.com/sitemap.xml`.
6. **Analytics:** add your GA4 / Meta Pixel snippets before `</head>` on
   each page.

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000
```
