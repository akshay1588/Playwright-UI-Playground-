from playwright.sync_api import sync_playwright, expect, Playwright
#from conftest import browser_context_args

def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=5000)
    context = browser.new_context()
    page = context.new_page()
    page.goto('http://uitestingplayground.com/')
    page.locator('a[href="/verifytext"]').click()

    TextVerify = page.locator('.bg-primary').get_by_text('Welcome')
    expect(TextVerify).to_contain_text('Welcome UserName!')

with sync_playwright() as playwright:
    run(playwright)