from playwright.sync_api import sync_playwright
import time

# Step 1. Create a browser
# Can use chromium/firefox/webkit
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    # time.sleep(5)

    # Step 2. Create a new BrowserContext
    context = browser.new_context()
    page = context.new_page()
    # time.sleep(5)

    # Step 3. Open a page
    page.goto("https://reddit.com")

    page.wait_for_selector("nav")

    for nav in page.query_selector_all("a"):
        print(nav.get_attribute("href"))

    browser.close()
