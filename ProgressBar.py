from playwright.sync_api import sync_playwright, expect, Playwright
#from conftest import browser_context_args

def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=8000)
    context = browser.new_context()
    page = context.new_page()
    page.goto('http://uitestingplayground.com/')
    page.locator('a[href="/progressbar"]').click()

    startbtn = page.locator('#startButton')
    stopbtn = page.locator('#stopButton')
    startbtn.click()
    #barProgress = page.locator('.progress-bar')
    status = page.locator('#progressBar')
    #print(status)
    while True:
        valueNow= int(status.get_attribute('aria-valuenow'))
        #print(valueNow)
        if valueNow>=75:
            break
        else:
            print(f'Current Percentage: {valueNow}%') 

    stopbtn.click()
    assert valueNow>=75
    #expect(valueNow).to_have_value('75')

with sync_playwright() as playwright:
    run(playwright)