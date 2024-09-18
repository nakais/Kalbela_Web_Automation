from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from page_objects.base_page import BasePage


class TopSection(BasePage):
    LOGO = (By.XPATH, '//*[@id="midHeader"]/div[2]/div/div[1]/a/img')
    SEARCH_ICON = (By.XPATH, '//*[@id="dropdownSearch"]')
    SEARCH_INPUT = (By.XPATH, '//*[@id="navigation"]/div/div/span[1]/div/div/div/input')
    BELL_ICON = (By.XPATH, '//*[@id="dropdownNotification"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_logo(self):
        self.click(self.LOGO)

    def click_search_icon(self):
        # Scroll into view to ensure it's visible
        search_icon = self.wait.until(EC.element_to_be_clickable(self.SEARCH_ICON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", search_icon)
        search_icon.click()

    def search(self, search_term):
        # Wait for the search input to be visible
        search_input = self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT))
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.RETURN)

    def click_bell_icon(self):
        self.click(self.BELL_ICON)
