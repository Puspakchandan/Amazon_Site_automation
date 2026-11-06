import pytest
from playwright.sync_api import expect
import logging
logger = logging.getLogger(__name__) 


def test_open_amazon_site(amazon_pagae):
    """ Successfully login into amazon  site"""
    page = amazon_pagae
    expect(page.get_by_label("Amazon.in").first).to_be_visible()
    expect(page.locator("div.nav-fill").locator("nth=1")).to_be_visible()
    expect(page.locator("span.nav-cart-count")).to_be_visible()

def test_verify_site_already_login_or_not(amazon_pagae):
    """ verify the site is login or not """
    try:
        page = amazon_pagae
        page.locator("span.nav-line-1").locator("nth=2").hover()
        page.wait_for_timeout(1000)
        if page.locator("span.nav-action-inner").is_visible() :
           logger.info ("User not login yet")
        else:
            logger.info("User is already logged in")
    except Exception as e:
        logger.info("Failed to verify the site ")
        page.screenshot(path = "screenshot.jpg")

def test_verify_amazon_pay_balance(amazon_pagae):
    """ verify amazon Pay balanced """
    try:
        page = amazon_pagae
        logger.info("Go to the amazon pay balanced and click ")
        page.get_by_role("link", name = "Amazon Pay").first.click()
        expect(page.get_by_text("Amazon Pay Bala")).to_be_visible()
        logger.info("Verify the balance ")
        text = page.locator("span.currency-green").inner_text()
        if text == "₹0.00":
            logger.info("No Banalced Present")
        else:
            logger.info("Some balanced is present")
    except Exception as e:
        page.screenshot(path="balanced.jpeg")
        raise


@pytest.mark.xfail(reason = "No Element found ")
def test_verify_new_release_option(amazon_pagae):
    """ Click on new Release option """
    page = amazon_pagae
    page.get_by_role("New Releases").click()
    page.pause()
    expect(page.get_by_alt_text("Amazon Hot New Releases", exact= True)).to_be_visible()















    


