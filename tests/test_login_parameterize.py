"""
Test Case: User Login Functionality using Parameterization
The test data is passed through data files.
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
from utilities.data_reader_util import read_csv_data, read_json_data, read_excel_data

# Load/read the data from the test data files

csv_data = read_csv_data("testdata/logindata.csv")
json_data = read_json_data("testdata/logindata.json")
excel_data = read_excel_data("testdata/logindata.xlsx")

@pytest.mark.datadriven
@pytest.mark.parametrize("testName,email,password,expected",excel_data)

def test_login_datadriven(page, testName, email, password, expected):
    """
    Automated Test Case: Verify that login fails for invalid user credentials.
    """

    # --- Page Object Initialization ---
    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_account_page = MyAccountPage(page)

    # --- Step 1: Navigate to Login Page ---
    home_page.click_my_account()
    home_page.click_login()

    # --- Step 2: Enter Invalid Credentials ---
    login_page.login(email, password)
    time.sleep(5)

    if expected == "success":
        expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=3000)
    else:
        expect(login_page.get_login_error()).to_be_visible(timeout=3000)
