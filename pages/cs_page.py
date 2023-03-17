from locators.customer_service_locators import BlogPageLocators
from pages.base_page import BasePage


class BlogPage(BasePage):
    """Methods for checking of length of content and article content itself."""
    locators = BlogPageLocators()

    def check_article_lens(self, article_title):
        titles = {'Customer Service - Client Service':
            {
                'title': self.locators.ARTICLE1_TITLE,
                'content': self.locators.ARTICLE1_CONTENT
            },
            'Online Discount Coupons':
                {
                    'title': self.locators.ARTICLE2_TITLE,
                    'content': self.locators.ARTICLE2_CONTENT
                },

        }
        blog_titles = self.element_is_present(titles[article_title]['title'])
        title_contents = self.element_is_present(titles[article_title]['content']).text
        return blog_titles.text, len(title_contents)
