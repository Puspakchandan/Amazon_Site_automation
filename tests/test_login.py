import pytest
from playwright.sync_api import expect


def test_login_amazon_site(amazon_pagae):
    """ Successfully login into amazon  site"""
    page = amazon_pagae
    expect(page.get_by_label("Amazon.in").first).to_be_visible()
    expect(page.locator("div.nav-fill").locator("nth=1")).to_be_visible()
    expect(page.locator("span.nav-cart-count")).to_be_visible()
    