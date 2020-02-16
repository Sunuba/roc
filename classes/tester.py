from classes.Commands import *


class Tester:
    def __init__(self, level,troopcount):
        self.level = level
        self.troopcount = troopcount

    def start():
        is_verify_on = IsVerifyOn()
        check_antibot = CheckAntibot()
        check_action_points = CheckActionPoint()
        go_outside = GoOutside()

        reset_level = ClickResetLevelButton()
        set_level = ClickSetLevelButton()
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
        click_confirm = SimpleClick('confirm')
        ask_help = AskHelp()
        help_others = HelpOthers()
        get_out = GoOutside()
        openmail = OpenMail()
        opensystemmail = OpensystemMail()
        receivemail = SimpleClick('receive')
        closemail = SimpleClick('close_window')

        # Chain starts here.
        is_verify_on.set_successor(check_antibot)
        check_antibot.set_successor(check_action_points)
        check_action_points.set_successor(go_outside)
        go_outside.set_successor(openmail)
        openmail.set_successor(opensystemmail)
        opensystemmail.set_successor(receivemail)
        receivemail.set_successor(click_confirm)
        click_confirm.set_successor(closemail)
        is_verify_on.do_work()

