"""
Test Case: Logout Functionality

===========================================
Test Steps
===========================================

1. Once the user is successfully logged in, click on the "Logout" button.


Expected Result:
----------------
The user should be logged out.

"""
import time

import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.logout_page import LogoutPage
from config import Config


@pytest.mark.sanity
@pytest.mark.regression
def test_logout(page):

    home_page = HomePage(page)
    my_account_page = MyAccountPage(page)
    login_page = LoginPage(page)
    logout_page = LogoutPage(page)

    # --- Step 1: Navigate to Login Page ---
    home_page.click_my_account()
    home_page.click_login()
    time.sleep(4)

    # --- Step 2: Enter Valid Credentials ---
    login_page.login(Config.email, Config.password)
    time.sleep(3)
    expect(my_account_page.get_my_account_page_heading()).to_be_visible()
    time.sleep(3)

    # 3 - Logout Page
    home_page.click_my_account()
    home_page.click_logout()
    time.sleep(4)
    expect(logout_page.get_continue_button()).to_be_visible(timeout=3000)
    time.sleep(4)
    logout_page.click_continue()
    time.sleep(4)
    validate_title = home_page.get_home_page_title()
    assert validate_title == "Your Store"
    time.sleep(4)
