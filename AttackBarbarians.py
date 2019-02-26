from classes.Commands import CheckAntibot, CheckActionPoint, GoOutside, ClickSearchButton, IsTroopReturns
from classes.Commands import ClickSearchTargetButton, ClickBarbarianButton, ClickResetLevelButton
from classes.Commands import ClickSetLevelButton, ClickAttackButton, ClickNewTroopButton, ClickMarchButton
from classes.Commands import IsVerifyOn, IsMarchButtonVisible, IsTroopFights


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
        is_troops_fight = IsTroopFights()
        # while troop returning do nothing, when then reach home, start another attack.
        is_troops_return = IsTroopReturns()



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
        march_to_enemy.set_successor(is_troops_fight)
        is_troops_fight.set_successor(is_troops_return)
        is_verify_on.do_work()