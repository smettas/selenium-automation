import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from urllib.parse import urlparse

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Target website
url = "https://www.google.com"  # Replace with your target website
driver.get(url)
time.sleep(3)

# Extract all anchor tags
all_links = driver.find_elements(By.TAG_NAME, "a")

# Get the domain of the target site
base_domain = urlparse(url).netloc

internal_links = []
external_links = []
broken_links = []

# Process each link
for link in all_links:
    href = link.get_attribute("href")
    
    if href:
        parsed_url = urlparse(href)
        link_domain = parsed_url.netloc

        if base_domain in link_domain or link_domain == "":
            internal_links.append(href)  # Internal link
        else:
            external_links.append(href)  # External link
        
        # Check if the link is broken
        try:
            response = requests.head(href, allow_redirects=True, timeout=5)
            if response.status_code >= 400:
                broken_links.append(href)
        except requests.RequestException:
            broken_links.append(href)

# Print categorized links
print("\nInternal Links:", internal_links)
print("\nExternal Links:", external_links)
print("\nBroken Links:", broken_links)

# Close browser
driver.quit()
