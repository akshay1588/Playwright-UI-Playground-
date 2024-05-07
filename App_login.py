from playwright.sync_api import sync_playwright, expect, Playwright, Page
#from conftest import browser_context_args
import pytest

@pytest.fixture(autouse=True)
def visit_test_page(page:Page):
    page.goto('http://uitestingplayground.com/sampleapp')

def test_successful_login(page:Page):
    user_name = page.locator('input[placeholder="User Name"]')
    user_input = 'John'
    user_name.fill(user_input)
    #UserName= user_name.fill('John')

    passWord = page.locator('input[type="password"]')
    pass_word= passWord.fill('pwd')

    logIn = page.get_by_role('button', name='Log In')
    logIn.click()
    success = page.locator('#loginstatus')
    expect(success).to_have_text(f"Welcome, {user_input}!")

def test_unsuccessful_login(page:Page):
    user_name = page.locator('input[placeholder="User Name"]')
    UserName= user_name.fill('John')

    passWord = page.locator('input[type="password"]')
    pass_word= passWord.fill('123456')

    logIn = page.get_by_role('button', name='Log In')
    logIn.click()
    failure = page.locator('#loginstatus')
    expect(failure).to_have_text('Invalid username/password')


# def run(playwright: Playwright):
#     chromium = playwright.chromium
#     browser = chromium.launch(headless=False, slow_mo=8000)
#     context = browser.new_context()
#     page = context.new_page()
    
#     user_name = page.locator('input[placeholder="User Name"]')
#     UserName= user_name.fill('John')

#     passWord = page.locator('input[type="password"]')
#     pass_word= passWord.fill('pwd')

#     logIn = page.get_by_role('button', name='Log In')
#     logIn.click()
#     if UserName !=" " and pass_word == 'pwd':
        

#     elif UserName == 'John' and pass_word != 'pwd':
#         expect(page.locator('#loginstatus').to_have_text('Invalid username/password'))
    

    
# with sync_playwright() as playwright:
#     run(playwright)