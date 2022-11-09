from pages.base_page import BasePage


class Dashboard(BasePage):
    scouts_panel_heading_xpath = "(//h6)[1]"
    main_page_button_xpath = "//ul[1]/div[1]"
    players_button_xpath = "//ul[1]/div[2]"
    language_button_xpath = "//ul[2]/div[1]"
    sign_out_button_xpath = "//ul[2]/div[2]"
    add_player_button_xpath = "//a[contains(@href,'add')]/button"
    dev_team_contact_xpath = "//a[contains(@target,'_')]"
    logo_scouts_panel_xpath = "//*[contains(@style,'url')]"
    menu_button_xpath = "//*[@aria-label="menu"]"
    players_count_panel_xpath = "//*[contains(@class,'elevation1')]"
    pass
