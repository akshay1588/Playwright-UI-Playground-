from playwright.sync_api import sync_playwright, expect, Playwright
#from conftest import browser_context_args

def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=5000)
    context = browser.new_context()
    page = context.new_page()
    page.goto('http://uitestingplayground.com/')
    page.locator('a[href="/scrollbars"]').click()

    box = page.locator('#hidingButton')
    box.scroll_into_view_if_needed()
    expect(box).to_have_text('Hiding Button')

with sync_playwright() as playwright:
    run(playwright)