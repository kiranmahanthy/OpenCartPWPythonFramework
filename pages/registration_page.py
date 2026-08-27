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
        self.btn_continue = page.locator("input.input") # if class is used then input[class=input] can be used
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
    

    def complete_registration(self, user_data:dict):
        self.txt_first_name.fill(user_data["firstName"])
        self.txt_last_name.fill(user_data["lastName"])
        self.txt_email.fill(user_data["email"])
        self.txt_telephone.fill(user_data["telephone"])
        self.txt_password.fill(user_data["password"])
        self.txt_confirm_password.fill(user_data["password"])
        self.set_privacy_policy()
        self.click_continue()






