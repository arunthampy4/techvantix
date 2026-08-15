# TechVantix — techvantix.com

Modern, animated, SEO/GEO/AEO-optimized website for **TechVantix**, a digital
marketing, web development and AI automation agency.

## Stack

Pure static HTML + CSS + vanilla JavaScript. No build step, no framework,
no dependencies — upload the files to any hosting and it works.

## Clean URLs

Every page is a folder with an `index.html`, so public URLs contain no `.html`:
`techvantix.com/services/web-development/`, `techvantix.com/oman/seo-company-oman/`,
`techvantix.com/blog/`, etc. This works on any static host; the included
`.htaccess` also covers Apache/cPanel hosting (no directory listings, 404 page,
redirect of accidental `/index.html` requests).

## Structure

```
index.html                      Homepage (hero, services, why us, AI & search, process, FAQ, contact)
services/                       /services/ overview page + six service pages
  index.html · seo-geo-aeo/ · web-development/ · ai-chatbot-automation/
  paid-advertising/ · social-media-marketing/ · lead-generation/
oman/                           Oman local-SEO landing pages
  index.html                    Hub: Digital Marketing & Web Development Company in Oman
  website-development-oman/ · digital-marketing-oman/
  social-media-marketing-oman/ · ecommerce-website-development-oman/
  shopify-website-development-oman/ · whatsapp-automation-oman/
  ai-chatbot-development-oman/ · seo-company-oman/
blog/                           Blog index + articles (BlogPosting schema)
  index.html · how-to-rank-on-chatgpt-geo-aeo/
  whatsapp-business-api-guide/ · seo-vs-google-ads/
css/style.css                   Design system (dark theme, teal brand accent)
js/main.js                      Scroll reveals, counters, rotator, accordion, mobile nav, form
assets/                         Favicon (+ upload techvantix-logo.png here)
404.html · robots.txt · sitemap.xml · llms.txt · .htaccess
```

**Oman pages:** interlinked via the footer on every page and the `oman/index.html`
hub, each with `Service` schema (`areaServed: Oman`), bilingual positioning and
keyword-targeted titles — built to rank for "… in Oman" searches without putting
location details on the main pages.

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
2. **Logo:** every page loads the logo from `/assets/techvantix-logo.png`
   (878×210). **Upload the official PNG to that exact path when deploying.**
   Until the file exists, pages automatically fall back to the logo hosted on
   the current WordPress site, so nothing looks broken in the meantime.
3. **OG image:** `og:image` currently points at the logo PNG on the live
   WordPress site. For best social sharing, create a 1200×630 cover image,
   upload it as `assets/og-cover.png` and update the `og:image` /
   `twitter:image` tags on all pages.
4. **Contact form:** the form opens the visitor's email app pre-filled
   (mailto to info@techvantix.com) — works with zero backend. For silent
   in-page submission, connect a form service (e.g. Formspree/Web3Forms) by
   changing the handler in `js/main.js` / `contact/index.html`.
5. **Google reCAPTCHA (contact page):** the `/contact/` form ships with a
   built-in "I'm not a robot" checkbox. To switch it to the official Google
   reCAPTCHA v2 widget: create free keys at
   https://www.google.com/recaptcha/admin for domain `techvantix.com`
   (v2 "I'm not a robot" Checkbox), then paste the **site key** into
   `RECAPTCHA_SITE_KEY = ""` near the bottom of `contact/index.html`.
   The page swaps in the real widget automatically. (Note: full server-side
   token verification requires a form backend — connect one of the form
   services above and it will verify the token for you.)
5. **Google Search Console:** after launch, verify the domain and submit
   `https://techvantix.com/sitemap.xml`.
6. **Analytics:** add your GA4 / Meta Pixel snippets before `</head>` on
   each page.

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000
```
