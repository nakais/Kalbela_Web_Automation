import pytest
from selenium import webdriver
from page_objects.navigation_section import NavigationSection
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


def test_latest_link_click(setup):
    navigation_section = NavigationSection(setup)
    navigation_section.click_latest_link()
    assert "all-news" in setup.current_url  # Modify if needed


def test_national_link_click(setup):
    navigation_section = NavigationSection(setup)
    navigation_section.click_national_link()
    assert "national" in setup.current_url  # Modify if needed
