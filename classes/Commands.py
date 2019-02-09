from classes import AbstractMethods
from classes.ImageCoordinate import ImageCoordinate
from classes.Clicker import Clicker as clicker
from classes.Speak import Speak
import pyautogui
import sys
import winsound
from time import sleep


class MousePosition:
    @staticmethod
    def position():
        print(pyautogui.position())


class RemoveOldCaveMessage(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/cave_old'):
            coord = ImageCoordinate.coords('images/delete_button')
            clicker.click(coord)
        self.next()


class RemoveWarReport(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/war_report'):
            coord = ImageCoordinate.coords('images/delete_button')
            clicker.click(coord)
        self.next()


class ClaimPrize(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/claim_gift'):
            coord = ImageCoordinate.coords('images/claim_gift')
            clicker.click(coord)
        self.next()


class ClickOnNida(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/nida_image'):
            coord = ImageCoordinate.coords('images/nida_image')
            clicker.click(coord)
        self.next()


class OpenMail(AbstractMethods.ProcessHandler):
    def do_work(self):
        while not ImageCoordinate.is_on_screen('images/mail_button'):
            coord = ImageCoordinate.coords('images/close_window')
            clicker.click(coord)
        else:
            coord = ImageCoordinate.coords('images/mail_button')
            clicker.move_click(coord)
        self.next()


class ClickReport(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/report_selected'):
            pass
        else:
            coord = ImageCoordinate.coords('images/report_button')
            clicker.move_click(coord)
        self.next()


class DeleteGatheringReport(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/gathering_report'):
            coord = ImageCoordinate.coords('images/gathering_report')
            clicker.move_click(coord)
            coord = ImageCoordinate.coords('images/delete_button')
            clicker.move_click(coord)
        self.next()


class SelectExploreMail(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.coords('images/explore_mail'):
            coord = ImageCoordinate.coords('images/explore_mail')
            clicker.move_click(coord)
        else:
            pass
        self.next()


class ClickTelescope(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(2)
        coord = ImageCoordinate.coords('images/teleskop_button')
        clicker.move_click(coord)
        self.next()


class ClickPresentIcon(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(1)
        if ImageCoordinate.is_on_screen('images/present_icon'):
            coord = ImageCoordinate.coords('images/present_icon')
            clicker.move_click(coord)
            sleep(1)
            clicker.click(coord)
        self.next()


class ClickInvestigation(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/investigate_button'):
            coord = ImageCoordinate.coords('images/investigate_button')
            clicker.click(coord)
        self.next()


class MoveToScoutCampAndClick(AbstractMethods.ProcessHandler):
    def do_work(self):
        print('Moving over scout camp and clicking on it to open scout menu')
        clicker.move(368*2, -127*2)
        clicker.click(clicker.mouse_pos())
        self.next()


class ClickDurbin(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(2)
        print('Clicking on monocular image to open scout management window')
        coord = ImageCoordinate.coords('images/durbin_butonu')
        clicker.click(coord)
        self.next()


class IsExploreButtonExists(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(2)
        if ImageCoordinate.is_on_screen('images/explore_button'):
            return True
        else:
            return False


class SearchExploreButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(2)
        print('Searching for explore button in scout management window')
        while not ImageCoordinate.is_on_screen('images/explore_button'):
            print('No scouts are available, Waiting 20 seconds')
            Speak().speak('No scouts are available, waiting for 20 seconds')
            sleep(20)
            Speak().speak('Waited for 20 seconds')
            print('Waited 10 seconds...')
        else:
            print('Continue exploration...')
            Speak().speak('Continue exploration!')
        self.next()


class SendScoutButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(2)
        if ImageCoordinate.is_on_screen('images/send_scout_button'):
            print('Sending scout to explore the kingdom')
            coord = ImageCoordinate.coords('images/send_scout_button')
            clicker.move_click(coord)
        self.next()


class ClickExploreButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(2)
        print('Clicking on explore button 1')
        coord = ImageCoordinate.coords('images/explore_button')
        clicker.click(coord)
        self.next()


class ClickExploreButton2(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(2)
        print('Clicking on explore button 2')
        coord = ImageCoordinate.coords('images/explore_button')
        clicker.click(coord)
        self.next()


class GoHome(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/isHome'):
            print('You are at home')
            coord = ImageCoordinate.coords('images/isHome')
            clicker.move_to(coord)
        else:
            coord = ImageCoordinate.coords('images/isOutside')
            clicker.move_click(coord)
            print('Going to home. Now, you are at home.')
        self.next()


class GoOutside(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/isOutside'):
            print('You are at outside')
        else:
            coord = ImageCoordinate.coords('images/isHome')
            clicker.move_click(coord)
            print('Going outside. Now, you are at outside')
        self.next()


class ClickSearchTargetButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        print('Clicking on to search for target')
        coord = ImageCoordinate.coords('images/btnSearch')
        clicker.move_click(coords=coord)
        self.next()


class ClickBarbarianButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        print('Clicking on barbarian')
        coord = ImageCoordinate.coords('images/btnBarb')
        clicker.move_click(coords=coord)
        self.next()


class ClickResetLevelButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        print('Resetting level to 1')
        coord = ImageCoordinate.coords('images/search_minus_button')
        clicker.move_click(coord, clicks=25, interval=0.15)
        self.next()


class ClickSetLevelButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        print('Resetting level to ' + str(self.get_level()))
        coord = ImageCoordinate.coords('images/search_plus_button')
        clicker.move_click(coord, clicks=self.get_level()-1, interval=0.15)
        self.next()


class ClickSearchButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        print('Clicking search button to search for the target')
        coord = ImageCoordinate.coords('images/search')
        clicker.move_click(coord)
        clicker.move(368, -127)
        clicker.click(clicker.mouse_pos())
        self.next()


class ClickAttackButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        print('Clicking on attack button')
        coord = ImageCoordinate.coords('images/btnAttack')
        clicker.move_click(coord)
        self.next()


class ClickNewTroopButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        print('Clicking on New Troops button')
        coord = ImageCoordinate.coords('images/newTroops')
        clicker.move_click(coord)
        self.next()


class ClickMarchButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        print('Clicking on March button')
        coord = ImageCoordinate.coords('images/btnMarch')
        clicker.move_click(coord)
        self.next()


class CheckActionPoint(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/end_of_ap'):
            sys.exit('Action Points are finished')
        else:
            print('Action Points are sufficient')
        self.next()


class CheckAntibot(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/is_antibot_active'):
            winsound.Beep(2500, 1500)
            print('Antibot! Antibot! Antibot!')
        else:
            print('Bot test is not active, continue playing game.')
        self.next()


class IsHardBattle(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/is_it_hard_battle'):
            sys.exit('It is a hard battle, stay away from the enemy. Stopping attack!')
        self.next()



