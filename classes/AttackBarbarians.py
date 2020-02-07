from classes.Commands import CheckAntibot, CheckActionPoint, GoOutside, ClickSearchButton
from classes.Commands import ClickSearchTargetButton, ClickBarbarianButton, ClickResetLevelButton
from classes.Commands import ClickSetLevelButton, ClickAttackButton, ClickNewTroopButton, ClickMarchButton
from classes.Commands import IsVerifyOn, IsMarchButtonVisible, IsTroopWalks, IsTroopFights, IsTroopReturns, GoHome
from classes.Commands import ClickOnHealButton, ClickOnHealMenuButton, AskHelp, HelpOthers, ClickToHospital


class AttackBarbarians:
    def __init__(self, level,troopcount):
        self.level = level
        self.troopcount = troopcount

    def start(self):
        is_verify_on = IsVerifyOn()
        check_antibot = CheckAntibot()
        check_action_points = CheckActionPoint()
        go_outside = GoOutside()

        reset_level = ClickResetLevelButton()
        set_level = ClickSetLevelButton()
        new_level = set_level.set_level(self.level)
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
   #     mail = OpenMail()

        search_target = []
        select_target = []
        search_button = []
        attack_button = []
        is_march_button_visible = []
        new_troops = []
        march_to_enemy = []
        for num in range(int(self.troopcount)):
            search_target.append(ClickSearchTargetButton())
            select_target.append(ClickBarbarianButton())
            search_button.append(ClickSearchButton())
            attack_button.append(ClickAttackButton())
            is_march_button_visible.append(IsMarchButtonVisible())
            new_troops.append(ClickNewTroopButton())
            march_to_enemy.append(ClickMarchButton())

        # Chain starts here.
        is_verify_on.set_successor(check_antibot)
        check_antibot.set_successor(check_action_points)
        check_action_points.set_successor(go_outside)
        go_outside.set_successor(search_target[0])
        
        search_target[0].set_successor(select_target[0])
        select_target[0].set_successor(reset_level)
        reset_level.set_successor(set_level)
        set_level.set_successor(search_button[0])
        search_button[0].set_successor(attack_button[0])
        attack_button[0].set_successor(is_march_button_visible[0])
        is_march_button_visible[0].set_successor(attack_button[0])
        attack_button[0].set_successor(new_troops[0])
        new_troops[0].set_successor(march_to_enemy[0])
        #for num in range(int(self.troopcount)-1):
         #   print(num)
        for num in range(int(self.troopcount)-1):
            march_to_enemy[num].set_successor(search_target[num+1])
            search_target[num+1].set_successor(search_button[num+1])
            search_button[num+1].set_successor(attack_button[num+1])
            attack_button[num+1].set_successor(is_march_button_visible[num+1])
            is_march_button_visible[num+1].set_successor(attack_button[num+1])
            attack_button[num+1].set_successor(new_troops[num+1])
            new_troops[num+1].set_successor(march_to_enemy[num+1])

        march_to_enemy[int(self.troopcount)-1].set_successor(is_troops_walks)
        
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
        #get_out.set_successor(mail)
        is_verify_on.do_work()

