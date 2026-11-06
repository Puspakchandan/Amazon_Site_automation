import pytest
from playwright.sync_api import sync_playwright, expect
import logging 
logger = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def amazon_pagae():
    """ Login to the amazon page """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        try:
            logger.info("Trying to login into amazon Site ")
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://www.amazon.in/")
            logger.info("Amazon page logged successfully")
            yield page 

        except Exception as e:
            page.screenshot(Path="screen.jpeg")
        finally:
            browser.close()
        

  







