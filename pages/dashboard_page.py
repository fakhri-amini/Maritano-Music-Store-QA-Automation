from pages.base_page import BasePage
from locators.dashboard_locators import DashboardLocators


class DashboardPage(BasePage):

    def click_products(self):

        self.click(
            DashboardLocators.PRODUCT_MENU
        )

    def click_logout(self):

        self.click(
            DashboardLocators.LOGOUT_BUTTON
        )