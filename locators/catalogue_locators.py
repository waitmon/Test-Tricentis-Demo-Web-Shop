from selenium.webdriver.common.by import By


class CatalogueLocators:
    """Set of locators referring to basic catalogue operations."""

    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[id="small-searchterms"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')
    PRODUCTS_TITLES = (By.CSS_SELECTOR, 'h2[class="product-title"]')
    NO_RESULT_TEXT = (By.CSS_SELECTOR, 'strong[class="result"]')
    SORT_BY_BUTTON = (By.CSS_SELECTOR, 'select[id="products-orderby"]')
    SORTING_OPTION_LOW_TO_HIGH = (By.CSS_SELECTOR, 'option[value="https://demowebshop.tricentis.com/desktops?orderby'
                                                   '=10"]')
    ACTUAL_PRICES = (By.CSS_SELECTOR, 'span[class="price actual-price"]')
    SORTING_OPTION_HIGH_TO_LOW = (By.CSS_SELECTOR, 'option[value="https://demowebshop.tricentis.com/desktops?orderby'
                                                   '=11"]')
    SORTING_OPTION_A_TO_Z = (By.CSS_SELECTOR, 'option[value="https://demowebshop.tricentis.com/desktops?orderby=5"]')
    SORTING_OPTION_Z_TO_A = (By.CSS_SELECTOR, 'option[value="https://demowebshop.tricentis.com/desktops?orderby=6"]')
    FILTER_UNDER_1000 = (By.CSS_SELECTOR, 'a[href="https://demowebshop.tricentis.com/desktops?price=-1000"]')
    FILTER_1000_1200 = (By.CSS_SELECTOR, 'a[href="https://demowebshop.tricentis.com/desktops?price=1000-1200"]')
    FILTER_OVER_1200 = (By.CSS_SELECTOR, 'a[href="https://demowebshop.tricentis.com/desktops?price=1200-"]')
    DISPLAY_BUTTON = (By.CSS_SELECTOR, 'select[id="products-pagesize"]')
    DISPLAY_OPTION_4_PER_PAGE = (By.CSS_SELECTOR, 'option[value="https://demowebshop.tricentis.com/apparel-shoes'
                                                  '?pagesize=4"]')
    DISPLAY_OPTION_8_PER_PAGE = (By.CSS_SELECTOR, 'option[value="https://demowebshop.tricentis.com/apparel-shoes'
                                                  '?pagesize=8"]')
    DISPLAY_OPTION_12_PER_PAGE = (By.CSS_SELECTOR, 'option[value="https://demowebshop.tricentis.com/apparel-shoes'
                                                   '?pagesize=12"]')
    VIEW_AS_BUTTON = (By.CSS_SELECTOR, 'select[id="products-viewmode"]')
    VIEW_MODE_GRID = (By.CSS_SELECTOR, 'option[value="https://demowebshop.tricentis.com/jewelry?viewmode=grid"]')
    VIEW_MODE_LIST = (By.CSS_SELECTOR, 'option[value="https://demowebshop.tricentis.com/jewelry?viewmode=list"]')

    # Electronics section

    CAMERA_PHOTO_SECTION = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[1]/div[1]/div/h2/a')
    CELL_PHONES_SECTION = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[1]/div[2]/div/h2/a')
    SMARTPHONE = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/h2/a')
    USED_PHONE = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/h2/a')
    PHONE_COVER = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div[3]/div/div[2]/h2/a')
    MANUFACTURER_DROPDOWN_MENU = (By.CSS_SELECTOR, 'select[id="product_attribute_80_2_37"]')
    MANUFACTURER_LIST = (By.CSS_SELECTOR, 'select[id="product_attribute_80_2_37"] option[value]')
    COLOR_DROPDOWN_MENU = (By.CSS_SELECTOR, 'select[id="product_attribute_80_1_38"]')
    COLOR_LIST = (By.CSS_SELECTOR, 'select[id="product_attribute_80_1_38"] option[value]')

    # Item page

    QUANTITY_FIELD = (By.CSS_SELECTOR, 'input[class="qty-input"]')
    ADD_TO_CART_BUTTON_PHONE_COVER = (By.CSS_SELECTOR, 'input[id="add-to-cart-button-80"]')
    ADD_TO_CART_BUTTON_SMARTPHONE = (By.CSS_SELECTOR, 'input[id="add-to-cart-button-43"]')
    CART_WARNING_TEXT = (By.CSS_SELECTOR, 'p[class="content"]')
    APPAREL_TOP_ITEM_PAGE = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div['
                                       '1]/div/div[2]/h2/a')
    ITEM_NAME = (By.CSS_SELECTOR, 'h1[itemprop="name"]')

    # Wishlist

    APPAREL_TOP_ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR, 'input[id="add-to-wishlist-button-5"]')
    WISHLIST_UPPER_MENU = (By.CSS_SELECTOR, 'span[class="wishlist-qty"]')
    REMOVE_FROM_WISHLIST_CHECKBOX = (By.CSS_SELECTOR, 'td[class="remove-from-cart"]')
    ADD_TO_CART_FROM_WISHLIST_CHECKBOX = (By.CSS_SELECTOR, 'input[name="addtocart"]')
    UPDATE_WISHLIST = (By.CSS_SELECTOR, 'input[name="updatecart"]')
    ADD_TO_CART_FROM_WISHLIST_BUTTON = (By.CSS_SELECTOR, 'input[name="addtocartbutton"]')
    EMPTY_WISH_LIST_TEXT = (By.CSS_SELECTOR, 'div[class="wishlist-content"]')
    ITEM_POLKA_TOP_WISHLIST_NAME = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div['
                                              '1]/form/table/tbody/tr/td[4]/a')
    ITEM_POLKA_TOP_CART_NAME = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/table/tbody/tr/td['
                                          '3]/a')

    # Main page urls lists

    ALL_LINKS = (By.XPATH, '//a[@href]')
