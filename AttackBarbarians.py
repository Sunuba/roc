from classes.Commands import CheckAntibot, CheckActionPoint, GoOutside, ClickSearchButton
from classes.Commands import ClickSearchTargetButton, ClickBarbarianButton, ClickResetLevelButton
from classes.Commands import ClickSetLevelButton, ClickAttackButton, ClickNewTroopButton, ClickMarchButton
from classes.Commands import ClickCloseButton, IsVerifyOn, IsMarchButtonVisible, ClickOnLocation


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

        is_verify_on.set_successor(check_antibot)
        check_antibot.set_successor(check_action_points)
        check_action_points.set_successor(go_outside)
        go_outside.set_successor(search_target)
        search_target.set_successor(select_target)
        select_target.set_successor(reset_level)
        reset_level.set_successor(set_level)
        set_level.set_successor(search_button)
        search_button.set_successor(attack_button)
        if is_march_button_visible:
            ClickOnLocation.click()
            pass
            print('Attack canceled, no queue available!')
        else:
            attack_button.set_successor(new_troops)
            new_troops.set_successor(march_to_enemy)
        is_verify_on.do_work()