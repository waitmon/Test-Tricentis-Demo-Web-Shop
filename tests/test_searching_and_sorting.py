from pages.searching_and_sorting_page import SearchingAndSortingPage


class TestSearchingProcess:
    """Checking and validating of sorting and searching options(prices, item titles, view modes)."""

    def test_correct_input(self, driver):
        search = SearchingAndSortingPage(driver, 'https://demowebshop.tricentis.com/')
        search.open()
        items_quantity = search.check_correct_input()
        assert items_quantity == 4

    def test_incorrect_input(self, driver):
        search = SearchingAndSortingPage(driver, 'https://demowebshop.tricentis.com/')
        search.open()
        search_result = search.check_incorrect_input()
        assert search_result == 'No products were found that matched your criteria.'

    def test_sorting_low_to_high(self, driver):
        sorting = SearchingAndSortingPage(driver, 'https://demowebshop.tricentis.com/desktops')
        sorting.open()
        sorting.check_price_sorting_asc()

    def test_sorting_high_to_low(self, driver):
        sorting = SearchingAndSortingPage(driver, 'https://demowebshop.tricentis.com/desktops')
        sorting.open()
        sorting.check_price_sorting_desc()

    def test_sorting_a_to_z(self, driver):
        sorting = SearchingAndSortingPage(driver, 'https://demowebshop.tricentis.com/desktops')
        sorting.open()
        sorting.check_name_sorting_a_to_z()

    def test_sorting_z_to_a(self, driver):
        sorting = SearchingAndSortingPage(driver, 'https://demowebshop.tricentis.com/desktops')
        sorting.open()
        sorting.check_name_sorting_z_to_a()

    def test_filter_under_1k(self, driver):
        sorting = SearchingAndSortingPage(driver, 'https://demowebshop.tricentis.com/desktops')
        sorting.open()
        sorting.check_filter_under_1k()

    def test_filter_from_1k_to_1_2k(self, driver):
        sorting = SearchingAndSortingPage(driver, 'https://demowebshop.tricentis.com/desktops')
        sorting.open()
        sorting.check_filter_from_1k_to_1_2k()

    def test_filter_over_1k(self, driver):
        sorting = SearchingAndSortingPage(driver, 'https://demowebshop.tricentis.com/desktops')
        sorting.open()
        sorting.check_filter_over_1k()

    def test_display_4_per_page(self, driver):
        display = SearchingAndSortingPage(driver, 'https://demowebshop.tricentis.com/apparel-shoes')
        display.open()
        display.check_display_option_4()

    def test_display_8_per_page(self, driver):
        display = SearchingAndSortingPage(driver, 'https://demowebshop.tricentis.com/apparel-shoes')
        display.open()
        display.check_display_option_8()

    def test_display_12_per_page(self, driver):
        display = SearchingAndSortingPage(driver, 'https://demowebshop.tricentis.com/apparel-shoes')
        display.open()
        display.check_display_option_12()

    def test_view_mode_grid(self, driver):
        view_mode = SearchingAndSortingPage(driver, 'https://demowebshop.tricentis.com/jewelry')
        view_mode.open()
        view_mode.view_mode_grid()

    def test_view_mode_list(self, driver):
        view_mode = SearchingAndSortingPage(driver, 'https://demowebshop.tricentis.com/jewelry')
        view_mode.open()
        view_mode.view_mode_list()
