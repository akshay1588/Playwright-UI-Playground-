from playwright.sync_api import sync_playwright, expect, Playwright
#from conftest import browser_context_args

def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=5000)
    context = browser.new_context()
    page = context.new_page()
    page.goto('http://uitestingplayground.com/')
    page.locator('a[href="/ajax"]').click()

    ajax_button = page.locator('#ajaxButton')
    ajax_button.click()
    paragraph = page.locator('.bg-success')
    paragraph.wait_for()
    expect(paragraph).to_have_text('Data loaded with AJAX get request.')

with sync_playwright() as playwright:
    run(playwright)