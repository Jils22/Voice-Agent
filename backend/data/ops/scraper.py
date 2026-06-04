import os
import re
import ssl
import requests
import time
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# SSL Bypass for Windows environment with self-signed certs
ssl._create_default_https_context = ssl._create_unverified_context
os.environ["CURL_CA_BUNDLE"] = ""

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
DOCS_DIR = os.path.join(os.path.dirname(__file__), "..", "store", "docs")
os.makedirs(DOCS_DIR, exist_ok=True)

SITEMAP_URL = "https://taxone.vyapar.com/sitemap.xml"

def get_article_urls():
    print("Fetching sitemap...")
    try:
        # Using verify=False to bypass SSL errors
        response = requests.get(SITEMAP_URL, headers=HEADERS, verify=False, timeout=30)
        response.raise_for_status()
        # Extract URLs matching help articles across different modules
        urls = re.findall(r'<loc>(https://taxone\.vyapar\.com/help/[^<]+)</loc>', response.text)
        print(f"Found {len(urls)} help articles in sitemap.")
        return sorted(list(set(urls)))
    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        # Fallback to a few known ones if sitemap fails
        return []

def scrape_article(url):
    slug = url.split("/")[-1].split("#")[0]
    filename = f"scrape_{slug}.md"
    filepath = os.path.join(DOCS_DIR, filename)
    
    print(f"Scraping {slug}...")
    try:
        response = requests.get(url, headers=HEADERS, verify=False, timeout=20)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")
        
        # Selectors for TaxOne Help Center
        title_tag = soup.find("h1")
        title_text = title_tag.get_text(strip=True) if title_tag else slug.replace("-", " ").title()
        
        # Target the main content area with specific selectors for TaxOne Help Center (with s_ prefix)
        content_div = soup.find("div", class_="s_article-detail") or \
                      soup.find("div", class_="s_article-content") or \
                      soup.find("div", class_="article-content") or \
                      soup.find("div", class_="article-body") or \
                      soup.find("article") or \
                      soup.find("main")
        
        if not content_div:
            # Fallback to finding the largest text container
            containers = soup.find_all("div")
            if containers:
                content_div = max(containers, key=lambda x: len(x.get_text()))
            else:
                content_div = soup.find("body")

        # Basic cleaning: remove header, footer, nav if they leaked in
        for junk in content_div.find_all(["nav", "header", "footer", "script", "style"]):
            junk.decompose()
            
        # Convert to markdown
        content_md = md(str(content_div), heading_style="ATX")
        
        # Clean up excessive newlines
        content_md = re.sub(r'\n{3,}', '\n\n', content_md)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {title_text}\n\n")
            f.write(f"Source: {url}\n\n")
            f.write(content_md)
        return True
            
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return False

def main():
    urls = get_article_urls()
    if not urls:
        print("No URLs found to scrape.")
        return

    success_count = 0
    for i, url in enumerate(urls):
        if scrape_article(url):
            success_count += 1
        
        # Progress indicator every 10 articles
        if (i + 1) % 10 == 0:
            print(f"Progress: {i + 1}/{len(urls)} processed...")
            
        # Small delay to be polite to the server
        time.sleep(0.2)

    print(f"\nScraping complete. Successfully processed {success_count} articles.")
    print(f"All files saved to: {DOCS_DIR}")

if __name__ == "__main__":
    main()
