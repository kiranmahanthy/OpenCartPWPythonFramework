from openpyxl.worksheet import page
from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page:Page):
        self.page = page

        # ===== Locators =====
        self.txt_email_address = page.locator("#input-email")
        self.txt_password = page.locator("#input-password")
        self.btn_submit = page.locator(".btn-primary")
        self.txt_error_msg = page.locator(".alert.alert-danger.alert-dismissible")

# ===== Action Methods =====
# Each method represents a user interaction on the page

    def login(self, email:str, password:str):
        try:
            self.txt_email_address.fill(email)
            self.txt_password.fill(password)
            self.btn_submit.click()
        except Exception as e:
            print(f" Invalid User Credentials: {e}")

    def get_login_error(self):
        """
        Return the error message element if login fails.
        Example use:
            error_text = login_page.get_login_error().inner_text()
        """
        try:
            return self.txt_error_message
        except Exception as e:
            print(f" Exception while fetching login error message: {e}")
            return None