from playwright.sync_api import sync_playwright, expect, Playwright
#from conftest import browser_context_args

def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=5000)
    context = browser.new_context()
    page = context.new_page()
    page.goto('http://uitestingplayground.com/')
    page.locator('a[href="/textinput"]').click()

    input_box = page.locator('#newButtonName')
    input_box.fill('James')
    button_update = page.locator('#updatingButton')
    button_update.click()
    expect(button_update).to_have_text('James')

with sync_playwright() as playwright:
    run(playwright)