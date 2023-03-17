from pages.cs_page import BlogPage


class TestBlogPage:
    """Checking contains and length in "Blog" section"""

    def test_cservice_articles_len(self, driver):
        blog = BlogPage(driver, 'https://demowebshop.tricentis.com/blog')
        blog.open()
        article1_title, article1_content = blog.check_article_lens('Customer Service - Client Service')
        article2_title, article2_content = blog.check_article_lens('Online Discount Coupons')
        assert article1_title == 'Customer Service - Client Service' and article1_content != 0
        assert article2_title == 'Online Discount Coupons' and article2_content != 0
