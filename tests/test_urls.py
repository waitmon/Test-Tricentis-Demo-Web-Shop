from pages.urls_page import UrlsPage


class TestUrls:
    """Checking 2000 status code of top menu links"""

    def test_urls_status_codes(self, driver):
        main_page = UrlsPage(driver, 'https://demowebshop.tricentis.com/')
        main_page.open()
        main_page.check_top_menu_urls()

