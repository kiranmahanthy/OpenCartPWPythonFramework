"""
Test Case: User Login Functionality

===========================================
Test Steps
===========================================

Test Case 1: Verify Login with Invalid Credentials
--------------------------------------------------
1. Open the application in the browser.
2. Navigate to the "My Account" menu on the Home page.
3. Click on the "Login" link.
4. Enter an invalid email address and password.
5. Click on the "Login" button.
6. Verify that an error message appears indicating invalid credentials.

Expected Result:
----------------
An error message should be displayed, and the user should not be logged in.


Test Case 2: Verify Login with Valid Credentials
------------------------------------------------
1. Open the application in the browser.
2. Navigate to the "My Account" menu on the Home page.
3. Click on the "Login" link.
4. Enter a valid email address and password.
5. Click on the "Login" button.
6. Verify that the "My Account" page is displayed after successful login.

Expected Result:
----------------
The "My Account" page should appear, confirming a successful login.
"""

import time
import pytest
from playwright.sync_api import expect

from pages import my_account_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from config import Config  # Configuration file holding credentials


@pytest.mark.sanity
@pytest.mark.regression
def test_invalid_user_login(page):
    """
    Automated Test Case: Verify that login fails for invalid user credentials.
    """

    # --- Page Object Initialization ---
    home_page = HomePage(page)
    login_page = LoginPage(page)

    # --- Step 1: Navigate to Login Page ---
    home_page.click_my_account()
    home_page.click_login()

    # --- Step 2: Enter Invalid Credentials ---
    login_page.login(Config.invalid_email, Config.invalid_password)
    expect(login_page.get_login_error()).to_be_visible()

@pytest.mark.sanity
@pytest.mark.regression
def test_valid_user_login(page):
    """
    Automated Test Case: Verify that login fails for invalid user credentials.
    """

    # --- Page Object Initialization ---
    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_account_page = MyAccountPage(page)

    # --- Step 1: Navigate to Login Page ---
    home_page.click_my_account()
    time.sleep(3)
    home_page.click_login()
    time.sleep(3)

    # --- Step 2: Enter Valid Credentials ---
    login_page.login(Config.email, Config.password)
    time.sleep(3)
    expect(my_account_page.get_my_account_page_heading()).to_be_visible()

