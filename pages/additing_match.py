from pages.base_page import BasePage


class AdditingMatch(BasePage):
    adding_match_card_header_xpath = "//form/div[1]"
    my_team_label_xpath = "//label[text()="My team"]"
    enemy_team_label_asterisk_xpath = "//label[text()="Enemy team"]/span"
    my_team_score_field_xpath = "//input[@name="myTeamScore"]"
    date_select_field_xpath = "//input[@name="date"]"
    match_out_home_box_xpath = "//label[2]//input"
    submit_button_xpath = "//button[@type="submit"]"
    clear_button_xpath = "//button[2][@type="button"]"
    reports_button_xpath = "//ul/div[3]"
    matches_button_xpath = "//div[contains(@class,'jss915')]/parent::div"
    pass