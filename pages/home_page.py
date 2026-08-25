from playwright.sync_api import Page

class HomePage:
    def __init__(self, page:Page):
        self.page = page

        # ===== Locators =====
        self.link_my_account = page.locator("span:has-text('My Account')")
        self.link_register = page.locator("a:has-text('Register')")
        self.link_login = page.locator("a:has-text('Register')")
        self.txt_search = page.locator("input[name='search']")
        self.btn_search = page.locator("#search button[type='button']")

    # ===== Action Methods =====
    # Each method represents a user interaction on the page

    def get_home_page_title(self):
        return self.page.title()

    def click_my_account(self):
        """Click on the 'My Account' link."""
        try:
            self.link_my_account.click()
        except Exception as e:
            print(f" Exception while clicking 'My Account': {e}")
            raise

    def click_register(self):
        """Click on the 'Register' link."""
        try:
            self.link_register.click()
        except Exception as e:
            print(f" Exception while clicking 'Register': {e}")
            raise

    def click_login(self):
        """Click on the 'Login' link."""
        try:
            self.link_login.click()
        except Exception as e:
            print(f" Exception while clicking 'Login': {e}")
            raise

    def search_product_name(self, product_name):
        """Click on the 'Search' link."""
        try:
            self.txt_search.fill(product_name)
            self.btn_search.click()
        except Exception as e:
            print(f" Exception while searching product name '{product_name}': {e}")
            raise
