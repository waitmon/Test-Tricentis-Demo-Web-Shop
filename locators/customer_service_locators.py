from selenium.webdriver.common.by import By


class BlogPageLocators:
    """Set of locators referring to Blog page."""

    ARTICLE1_TITLE = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div[1]/a')
    ARTICLE1_CONTENT = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div[2]/p[1]')
    ARTICLE2_TITLE = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[1]/a')
    ARTICLE2_CONTENT = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/p')
