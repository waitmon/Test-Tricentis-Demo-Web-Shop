from pages.base_page import BasePage
from locators.catalogue_locators import CatalogueLocators
import requests


class UrlsPage(BasePage):
    """Methods for getting 200 status code from top-menu presented links"""
    locators = CatalogueLocators()

    def check_top_menu_urls(self):
        urls = ['https://demowebshop.tricentis.com/books', 'https://demowebshop.tricentis.com/computers',
                'https://demowebshop.tricentis.com/desktops', 'https://demowebshop.tricentis.com/notebooks',
                'https://demowebshop.tricentis.com/accessories', 'https://demowebshop.tricentis.com/electronics',
                'https://demowebshop.tricentis.com/camera-photo', 'https://demowebshop.tricentis.com/cell-phones',
                'https://demowebshop.tricentis.com/apparel-shoes',
                'https://demowebshop.tricentis.com/digital-downloads',
                'https://demowebshop.tricentis.com/jewelry', 'https://demowebshop.tricentis.com/gift-cards']

        for url in urls:
            response = requests.get(url)
            assert response.status_code == 200
