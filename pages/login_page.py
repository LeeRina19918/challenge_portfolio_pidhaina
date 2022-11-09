from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//input[starts-with(@id,'p')]"
    sign_in_button_xpath = "//div[2]/button"
    language_select_menu_xpath = "//*[@role='button']"
    scouts_panel_xpath = "//h5[not(@id)]"
    remaind_password_xpath = "//*[contains(@class,'jss37')]"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
