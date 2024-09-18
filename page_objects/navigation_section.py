from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class NavigationSection(BasePage):
    LATEST_LINK = (By.XPATH, '//*[@id="top-nav"]/div/div/nav/ul/li[1]/a[2]')
    NATIONAL_LINK = (By.XPATH, '//*[@id="top-nav"]/div/div/nav/ul/li[2]/a')

    def click_latest_link(self):
        self.click(self.LATEST_LINK)

    def click_national_link(self):
        self.click(self.NATIONAL_LINK)
