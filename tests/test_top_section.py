import pytest
from selenium import webdriver
from page_objects.top_section import TopSection
import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.kalbela.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_logo_click(setup):
    top_section = TopSection(setup)
    top_section.click_logo()
    assert "www.kalbela.com" in setup.current_url


def test_search_icon_click(setup):
    top_section = TopSection(setup)
    top_section.click_search_icon()
    top_section.search("বাংলাদেশ")  # Replace with any search term
    assert "search" in setup.current_url


def test_bell_icon_click(setup):
    top_section = TopSection(setup)
    top_section.click_bell_icon()
    assert setup.current_url == "https://www.kalbela.com/#"  # Modify if needed
