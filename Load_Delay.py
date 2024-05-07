from playwright.sync_api import sync_playwright, expect, Playwright
#from conftest import browser_context_args

def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=5000)
    context = browser.new_context()
    page = context.new_page()
    page.goto('http://uitestingplayground.com/')
    page.locator('a[href="/loaddelay"]').click()

    delay_page_button = page.locator('.btn-primary')
    delay_page_button.wait_for(timeout=10000)
    expect(delay_page_button).to_be_visible()

with sync_playwright() as playwright:
    run(playwright)