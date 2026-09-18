from playwright.sync_api import Page


class RegistrationPage:
    def __init__(self, page:Page):
        self.page = page

        # ===== Locators =====
        self.txt_first_name = page.locator("#input-firstname")
        self.txt_last_name = page.locator("#input-lastname")
        self.txt_email = page.locator("#input-email")
        self.txt_telephone = page.locator("#input-telephone")
        self.txt_password = page.locator("#input-password")
        self.txt_confirm_password = page.locator("#input-confirm")
        self.radiobtn_subscribe_yes = page.get_by_label("Yes")
        self.radiobtn_subscribe_no = page.get_by_label("No")
        self.chk_policy = page.locator("input[name=agree]")
        self.btn_continue = page.locator("input[value='Continue']") # if class is used then input[class=input] can be used
        self.msg_confirmation = page.locator('h1:has-text("Your Account Has Been Created!")')

# ===== Action Methods =====
# Each method represents a user interaction on the page
    def set_privacy_policy(self):
        """Select the 'Privacy Policy' checkbox."""
        self.chk_policy.check()

    def click_continue(self):
        """Click on the 'Continue' button to submit the registration form."""
        self.btn_continue.click()

    def get_confirmation_msg(self):
        """
        Return the confirmation message locator.
        This can be used to verify successful registration.
        """
        return self.msg_confirmation

    def subscribe_newsletter(self, user_choice):
        if user_choice:
            self.radiobtn_subscribe_yes.click()
        else:
            self.radiobtn_subscribe_no.click()
    

    '''def complete_registration(self, user_data:dict):
        self.txt_first_name.fill(user_data["first_name"])
        self.txt_last_name.fill(user_data["last_name"])
        self.txt_email.fill(user_data["email"])
        self.txt_telephone.fill(user_data["telephone"])
        self.txt_password.fill(user_data["password"])
        self.txt_confirm_password.fill(user_data["password"])
        self.set_privacy_policy()
        self.click_continue()'''

    # ===== Action Methods =====

    def set_first_name(self, fname: str):
        """Enter the user's first name into the 'First Name' field."""
        self.txt_first_name.fill(fname)

    def set_last_name(self, lname: str):
        """Enter the user's last name into the 'Last Name' field."""
        self.txt_last_name.fill(lname)

    def set_email(self, email: str):
        """Enter the user's email address."""
        self.txt_email.fill(email)

    def set_telephone(self, tel: str):
        """Enter the user's telephone number."""
        self.txt_telephone.fill(tel)

    def set_password(self, pwd: str):
        """Enter the password."""
        self.txt_password.fill(pwd)

    def set_confirm_password(self, pwd: str):
        """Re-enter the password in the 'Confirm Password' field."""
        self.txt_confirm_password.fill(pwd)

    def set_privacy_policy(self):
        """Select the 'Privacy Policy' checkbox."""
        self.chk_policy.check()

    def click_continue(self):
        """Click on the 'Continue' button to submit the registration form."""
        self.btn_continue.click()

    def get_confirmation_msg(self):
        """
        Return the confirmation message locator.
        This can be used to verify successful registration.
        """
        return self.msg_confirmation






