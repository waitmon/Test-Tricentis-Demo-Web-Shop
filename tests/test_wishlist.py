from pages.wishlist_cart_page import WishListCartPage


class TestWishlistOperations:
    """Checking wishlist related options and actions (removing, adding items)"""

    def test_add_item_to_wishlist(self, driver):
        wishlist_test = WishListCartPage(driver, 'https://demowebshop.tricentis.com/apparel-shoes')
        wishlist_test.open()
        smoke_test = wishlist_test.add_item_to_wishlist()
        assert smoke_test == 'The product has been added to your wishlist'

    def test_remove_item_from_wishlist(self, driver):
        wishlist_test = WishListCartPage(driver, 'https://demowebshop.tricentis.com/apparel-shoes')
        wishlist_test.open()
        smoke_test = wishlist_test.remove_item_from_wishlist()
        assert smoke_test == 'The wishlist is empty!'

    def test_add_item_from_wishlist_to_cart(self, driver):
        wishlist_test = WishListCartPage(driver, 'https://demowebshop.tricentis.com/apparel-shoes')
        wishlist_test.open()
        wishlist_test.add_item_from_wishlist_to_cart()


