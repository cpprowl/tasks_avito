from playwright.sync_api import sync_playwright, Playwright
from playwright.sync_api import expect
from datetime import datetime


def run(playwright: Playwright):
    browser = playwright.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    # import time
    # time.sleep(5000000)
    # page.locator("html").press("PageDown")
    element = page.locator("xpath=//html/body/div[1]/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[4]")
    expect(element).to_be_visible()
    element.screenshot(path=f"./screenshot_test_1.png")
    # Test the background page as you would any other page.
    browser.close()

def test_1():
    with sync_playwright() as playwright:
        run(playwright)