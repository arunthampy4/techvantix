#!/usr/bin/env python3
"""Post-generation SEO pass: SERP-safe titles/descriptions, drop meta keywords.

Run AFTER the page generators. Titles are kept under ~60 characters and
descriptions under ~158 so Google displays them in full rather than
truncating, and `meta keywords` is removed everywhere (Google ignores it and
a stuffed list is a spam signal to other parsers).
"""
import glob, os, re

ROOT = "/home/user/techvantix"

# key = path relative to ROOT (without /index.html)  ->  (title, description)
META = {
    "": ("Digital Marketing & AI Automation Agency | TechVantix",
         "TechVantix builds SEO, AI search visibility, high-performance websites, chatbots and paid campaigns that turn clicks into customers."),

    # ---------------- Core services ----------------
    "services": ("Our Services — Marketing, Web & AI | TechVantix",
                 "SEO, GEO and AEO, websites and e-commerce, AI chatbots, Google and Meta Ads, social media and lead generation — each with a dedicated page."),
    "services/seo": ("SEO Services That Grow Rankings | TechVantix",
                     "Technical SEO, keyword and intent research, content strategy, local SEO and authority building that grow organic rankings, traffic and leads."),
    "services/geo": ("GEO — Get Recommended by AI Search | TechVantix",
                     "Generative Engine Optimization: entity building, structured data and citable content that make ChatGPT, Gemini and Perplexity recommend your brand."),
    "services/aeo": ("AEO — Win Snippets & AI Answers | TechVantix",
                     "Answer Engine Optimization: FAQ schema, snippet-ready formatting and question-led content that win featured snippets, voice results and AI Overviews."),
    "services/seo-geo-aeo": ("SEO, GEO & AEO Combined Program | TechVantix",
                             "How the three search disciplines work as one program — rankings on Google plus visibility inside AI-generated answers and featured snippets."),
    "services/web-development": ("Website Design & Development | TechVantix",
                                 "Fast, mobile-first, conversion-focused websites and landing pages — built to load instantly, rank well and turn visitors into enquiries."),
    "services/ecommerce-development": ("E-commerce & Shopify Development | TechVantix",
                                       "Shopify, WooCommerce and custom online stores with optimized checkout, product SEO, payment and delivery integration, and marketing built in."),
    "services/ai-chatbot-automation": ("AI Chatbots & Business Automation | TechVantix",
                                       "Custom AI assistants that answer customers, qualify leads and book appointments 24/7, plus workflow automation that saves hours every day."),
    "services/whatsapp-automation": ("WhatsApp Automation & Business API | TechVantix",
                                     "WhatsApp Business API setup, AI chatbots, broadcast campaigns, shared team inbox and order notifications — configured compliantly."),
    "services/google-ads": ("Google Ads Management & PPC | TechVantix",
                            "Search, Shopping, YouTube and remarketing campaigns with verified conversion tracking, optimized toward cost per acquisition and real return."),
    "services/meta-ads": ("Meta Ads — Facebook & Instagram | TechVantix",
                          "Facebook and Instagram campaigns built on strong creative, precise audiences and Conversions API tracking for measurable return on ad spend."),
    "services/paid-advertising": ("Paid Advertising Management | TechVantix",
                                  "Performance campaigns across Google and Meta — tracked end to end, tested relentlessly and optimized for profit rather than clicks."),
    "services/social-media-marketing": ("Social Media Marketing Services | TechVantix",
                                        "Strategy, scroll-stopping content, short-form video and community management that turn followers into fans — and fans into customers."),
    "services/lead-generation": ("Lead Generation Campaigns | TechVantix",
                                 "Full-funnel campaigns, high-converting landing pages, lead magnets and instant AI follow-up that fill your pipeline with qualified prospects."),

    # ---------------- Oman / Muscat ----------------
    "oman": ("Digital Agency in Oman & Muscat | TechVantix",
             "TechVantix serves businesses across Oman — websites, SEO, e-commerce, Shopify, WhatsApp automation, AI chatbots, social media and paid ads."),
    "oman/website-development-oman": ("Website Development Company in Oman | TechVantix",
                                      "Website development in Oman: fast, mobile-first, bilingual English and Arabic websites for businesses in Muscat and across the Sultanate."),
    "oman/digital-marketing-oman": ("Digital Marketing Services in Oman | TechVantix",
                                    "SEO, Google Ads, Meta Ads, social media and content marketing for Omani businesses — one team, measurable growth, reporting in OMR."),
    "oman/social-media-marketing-oman": ("Social Media Marketing Company in Oman | TechVantix",
                                         "Instagram, TikTok and LinkedIn management for Omani brands — bilingual content, Reels production and community management that converts."),
    "oman/ecommerce-website-development-oman": ("E-commerce Development in Oman | TechVantix",
                                                "Online stores for Omani retail: local payment gateways, OMR pricing, delivery integration, Arabic storefronts and conversion-focused design."),
    "oman/shopify-website-development-oman": ("Shopify Development Company in Oman | TechVantix",
                                              "Shopify store setup, theme customisation, payment integration and migration for brands in Muscat and across Oman that want to sell online fast."),
    "oman/whatsapp-automation-oman": ("WhatsApp Automation & API in Oman | TechVantix",
                                      "WhatsApp Business API setup, AI chatbots, broadcast campaigns and automated customer service on the app Oman uses most."),
    "oman/ai-chatbot-development-oman": ("AI Chatbot Development in Oman | TechVantix",
                                         "Custom AI chatbots for Omani businesses that answer customers, qualify leads and book appointments 24/7 — in Arabic and English."),
    "oman/seo-company-oman": ("SEO Company in Oman & Muscat | TechVantix",
                              "Bilingual SEO for Oman: technical fixes, Arabic and English content, Google Maps visibility and AI search optimization that compounds."),
    "oman/geo-aeo-oman": ("GEO & AEO Services in Oman | TechVantix",
                          "Get cited by ChatGPT, Gemini and Google AI Overviews when customers in Muscat and Oman ask AI which company to hire."),
    "oman/google-ads-oman": ("Google Ads Company in Oman | TechVantix",
                             "Google Ads management for Omani businesses — Search, Shopping and YouTube campaigns with call and WhatsApp tracking, reported in OMR."),
    "oman/meta-ads-oman": ("Facebook & Instagram Ads in Oman | TechVantix",
                           "Meta Ads for Omani businesses: bilingual creative, click-to-WhatsApp campaigns and Conversions API tracking that turn scrolling into enquiries."),
    "oman/lead-generation-oman": ("Lead Generation Company in Oman | TechVantix",
                                  "Targeted campaigns, bilingual landing pages, instant WhatsApp follow-up and CRM tracking that fill your pipeline with qualified Omani prospects."),

    # ---------------- Blog & contact ----------------
    "blog": ("Blog — SEO, AI Search & Growth | TechVantix",
             "Practical, no-fluff articles on SEO, AI search, WhatsApp automation and marketing strategy from the team building it every day."),
    "blog/how-to-rank-on-chatgpt-geo-aeo": ("How to Get Recommended by ChatGPT | TechVantix",
                                            "A practical GEO and AEO guide: how AI assistants decide which businesses to name, and the steps to become one of them."),
    "blog/whatsapp-business-api-guide": ("WhatsApp Business API Explained | TechVantix",
                                         "What the WhatsApp Business API is, how it differs from the free app, what it costs, and how businesses use it to automate sales and support."),
    "blog/seo-vs-google-ads": ("SEO vs Google Ads: Where to Start | TechVantix",
                               "Which deserves your budget first? A practical comparison of cost, speed and durability — plus the hybrid most growing businesses should run."),
    "contact": ("Contact Us — Free Consultation | TechVantix",
                "Tell us about your project and get a clear proposal. We reply within one business day — no pressure, no spam, no jargon."),
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def apply():
    changed = long_t = long_d = kw_removed = 0
    for path in glob.glob(os.path.join(ROOT, "**", "index.html"), recursive=True):
        rel = os.path.relpath(os.path.dirname(path), ROOT).replace("\\", "/")
        key = "" if rel == "." else rel
        s = open(path, encoding="utf-8").read()
        orig = s

        # 1. Strip meta keywords everywhere (no ranking value; stuffed lists read as spam)
        s2 = re.sub(r'\s*<meta name="keywords" content="[^"]*">', "", s)
        if s2 != s:
            kw_removed += 1
        s = s2

        if key in META:
            title, desc = META[key]
            s = re.sub(r"<title>.*?</title>", f"<title>{esc(title)}</title>", s, count=1, flags=re.S)
            s = re.sub(r'<meta name="description" content="[^"]*">',
                       f'<meta name="description" content="{esc(desc)}">', s, count=1)
            # keep social titles in sync with the SERP title
            s = re.sub(r'<meta property="og:title" content="[^"]*">',
                       f'<meta property="og:title" content="{esc(title)}">', s, count=1)
            s = re.sub(r'<meta name="twitter:title" content="[^"]*">',
                       f'<meta name="twitter:title" content="{esc(title)}">', s, count=1)
            s = re.sub(r'<meta property="og:description" content="[^"]*">',
                       f'<meta property="og:description" content="{esc(desc)}">', s, count=1)
            s = re.sub(r'<meta name="twitter:description" content="[^"]*">',
                       f'<meta name="twitter:description" content="{esc(desc)}">', s, count=1)
            if len(title) > 60:
                long_t += 1
                print(f"  ! title {len(title)} chars: {key}")
            if len(desc) > 158:
                long_d += 1
                print(f"  ! desc {len(desc)} chars: {key}")
        elif key not in ("",):
            print(f"  ? no META entry for: {key}")

        if s != orig:
            open(path, "w", encoding="utf-8").write(s)
            changed += 1

    print(f"\nUpdated {changed} pages | keywords removed from {kw_removed} | "
          f"over-long titles {long_t} | over-long descriptions {long_d}")


if __name__ == "__main__":
    apply()
