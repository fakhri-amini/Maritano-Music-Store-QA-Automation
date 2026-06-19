from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_by_id(self, locator):
        return self.driver.find_element(
            By.ID,
            locator
        )

    def click(self, locator):
        self.find_element_by_id(locator).click()

    def enter_text(self, locator, text):

        element = self.find_element_by_id(locator)

        element.clear()

        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element_by_id(locator).text