import random
from locators.catalogue_locators import CatalogueLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class CataloguePage(BasePage):
    """Methods for catalogue operations: browsing, inputting boundary quantity values, checking item available
    options."""
    locators = CatalogueLocators()

    def check_phone_cover_options(self):
        self.element_is_present(self.locators.CELL_PHONES_SECTION).click()
        self.element_is_present(self.locators.PHONE_COVER).click()
        self.element_is_present(self.locators.MANUFACTURER_DROPDOWN_MENU).click()
        manufacturers = self.elements_are_present(self.locators.MANUFACTURER_LIST)
        available_manufacturers_list = []
        for title in manufacturers:
            manufacturer_title = title.text
            available_manufacturers_list.append(manufacturer_title)
        assert len(available_manufacturers_list) == 2
        self.element_is_present(self.locators.COLOR_DROPDOWN_MENU).click()
        colors = self.elements_are_present(self.locators.COLOR_LIST)
        available_colors_list = []
        for color in colors:
            color_title = color.text
            available_colors_list.append(color_title)
        assert available_colors_list == ['Black', 'White', 'Blue', 'Yellow']

    def add_phone_cover_to_cart(self):
        self.element_is_present(self.locators.CELL_PHONES_SECTION).click()
        self.element_is_present(self.locators.PHONE_COVER).click()
        self.element_is_present(self.locators.MANUFACTURER_DROPDOWN_MENU).click()
        Select(self.element_is_present(self.locators.MANUFACTURER_DROPDOWN_MENU)).select_by_index(
            random.randint(0, len(self.locators.MANUFACTURER_DROPDOWN_MENU) - 1))
        self.element_is_present(self.locators.COLOR_DROPDOWN_MENU).click()
        Select(self.element_is_present(self.locators.COLOR_DROPDOWN_MENU)).select_by_index(
            random.randint(0, len(self.locators.COLOR_DROPDOWN_MENU) - 1))
        self.element_is_present(self.locators.QUANTITY_FIELD).clear()
        positive_values = ['1', '10000', '2', '9999', '32']
        self.element_is_visible(self.locators.QUANTITY_FIELD).send_keys(random.choice(positive_values))
        self.element_is_present(self.locators.ADD_TO_CART_BUTTON_PHONE_COVER).click()
        return self.element_is_present(self.locators.CART_WARNING_TEXT).text

    def add_negative_qty_values(self):
        self.element_is_present(self.locators.CELL_PHONES_SECTION).click()
        self.element_is_present(self.locators.SMARTPHONE).click()
        self.element_is_present(self.locators.QUANTITY_FIELD).click()
        self.element_is_present(self.locators.QUANTITY_FIELD).clear()
        negative_values = ['-1', '0', '-10000', 'ten', 'overninethousands']
        self.element_is_visible(self.locators.QUANTITY_FIELD).send_keys(random.choice(negative_values))
        self.element_is_present(self.locators.ADD_TO_CART_BUTTON_SMARTPHONE).click()
        return self.element_is_present(self.locators.CART_WARNING_TEXT).text

    def add_over_limit_qty_values(self):
        self.element_is_present(self.locators.CELL_PHONES_SECTION).click()
        self.element_is_present(self.locators.SMARTPHONE).click()
        self.element_is_present(self.locators.QUANTITY_FIELD).click()
        self.element_is_present(self.locators.QUANTITY_FIELD).clear()
        exceeded_values = ['10001', '20000', '30000']
        self.element_is_visible(self.locators.QUANTITY_FIELD).send_keys(random.choice(exceeded_values))
        self.element_is_present(self.locators.ADD_TO_CART_BUTTON_SMARTPHONE).click()
        return self.element_is_present(self.locators.CART_WARNING_TEXT).text
