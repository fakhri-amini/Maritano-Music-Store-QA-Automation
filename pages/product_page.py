from pages.base_page import BasePage
from locators.product_locators import ProductLocators

class ProductPage(BasePage):

    def open_product_menu(self):
        self.click(
            ProductLocators.PRODUCT_MENU
        )

    def click_add_product(self):
        self.click(
            ProductLocators.ADD_PRODUCT_BTN
        )

    def enter_product_name(self, name):
        self.enter_text(
            ProductLocators.PRODUCT_NAME,
            name
        )

    def enter_category(self, category):
        self.enter_text(
            ProductLocators.PRODUCT_CATEGORY,
            category
        )

    def enter_price(self, price):
        self.enter_text(
            ProductLocators.PRODUCT_PRICE,
            str(price)
        )

    def enter_image(self, image):
        self.enter_text(
            ProductLocators.PRODUCT_IMAGE,
            image
        )

    def save_product(self):
        self.click(
            ProductLocators.SAVE_PRODUCT_BTN
        )

    def click_edit_product(self):
        self.click(
            ProductLocators.EDIT_PRODUCT_BTN
        )

    def enter_edit_product_name(self, name):
        self.enter_text(
            ProductLocators.EDIT_PRODUCT_NAME,
            name
        )

    def click_update_product(self):
        self.click(
            ProductLocators.UPDATE_PRODUCT_BTN
        )

    def click_delete_product(self):

        self.click(
            ProductLocators.DELETE_PRODUCT_BTN
    )