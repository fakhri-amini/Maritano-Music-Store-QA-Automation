from config.config import BASE_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.test_data import (
    LOGIN_USERNAME,
    LOGIN_PASSWORD,
    NEW_PRODUCT_NAME,
    NEW_PRODUCT_CATEGORY,
    NEW_PRODUCT_PRICE,
    NEW_PRODUCT_IMAGE,
    UPDATED_PRODUCT_NAME
)

from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_add_product(driver):

    driver.get(
        f"{BASE_URL}/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        LOGIN_USERNAME,
        LOGIN_PASSWORD
    )

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "dashboardTitle")
        )
    )

    product_page = ProductPage(driver)

    product_page.open_product_menu()

    product_page.click_add_product()

    product_page.enter_product_name(
        NEW_PRODUCT_NAME
    )

    product_page.enter_category(
        NEW_PRODUCT_CATEGORY
    )

    product_page.enter_price(
        NEW_PRODUCT_PRICE
    )

    product_page.enter_image(
        NEW_PRODUCT_IMAGE
    )

    product_page.save_product()

    assert NEW_PRODUCT_NAME in driver.page_source


def test_edit_product(driver):

    driver.get(
        f"{BASE_URL}/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        LOGIN_USERNAME,
        LOGIN_PASSWORD
    )

    product_page = ProductPage(driver)

    product_page.open_product_menu()

    product_page.click_edit_product()

    product_page.enter_edit_product_name(
        UPDATED_PRODUCT_NAME
    )

    product_page.click_update_product()

    assert UPDATED_PRODUCT_NAME in driver.page_source

def test_delete_product(driver):

    driver.get(
        f"{BASE_URL}/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        LOGIN_USERNAME,
        LOGIN_PASSWORD
    )

    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, "dashboardTitle")
            )
        )

    assert "dashboard" in driver.current_url