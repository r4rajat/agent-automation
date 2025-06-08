"""
Conftest file for pytest fixtures.
"""

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser():
    """
    Create a browser instance for the test.
    """
    with sync_playwright() as playwright:
        # Launch browser with options
        browser = playwright.chromium.launch(headless=False, slow_mo=100)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    """
    Create a new browser page for the test.
    """
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
