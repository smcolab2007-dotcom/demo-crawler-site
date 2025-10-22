# demo-crawler-site
A simple educational demo showing how to build and test a basic web page and an ethical web crawler. Designed for teaching and learning purposes. Follow ethical practices: crawl only allowed sites, respect robots.txt, and never collect or share private data.


## 🚀 Project Structure

demo-crawler-site/ ├── index.html        → Public page (OK to crawl) ├── private.html      → Private page (blocked by robots.txt) ├── mixed.html        → Mixed content (public + hidden section) ├── robots.txt        → Controls crawler behavior └── polite_crawler.py                 ← fixed URL version
└── polite_crawler_input_url.py       ← runtime input version (recommended for students)

---




*** Instructions to students:
## ⚖️ Safety & Ethical Notes

This project is **for learning only**.

1. ✅ Crawl only your own test site or sites that **explicitly allow** crawling.  
2. 🚫 Never collect, store, or share private or personal data.  
3. 🔒 Do **not** bypass authentication or access restricted content.  
4. 🤖 Always follow `robots.txt` rules and **respect website permissions**.  

---

⚠️ Safety Note — Ethical Crawling

This crawler is for learning only. Use it only on your own GitHub Pages sites or other pages that explicitly allow crawling in their robots.txt.

❌ Do not use it on:

.Google (google.com)

.Facebook (facebook.com)

.Twitter/X (twitter.com)

.Instagram (instagram.com)

.LinkedIn (linkedin.com)

.Any site that disallows bots or needs login


These platforms block automated access and track bot traffic for security. Using a crawler there violates their Terms of Service and data protection laws.

✅ Safe practice:
Replace the seed URL only with your own public demo repo (for example,
https://your-username.github.io/your-demo-repo/).




## 🧭 How to Use

1. Open the repository in GitHub Pages (enable it under **Settings → Pages**).  
2. Run `polite_crawler.py` in Google Colab or your local Python environment.  
3. Observe how the crawler politely checks `robots.txt` and avoids restricted pages.
4. Optional: Run `polite_crawler_visible.py` in Google Colab or your local Python environment. Observe the Output.

## 🧑‍🎓 For Students — How to Run in Google Colab

# STEP 1 — Get your instructor's GitHub repo
!git clone https://github.com/smcolab2007-dotcom/demo-crawler-site.git
%cd demo-crawler-site

# STEP 2 — Install required packages
!pip install requests beautifulsoup4 --quiet

# STEP 3 — Run the crawler
!python polite_crawler_unfinished.py

---
## SNA PART:
 Run `sna_polite_crawler_unfinished.py`

## Metrics Calculations:
 Run `sna_metrics_polite_crawler_unfinished.py`

## 📘 License

This demo is released for **educational use only** — not for production or commercial crawling.
