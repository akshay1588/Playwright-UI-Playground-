from playwright.sync_api import sync_playwright, expect, Playwright
#from conftest import browser_context_args
import pytest
def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=8000)
    context = browser.new_context()
    page = context.new_page()
    page.goto('http://uitestingplayground.com/')
    page.locator('a[href="/mouseover"]').click()

    count = 0 
    hover = page.locator(('a[title="Click me"]'))
    hover.hover()
    #click = page.locator('text="Click me"').dblclick()
    clickCount = page.locator('text="Click me"')
    clickCount.click(click_count=2)

    
    number_of_clicks = page.locator('#clickCount')
    expect(number_of_clicks).to_have_text('2')

with sync_playwright() as playwright:
    run(playwright)