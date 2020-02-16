from classes.Commands import *


class ExploreFog:
    def __init__(self):
        pass

    @staticmethod
    def start():
        is_verify_on = IsVerifyOn()
        check_antibot = CheckAntibot()
        go_home = GoHome()
        move_to_scout_camp_and_click = MoveToScoutCampAndClick()
        click_monocular = ClickDurbin()
        search_explore_button = SearchExploreButton()
        click_first_explore_button = ClickExploreButton()
        click_second_explore_button = ClickExploreButton2()
        click_send_button = SendScoutButton()
        # define execution queue
        is_verify_on.set_successor(check_antibot)
        check_antibot.set_successor(go_home)
        go_home.set_successor(move_to_scout_camp_and_click)
        move_to_scout_camp_and_click.set_successor(click_monocular)
        click_monocular.set_successor(search_explore_button)
        search_explore_button.set_successor(click_first_explore_button)
        click_first_explore_button.set_successor(click_second_explore_button)
        click_second_explore_button.set_successor(click_send_button)

        is_verify_on.do_work()
