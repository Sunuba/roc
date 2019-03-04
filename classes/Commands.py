from classes import AbstractMethods
from classes.ImageCoordinate import ImageCoordinate
from classes.Clicker import Clicker as clicker
from classes.Speak import Speak
import pyautogui
import sys
import winsound
from time import sleep
import datetime
import time


class ResetWhile():
    def __init__(self, seconds):
        self.seconds = seconds

    def start(self):
        saniye = self.seconds
        while saniye > 0:
            print('Waiting:' + str(saniye))
            sleep(1)
            saniye -= 1


class MousePosition:
    @staticmethod
    def position():
        print(pyautogui.position())


class ZoomOut(AbstractMethods.ProcessHandler):
    def do_work(self):
        pyautogui.keyDown('s')
        time.sleep(2)
        pyautogui.keyUp('s')
        pyautogui.keyDown('s')
        time.sleep(2)
        pyautogui.keyUp('s')
        pyautogui.keyDown('s')
        time.sleep(2)
        pyautogui.keyUp('s')
        pyautogui.keyDown('s')
        time.sleep(2)
        pyautogui.keyUp('s')
        print('Zoomed out.')
        self.next()


class DoYouSeeHome(AbstractMethods.ProcessHandler):
    def do_work(self):
        start_time = time.time()
        while ImageCoordinate.is_on_screen('images/present_house'):
            coord = ImageCoordinate.coords('images/present_house')
            clicker.move_click(coord)
            print('Moved mouse to present home.')
        else:
            print('I do not see any present home.')
        self.next()



class ClickToVillage(AbstractMethods.ProcessHandler):
    def do_work(self):
        start_time = time.time()
        while not ImageCoordinate.is_on_screen('images/present_icon'):
            # if time.time() - start_time > 10:
            #     print('Restarting...')
            #     break
            print('No present this time')
        else:
            coord = ImageCoordinate.coords('images/present_icon', shot=False)
            clicker.click(coord)
            clicker.repeat_click(3, interval=0.55)
            print('Received present')
        self.next()


class ClickWoodButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        coord = ImageCoordinate.coords('images/btnWood')
        clicker.click(coord)
        self.next()


class CountOccurrence(AbstractMethods.ProcessHandler):
    def do_work(self):
        ImageCoordinate.count_occurrence('images/callback_button')
        pass


class IsVerifyOn(AbstractMethods.ProcessHandler):
    def do_work(self):
        today = datetime.datetime.now()
        while ImageCoordinate.is_on_screen('images/verify_button'):
            sys.exit('You missed to solve antibot, so exiting game. Exit time: ' + today.strftime("%H:%M:%S"))
        else:
            print('Game is safe, no verify button.')
        self.next()


class ClickOnLocation:
    @staticmethod
    def click():
        clicker.repeat_click(3)


class IsMarchButtonVisible(AbstractMethods.ProcessHandler):
    def do_work(self):
        while ImageCoordinate.is_on_screen('images/btnMarch'):
            clicker.repeat_click(3)
            print('No queue available, quit attack.')
            print('waiting for some time...')
        else:
            pass
        self.next()


class IsTroopWalks(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(1)
        while ImageCoordinate.is_on_screen('images/walking'):
            print('Troops are walking. Timestamp: ' + str(time.time()))
            sleep(5)
        else:
            pass
        self.next()


class IsTroopFights(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(2)
        while not ImageCoordinate.is_on_screen('images/returning'):
            sleep(5)
            print('Troops are fighting now. Timestamp: ' + str(time.time()))
        else:
            pass
        self.next()


class IsTroopReturns(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(2)
        while ImageCoordinate.is_on_screen('images/returning'):
            sleep(5)
            print('Troops are returning, let\'s wait them. Timestamp: ' + str(time.time()))
        else:
            pass
        self.next()


class ClickCloseButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/close_window'):
            coord = ImageCoordinate.coords('images/close_window')
            clicker.move_click(coord)
        else:
            pass
        self.next()

class RemoveOldCaveMessage(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/cave_old'):
            coord = ImageCoordinate.coords('images/delete_button')
            clicker.click(coord)
        self.next()


class RemoveWarReport(AbstractMethods.ProcessHandler):
    def do_work(self):
        while ImageCoordinate.is_on_screen('images/war_report'):
            coord_for_war_report = ImageCoordinate.coords('images/war_report')
            clicker.click(coord_for_war_report)
            sleep(0.75)
            coord = ImageCoordinate.coords('images/delete_button')
            clicker.click(coord)
        self.next()


class RemoveActionPointRefund(AbstractMethods.ProcessHandler):
    def do_work(self):
        while ImageCoordinate.is_on_screen('images/apci'):
            coord_for_war_report = ImageCoordinate.coords('images/apci')
            clicker.click(coord_for_war_report)
            sleep(0.75)
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
        clicker.move(368*2-140, -127*2-140)
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
            # Speak().speak('No scouts are available, waiting for 20 seconds')
            sleep(5)
            # Speak().speak('Waited for 20 seconds')
            print('Waited 5 seconds...')
            CheckAntibot().do_work()
        else:
            print('Continue exploration...')
            # Speak().speak('Continue exploration!')
        self.next()


class SendScoutButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(2)
        if ImageCoordinate.is_on_screen('images/send_scout_button'):
            print('Sending scout to explore the kingdom')
            coord = ImageCoordinate.coords('images/send_scout_button', shot=False)
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
            coord = ImageCoordinate.coords('images/isHome', shot=False)
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
            print('Going outside.')
            coord = ImageCoordinate.coords('images/isHome')
            clicker.move_click(coord)
            print('Now, you are at outside')
        self.next()


class ClickSearchTargetButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/btnSearch'):
            print('Clicking on to search for target')
            coord = ImageCoordinate.coords('images/btnSearch', shot=False)
            clicker.move_click(coords=coord)
        else:
            sys.exit('btnSearch is not visible.')
        self.next()


class ClickBarbarianButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        print('Clicking on barbarian')
        if ImageCoordinate.is_on_screen('images/btnBarb'):
            coord = ImageCoordinate.coords('images/btnBarb', shot=False)
            clicker.move_click(coords=coord)
        else:
            pass
        self.next()


class ClickResetLevelButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/search_minus_button'):
            print('Resetting level to 1')
            coord = ImageCoordinate.coords('images/search_minus_button', shot=False)
            clicker.move_click(coord, clicks=25, interval=0.15)
        else:
            pass
        self.next()


class DecreaseLevel(AbstractMethods.ProcessHandler):
    def do_work(self):
        print('Decreasing level 1 point')
        coord = ImageCoordinate.coords('images/search_minus_button')
        clicker.click(coord, clicks=1, interval=0.15)
        self.next()


class ClickSetLevelButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/search_plus_button'):
            print('Setting level to ' + str(self.get_level()))
            coord = ImageCoordinate.coords('images/search_plus_button')
            clicker.move_click(coord, clicks=self.get_level()-1, interval=0.15)
        else:
            sys.exit('search_plus_button not found. Time: ' + str(time.time()))
        self.next()


class ClickSearchButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/search'):
            print('Clicking search button to search for the target')
            coord = ImageCoordinate.coords('images/search', shot=False)
            clicker.move_click(coord)
            clicker.move(368, -127)
            clicker.click(clicker.mouse_pos())
        else:
            pass
        self.next()


class ClickSearchWoodButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        print('Clicking search button to search for the target')
        coord = ImageCoordinate.coords('images/search')
        clicker.click(coord)
        while ImageCoordinate.is_on_screen('images/search'):
            sleep(2)
            DecreaseLevel().do_work()
            sleep(2)
            coord = ImageCoordinate.coords('images/search', shot=True)
            clicker.move_click(coord)
        else:
            clicker.move(0, -127)
            clicker.click(clicker.mouse_pos())
        self.next()


class ClickAttackButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/btnAttack'):
            print('Clicking on attack button')
            coord = ImageCoordinate.coords('images/btnAttack', shot=False)
            clicker.move_click(coord)
        else:
            pass
        self.next()


class ClickGatherButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        print('Clicking GATHER button')
        if ImageCoordinate.is_on_screen('images/gather_button'):
            coord = ImageCoordinate.coords('images/gather_button', shot=False)
            clicker.move_click(coord)
        self.next()


class ClickNewTroopButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/NewTroops'):
            print('Clicking on New Troops button')
            coord = ImageCoordinate.coords('images/newTroops', shot=False)
            print(coord)
            clicker.move_click(coord)
        else:
            clicker.click(clicker.mouse_pos())
        self.next()


class ClickNewTroopButtonForGathering(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/NewTroops'):
            print('Clicking on New Troops button')
            coord = ImageCoordinate.coords('images/newTroops', shot=False)
            print(coord)
            clicker.move_click(coord)
        else:
            sys.exit('No queue, please wait.')
        self.next()


class IsQueueAvailable(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/new_troop_controller'):
            pass
        else:
            sys.exit('No queue, please wait.')
        self.next()


class ClickMarch(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/btnMarch'):
            print('Going to gather that resource')
            coord = ImageCoordinate.coords('images/btnMarch')
            clicker.move_click(coord)
        else:
            pass
        self.next()


class CheckHospital(AbstractMethods.ProcessHandler):
    def do_work(self):

        self.next()


class ClickMarchButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/btnMarch'):
            print('Clicking on March button')
            coord = ImageCoordinate.coords('images/btnMarch', shot=False)
            clicker.move_click(coord)
        else:
            pass
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
        if ImageCoordinate.is_on_screen('images/verify_button'):
            winsound.Beep(2500, 1500)
            print('Verify the bot test please')
        else:
            print('Verification is not required. Continue...')
        self.next()


class ClickToHospital(AbstractMethods.ProcessHandler):
    def do_work(self):
        clicker.move(368 * 2, -127 * 2)
        clicker.click(clicker.mouse_pos())
        clicker.repeat_click(3)
        print('Clicked on hospital')
        self.next()


class ClickOnHealMenuButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/red_cross_hospital'):
            print('Clicking on red cross over the hospital')
            coord = ImageCoordinate.coords('images/red_cross_hospital')
            clicker.click(coord)
        else:
            print('I do not see any red cross, it means that troops are ok for now.')
        self.next()


class ClickOnHealButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/heal_button'):
            print('Clicking to heal button to heal troops.')
            coord = ImageCoordinate.coords('images/heal_button', shot=False)
            clicker.click(coord)
        else:
            print('Troops are healthy... No need to heal.')
            pass
        self.next()


class AskHelp(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(2)
        if ImageCoordinate.is_on_screen('images/ask_help_button'):
            coord = ImageCoordinate.coords('images/ask_help_button')
            clicker.move_to(coord)
            clicker.repeat_click(5, -20, 40)
            print('Clicked on help request')
        else:
            print('Help is not required')
        self.next()


class HelpOthers(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/help_others'):
            coord = ImageCoordinate.coords('images/help_others')
            clicker.move_to(coord)
            clicker.repeat_click(5, -20, 40)
            print('Helped alliance members')
        else:
            print('Alliance members do not need any help')
        self.next()


class DragScreen():
    @staticmethod
    def start(xOffset, yOffset, duration):
        pyautogui.dragRel(xOffset, yOffset, duration)