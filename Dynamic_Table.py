from playwright.sync_api import sync_playwright, expect, Playwright
#from conftest import browser_context_args

def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=True, slow_mo=5000)
    context = browser.new_context()
    page = context.new_page()
    page.goto('http://uitestingplayground.com/')
    page.locator('a[href="/dynamictable"]').click()

    finalComparison = page.locator('.bg-warning').inner_text()
    #print(finalComparison)
    percentage =finalComparison.split()
    final_percent = percentage[2]
    # print(percentage[2])

    dynamicTable = page.locator('text="Chrome"')
    cpu = page.get_by_role('row', name='Chrome').inner_text()
    cpu_one = cpu.strip().replace('\t', ',')
    cpu_two = cpu_one.split(',')
    #print(type(cpu_two))
    #print(cpu_one)
    
    for i in range(len(cpu_two)):
        if cpu_two[i]==final_percent:
            print(
                f"Chrome CPU percentage: {cpu_two[i]} and final percentage: {final_percent} match!"
            )    

with sync_playwright() as playwright:
    run(playwright)