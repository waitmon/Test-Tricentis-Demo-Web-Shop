from locators.catalogue_locators import CatalogueLocators
from pages.base_page import BasePage


class WishListCartPage(BasePage):
    """Methods for basic wishlist operations: adding to wishlist/cart, removing items."""

    locators = CatalogueLocators()

    def add_item_to_wishlist(self):
        self.element_is_present(self.locators.APPAREL_TOP_ITEM_PAGE).click()
        self.element_is_present(self.locators.APPAREL_TOP_ADD_TO_WISHLIST_BUTTON).click()
        return self.element_is_present(self.locators.CART_WARNING_TEXT).text

    def remove_item_from_wishlist(self):
        self.element_is_present(self.locators.APPAREL_TOP_ITEM_PAGE).click()
        self.element_is_present(self.locators.APPAREL_TOP_ADD_TO_WISHLIST_BUTTON).click()
        self.element_is_present(self.locators.WISHLIST_UPPER_MENU).click()
        self.element_is_present(self.locators.REMOVE_FROM_WISHLIST_CHECKBOX).click()
        self.element_is_present(self.locators.UPDATE_WISHLIST).click()
        return self.element_is_present(self.locators.EMPTY_WISH_LIST_TEXT).text

    def add_item_from_wishlist_to_cart(self):
        self.element_is_present(self.locators.APPAREL_TOP_ITEM_PAGE).click()
        item_name = self.element_is_present(self.locators.ITEM_NAME).text
        self.element_is_present(self.locators.APPAREL_TOP_ADD_TO_WISHLIST_BUTTON).click()
        self.element_is_present(self.locators.WISHLIST_UPPER_MENU).click()
        item_wishlist_name = self.element_is_present(self.locators.ITEM_POLKA_TOP_WISHLIST_NAME).text
        self.element_is_present(self.locators.ADD_TO_CART_FROM_WISHLIST_CHECKBOX).click()
        self.element_is_present(self.locators.ADD_TO_CART_FROM_WISHLIST_BUTTON).click()
        item_cart_name = self.element_is_present(self.locators.ITEM_POLKA_TOP_CART_NAME).text
        assert item_name == item_wishlist_name == item_cart_name
