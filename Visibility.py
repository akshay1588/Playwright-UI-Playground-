from playwright.sync_api import sync_playwright, expect, Playwright
#from conftest import browser_context_args
import pytest
def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=8000)
    context = browser.new_context()
    page = context.new_page()
    page.goto('http://uitestingplayground.com/')
    page.locator('a[href="/visibility"]').click()

    hide_btn = page.get_by_role('button', name='Hide')
    remove_btn = page.locator('#removedButton')
    ZeroWidth = page.get_by_role('button', name='Zero Width')
    overlapBtn = page.locator('.btn-success')
    Opacitybtn = page.locator('#transparentButton')
    VisibilityHidden_btn = page.get_by_text('Visibility Hidden')
    NoneDisplaybtn = page.locator('#notdisplayedButton')
    OffscreenBtn = page.get_by_role('button', name='Offscreen')

    hide_btn.click()
    expect(remove_btn).to_be_hidden()
    expect(ZeroWidth).not_to_be_visible()
    expect(ZeroWidth).to_have_css('width','0px')
    with pytest.raises(TimeoutError):
        overlapBtn.click(timeout=2000)

    expect(Opacitybtn).to_have_css('opacity', '0')
    expect(VisibilityHidden_btn).to_be_hidden()
    expect(NoneDisplaybtn).to_be_hidden()
    expect(OffscreenBtn).not_to_be_in_viewport()
    
with sync_playwright() as playwright:
    run(playwright)