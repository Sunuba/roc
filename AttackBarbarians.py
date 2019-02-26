from classes.Commands import CheckAntibot, CheckActionPoint, GoOutside, ClickSearchButton
from classes.Commands import ClickSearchTargetButton, ClickBarbarianButton, ClickResetLevelButton
from classes.Commands import ClickSetLevelButton, ClickAttackButton, ClickNewTroopButton, ClickMarchButton
from classes.Commands import IsVerifyOn, IsMarchButtonVisible, IsTroopWalks, IsTroopFights, IsTroopReturns, GoHome
from classes.Commands import ClickOnHealButton, ClickOnHealMenuButton, AskHelp, HelpOthers, ClickToHospital


class AttackBarbarians:
    def __init__(self, level):
        self.level = level

    def start(self):
        is_verify_on = IsVerifyOn()
        check_antibot = CheckAntibot()
        check_action_points = CheckActionPoint()
        go_outside = GoOutside()
        search_target = ClickSearchTargetButton()
        select_target = ClickBarbarianButton()
        reset_level = ClickResetLevelButton()
        set_level = ClickSetLevelButton()
        new_level = set_level.set_level(self.level)
        search_button = ClickSearchButton()
        attack_button = ClickAttackButton()
        # if march button is visible cancel attack, otherwise continue.
        is_march_button_visible = IsMarchButtonVisible()
        new_troops = ClickNewTroopButton()
        march_to_enemy = ClickMarchButton()
        # After this step check hospital
        # Now while troop not returning do nothing
        is_troops_walks = IsTroopWalks()
        is_troops_fights = IsTroopFights()
        # while troop returning do nothing, when then reach home, start another attack.
        is_troops_returns = IsTroopReturns()
        # in this section you will heal all your troops
        go_home = GoHome()
        click_hospital = ClickToHospital()
        click_red_cross = ClickOnHealMenuButton()
        click_heal_button = ClickOnHealButton()
        ask_help = AskHelp()
        help_others = HelpOthers()
        get_out = GoOutside()

        # Chain starts here.
        is_verify_on.set_successor(check_antibot)
        check_antibot.set_successor(check_action_points)
        check_action_points.set_successor(go_outside)
        go_outside.set_successor(search_target)
        search_target.set_successor(select_target)
        select_target.set_successor(reset_level)
        reset_level.set_successor(set_level)
        set_level.set_successor(search_button)
        search_button.set_successor(attack_button)
        attack_button.set_successor(is_march_button_visible)
        is_march_button_visible.set_successor(attack_button)
        attack_button.set_successor(new_troops)
        new_troops.set_successor(march_to_enemy)
        march_to_enemy.set_successor(is_troops_walks)
        is_troops_walks.set_successor(is_troops_fights)
        is_troops_fights.set_successor(is_troops_returns)
        # Healing chain starts here
        is_troops_returns.set_successor(go_home)
        go_home.set_successor(click_hospital)
        click_hospital.set_successor(click_red_cross)
        click_red_cross.set_successor(click_heal_button)
        click_heal_button.set_successor(ask_help)
        ask_help.set_successor(help_others)
        help_others.set_successor(get_out)
        is_verify_on.do_work()

