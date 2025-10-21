## 🧑‍🎓 For Students — How to Run in Google Colab

# STEP 1 — Get your instructor's GitHub repo
!git clone https://github.com/smcolab2007-dotcom/demo-crawler-site.git
%cd demo-crawler-site

# STEP 2 — Install required packages
!pip install requests beautifulsoup4 --quiet

# STEP 3 — Run the crawler
!python polite_crawler.py
