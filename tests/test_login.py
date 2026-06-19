from selenium.webdriver.common.by import By
import time

from config.config import BASE_URL
from tests.test_data import LOGIN_USERNAME, LOGIN_PASSWORD
from pages.login_page import LoginPage


def test_login_success(driver):

    driver.get(f"{BASE_URL}/login")

    login_page = LoginPage(driver)

    login_page.login(
        LOGIN_USERNAME,
        LOGIN_PASSWORD
    )

    print("\nCURRENT URL =", driver.current_url)

    print("\nPAGE TITLE =", driver.title)

    time.sleep(3)

    assert driver.find_element(
        By.ID,
        "dashboardTitle"
    ).is_displayed()