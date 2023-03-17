from pages.catalogue_page import CataloguePage


class TestCatalogueOperations:
    """Browsing catalogue, testing boundary quantity values, checking item available options (colors, quantity,
    model etc)."""

    def test_phones_section_available_options(self, driver):
        catalogue_page = CataloguePage(driver, 'https://demowebshop.tricentis.com/electronics')
        catalogue_page.open()
        catalogue_page.check_phone_cover_options()

    def test_smoke_phone_cover_add_to_cart(self, driver):
        catalogue_page = CataloguePage(driver, 'https://demowebshop.tricentis.com/electronics')
        catalogue_page.open()
        smoke_test = catalogue_page.add_phone_cover_to_cart()
        assert smoke_test == 'The product has been added to your shopping cart'

    def test_negative_qty_add_to_cart(self, driver):
        catalogue_page = CataloguePage(driver, 'https://demowebshop.tricentis.com/electronics')
        catalogue_page.open()
        negative_test = catalogue_page.add_negative_qty_values()
        assert negative_test == 'Quantity should be positive'

    def test_over_limit_qty_add_to_cart(self, driver):
        catalogue_page = CataloguePage(driver, 'https://demowebshop.tricentis.com/electronics')
        catalogue_page.open()
        negative_test = catalogue_page.add_over_limit_qty_values()
        assert negative_test == 'The maximum quantity allowed for purchase is 10000.'

