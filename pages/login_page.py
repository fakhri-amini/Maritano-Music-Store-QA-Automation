from pages.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def enter_username(self, username):

        self.enter_text(
            LoginLocators.USERNAME,
            username
        )

    def enter_password(self, password):

        self.enter_text(
            LoginLocators.PASSWORD,
            password
        )

    def click_login(self):

        self.click(
            LoginLocators.LOGIN_BUTTON
        )

    def login(self, username, password):

        self.enter_username(username)

        self.enter_password(password)

        self.click_login()