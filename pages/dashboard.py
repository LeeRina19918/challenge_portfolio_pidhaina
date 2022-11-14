import time
from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = 'Scouts panel'
    dashboard_url = ('https://scouts-test.futbolkolektyw.pl/')
    # scouts_panel_heading_xpath = "(//h6)[1]"
    # main_page_button_xpath = "//ul[1]/div[1]"
    # players_button_xpath = "//ul[1]/div[2]"
    # language_button_xpath = "//ul[2]/div[1]"
    # sign_out_button_xpath = "//ul[2]/div[2]"
    add_player_button_xpath = "//a[contains(@href,'add')]/button"
    # dev_team_contact_xpath = "//a[contains(@target,'_')]"
    # logo_scouts_panel_xpath = "//*[contains(@style,'url')]"
    # menu_button_xpath = "//*[@aria-label='menu']"
    # players_count_panel_xpath = "//*[contains(@class,'elevation1')]"

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_add_a_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)
