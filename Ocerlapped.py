from playwright.sync_api import sync_playwright, expect, Playwright
#from conftest import browser_context_args
import pytest
def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=8000)
    context = browser.new_context()
    page = context.new_page()
    page.goto('http://uitestingplayground.com/')
    page.locator('a[href="/overlapped"]').click()

    id_btn = page.get_by_placeholder("Id")
    id_btn.fill('457')

    name_btn = page.get_by_placeholder("Name")

    # name_btn.scroll_into_view_if_needed() --> This will not work since part of the input field is still visibile
    # We will have to use mouse functionality to scroll the element into view 

    div = name_btn.locator('..')
    div.hover()

    page.mouse.wheel(0,200)

    # name_fill = page.locator('#name')
    data = 'Tom'
    name_btn.fill(data)
    expect(name_btn).to_have_value(data)

with sync_playwright() as playwright:
    run(playwright)