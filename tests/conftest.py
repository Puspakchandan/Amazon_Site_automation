import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(scope="session")
def amazon_pagae():
    """ Login to the amazon page """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        try:
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://www.amazon.in/")
            yield page 
        finally:
            browser.close()
        

  







