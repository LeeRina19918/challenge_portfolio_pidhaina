import time

from pages.base_page import BasePage


class AddAPlayer(BasePage):
    expected_title = 'Add player'
    add_a_player_url = ('https://scouts-test.futbolkolektyw.pl/')

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.add_a_player_url) == self.expected_title