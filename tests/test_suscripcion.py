import time
from playwright.sync_api import sync_playwright


def test_suscripcion():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://www.automationexercise.com/")

        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)

        page.fill('#susbscribe_email', 'a@test3.com')
        time.sleep(3)

        page.click('#subscribe')

        page.screenshot(path="screenshots/testsuscripcion.png")

        browser.close()