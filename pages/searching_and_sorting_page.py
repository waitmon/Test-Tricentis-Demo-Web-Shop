from locators.catalogue_locators import CatalogueLocators
from pages.base_page import BasePage


class SearchingAndSortingPage(BasePage):
    """Methods for validating of searching inputs, sorting and page-view options."""

    locators = CatalogueLocators()

    def check_correct_input(self):
        self.element_is_present(self.locators.SEARCH_FIELD).click()
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys('computer')
        self.element_is_present(self.locators.SEARCH_BUTTON).click()
        return len(self.elements_are_present(self.locators.PRODUCTS_TITLES))

    def check_incorrect_input(self):
        self.element_is_present(self.locators.SEARCH_FIELD).click()
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys('ноутбук')
        self.element_is_present(self.locators.SEARCH_BUTTON).click()
        return self.element_is_present(self.locators.NO_RESULT_TEXT).text

    def check_price_sorting_asc(self):
        self.element_is_present(self.locators.SORT_BY_BUTTON).click()
        self.element_is_present(self.locators.SORTING_OPTION_LOW_TO_HIGH).click()
        actual_prices = self.elements_are_present(self.locators.ACTUAL_PRICES)
        price_list_ascending_order = []
        for price in actual_prices:
            current_price = float(price.text)
            price_list_ascending_order.append(current_price)
        assert price_list_ascending_order == sorted(price_list_ascending_order)

    def check_price_sorting_desc(self):
        self.element_is_present(self.locators.SORT_BY_BUTTON).click()
        self.element_is_present(self.locators.SORTING_OPTION_HIGH_TO_LOW).click()
        actual_prices = self.elements_are_present(self.locators.ACTUAL_PRICES)
        price_list_descending_order = []
        for price in actual_prices:
            current_price = float(price.text)
            price_list_descending_order.append(current_price)
        assert price_list_descending_order == sorted(price_list_descending_order, reverse=True)

    def check_name_sorting_a_to_z(self):
        self.element_is_present(self.locators.SORT_BY_BUTTON).click()
        self.element_is_present(self.locators.SORTING_OPTION_A_TO_Z).click()
        products_titles = self.elements_are_present(self.locators.PRODUCTS_TITLES)
        products_list_a_to_z = []
        for name in products_titles:
            product_name = name.text
            products_list_a_to_z.append(product_name)
        assert products_list_a_to_z == sorted(products_list_a_to_z)

    def check_name_sorting_z_to_a(self):
        self.element_is_present(self.locators.SORT_BY_BUTTON).click()
        self.element_is_present(self.locators.SORTING_OPTION_Z_TO_A).click()
        products_titles = self.elements_are_present(self.locators.PRODUCTS_TITLES)
        products_list_z_to_a = []
        for name in products_titles:
            product_name = name.text
            products_list_z_to_a.append(product_name)
        assert products_list_z_to_a == sorted(products_list_z_to_a, reverse=True)

    def check_filter_under_1k(self):
        self.element_is_present(self.locators.FILTER_UNDER_1000).click()
        actual_prices = self.elements_are_present(self.locators.ACTUAL_PRICES)
        price_list = []
        for price in actual_prices:
            listed_price = float(price.text)
            price_list.append(listed_price)
        assert any(filter_price < 1000.00 for filter_price in price_list)

    def check_filter_from_1k_to_1_2k(self):
        self.element_is_present(self.locators.FILTER_1000_1200).click()
        actual_prices = self.elements_are_present(self.locators.ACTUAL_PRICES)
        price_list = []
        for price in actual_prices:
            listed_price = float(price.text)
            price_list.append(listed_price)
        assert any(1000.00 <= filter_price <= 1200.00 for filter_price in price_list)

    def check_filter_over_1k(self):
        self.element_is_present(self.locators.FILTER_1000_1200).click()
        actual_prices = self.elements_are_present(self.locators.ACTUAL_PRICES)
        price_list = []
        for price in actual_prices:
            listed_price = float(price.text)
            price_list.append(listed_price)
        assert any(filter_price >= 1200.00 for filter_price in price_list)

    def check_display_option_4(self):
        self.element_is_present(self.locators.DISPLAY_BUTTON).click()
        self.element_is_present(self.locators.DISPLAY_OPTION_4_PER_PAGE).click()
        product_titles = self.elements_are_present(self.locators.PRODUCTS_TITLES)
        product_qty_list = []
        for name in product_titles:
            product_name = name.text
            product_qty_list.append(product_name)
        assert len(product_qty_list) == 4

    def check_display_option_8(self):
        self.element_is_present(self.locators.DISPLAY_BUTTON).click()
        self.element_is_present(self.locators.DISPLAY_OPTION_8_PER_PAGE).click()
        product_titles = self.elements_are_present(self.locators.PRODUCTS_TITLES)
        product_qty_list = []
        for name in product_titles:
            product_name = name.text
            product_qty_list.append(product_name)
        assert len(product_qty_list) == 8

    def check_display_option_12(self):
        self.element_is_present(self.locators.DISPLAY_BUTTON).click()
        self.element_is_present(self.locators.DISPLAY_OPTION_12_PER_PAGE).click()
        product_titles = self.elements_are_present(self.locators.PRODUCTS_TITLES)
        product_qty_list = []
        for name in product_titles:
            product_name = name.text
            product_qty_list.append(product_name)
        assert len(product_qty_list) == 12

    def view_mode_grid(self):
        self.element_is_present(self.locators.VIEW_AS_BUTTON).click()
        self.element_is_present(self.locators.VIEW_MODE_GRID).click()
        grid_option = self.element_is_present(self.locators.VIEW_MODE_GRID)
        grid_checked = grid_option.get_attribute("selected")
        assert grid_checked is not None

    def view_mode_list(self):
        self.element_is_present(self.locators.VIEW_AS_BUTTON).click()
        self.element_is_present(self.locators.VIEW_MODE_LIST).click()
        list_option = self.element_is_present(self.locators.VIEW_MODE_LIST)
        list_checked = list_option.get_attribute("selected")
        assert list_checked is not None
