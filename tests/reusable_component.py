import pytest
from playwright.sync_api import expect

from pages import registration_page, search_results_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage



# -------------------------------------------------------------
# Helper Function: Login
# -------------------------------------------------------------
def perform_login(page, email, password):
    home = HomePage(page)
    home.click_my_account()
    home.click_login()

    login = LoginPage(page)
    login.login(email, password)

    my_account_page = MyAccountPage(page)
    # Verify successful login by checking 'My Account' page presence
    #expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=3000)


