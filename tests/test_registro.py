import time
from playwright.sync_api import sync_playwright


def test_registro():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://www.automationexercise.com/")

        page.click('a[href="/login"]')

        page.fill('input[data-qa="signup-name"]', 'Oscar Isaac')
        page.fill('input[data-qa="signup-email"]', 'a@test3.com')

        page.click('button[data-qa="signup-button"]')
        time.sleep(3)

        page.check('#id_gender1')

        page.fill('#password', 'Qwerty123')

        page.select_option('#days', '10')
        page.select_option('#months', '9')
        page.select_option('#years', '2001')

        page.check('#newsletter')

        page.screenshot(path="screenshots/testregistro.png")
        time.sleep(3)

        browser.close()