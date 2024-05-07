from playwright.sync_api import sync_playwright, expect, Playwright
#from conftest import browser_context_args

def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=5000)
    context = browser.new_context()
    page = context.new_page()
    page.goto('http://uitestingplayground.com/')
    page.locator('a[href="/click"]').click()

    click_blue_button = page.locator('#badButton')
    click_blue_button.click()
       
    expect(click_blue_button).to_have_class('btn btn-success')

with sync_playwright() as playwright:
    run(playwright)