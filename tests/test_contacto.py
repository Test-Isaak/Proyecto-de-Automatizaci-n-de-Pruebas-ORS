import time
from playwright.sync_api import sync_playwright


def test_contacto():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://www.automationexercise.com/")

        page.click('a[href="/contact_us"]')

        page.fill('input[data-qa="name"]', 'Oscar Isaac')
        page.fill('input[data-qa="email"]', 'a@test3.com')
        page.fill('input[data-qa="subject"]', 'Consulta de Prueba')
        page.fill('#message', 'Esto es un mensaje de pruebas ingresando texto')
        time.sleep(3)

        page.on("dialog", lambda dialog: dialog.accept())
        time.sleep(3)

        page.click('input[data-qa="submit-button"]')

        page.screenshot(path="screenshots/testcontacto.png")

        browser.close()