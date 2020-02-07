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
import classes.breakgeetest


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
        time.sleep(1)
        pyautogui.keyUp('s')
        pyautogui.keyDown('s')
        time.sleep(1)
        pyautogui.keyUp('s')
        pyautogui.keyDown('s')
        time.sleep(1)
        pyautogui.keyUp('s')
        pyautogui.keyDown('s')
        time.sleep(1)
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
            coord = ImageCoordinate.coords('images/verify_button')
            clicker.click(coord)
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
            sleep(0.5)
        else:
            pass
        self.next()


class IsTroopFights(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(1)
        while (not ImageCoordinate.is_on_screen('images/returning')) and ImageCoordinate.is_on_screen('images/unitqueue'):
            print('Troops are fighting now. Timestamp: ' + str(time.time()))
            sleep(0.5)
        else:
            pass
        self.next()


class IsTroopReturns(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(1)
        while ImageCoordinate.is_on_screen('images/returning'):
            print('Troops are returning, let\'s wait them. Timestamp: ' +
                  str(time.time()))
            sleep(0.50)
        else:
            pass
        self.next()


class ClickCloseButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        coord = ImageCoordinate.is_on_screen('images/close_window')
        if coord:
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
        coord = ImageCoordinate.is_on_screen('images/claim_gift')
        if coord:
            clicker.click(coord)
        self.next()


class ClickOnNida(AbstractMethods.ProcessHandler):
    def do_work(self):

        coord = ImageCoordinate.is_on_screen('images/nida_image')
        if coord:
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
        coord = ImageCoordinate.is_on_screen('images/gathering_report')
        if coord:
            clicker.move_click(coord)
            coord = ImageCoordinate.coords('images/delete_button')
            clicker.move_click(coord)
        self.next()


class SelectExploreMail(AbstractMethods.ProcessHandler):
    def do_work(self):
        coord = ImageCoordinate.coords('images/explore_mail')
        if coord:
            clicker.move_click(coord)
        else:
            pass
        self.next()


class ClickTelescope(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(1)
        coord = ImageCoordinate.coords('images/teleskop_button')
        clicker.move_click(coord)
        self.next()


class ClickPresentIcon(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(1)
        coord = ImageCoordinate.is_on_screen('images/present_icon')
        if coord:
            clicker.move_click(coord)
            sleep(1)
            clicker.click(coord)
        self.next()


class ClickInvestigation(AbstractMethods.ProcessHandler):
    def do_work(self):
        coord = ImageCoordinate.is_on_screen('images/investigate_button')
        if coord:
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
        sleep(1)
        print('Clicking on monocular image to open scout management window')
        coord = ImageCoordinate.coords('images/durbin_butonu')
        clicker.click(coord)
        self.next()


class IsExploreButtonExists(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(1)
        if ImageCoordinate.is_on_screen('images/explore_button'):
            return True
        else:
            return False


class SearchExploreButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(1)
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
        sleep(1)
        coord = ImageCoordinate.is_on_screen('images/send_scout_button')
        if coord:
            clicker.move_click(coord)
        self.next()


class ClickExploreButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(1)
        print('Clicking on explore button 1')
        coord = ImageCoordinate.coords('images/explore_button')
        clicker.click(coord)
        self.next()


class ClickExploreButton2(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(1)
        print('Clicking on explore button 2')
        coord = ImageCoordinate.coords('images/explore_button')
        clicker.click(coord)
        self.next()


class GoHome(AbstractMethods.ProcessHandler):
    def do_work(self):
        coord = ImageCoordinate.coords('images/isOutside')
        if coord:
            clicker.move_click(coord)
            print('Going to home. Now, you are at home.')
        else:
            print(' you are at home.')
        self.next()


class GoOutside(AbstractMethods.ProcessHandler):
    def do_work(self):
        coord = ImageCoordinate.is_on_screen('images/isOutside')
        if coord:
            homecoord = ImageCoordinate.is_on_screen('images/isHome')
            if homecoord:
                print('You are at home')
                clicker.move_click(homecoord)
            else:
                print('you are outside')
        else:
            coord = ImageCoordinate.coords('images/isHome')
            if coord:
                print('im at home')
                clicker.move_click(coord)
                print('Now, you are at outside')
        self.next()


class ClickSearchTargetButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        coord = ImageCoordinate.is_on_screen('images/btnSearch')
        if coord:
            if not ImageCoordinate.is_on_screen('images/hammer'):
                print('this is not hammer')
            else:
                print('this is hammer')
                GoOutside().do_work()
            clicker.move_click(coord)
            print('Now, you are at clicked')
        else:
            sys.exit('btnSearch is not visible.')
        self.next()


class ClickBarbarianButton(AbstractMethods.ProcessHandler):
    coord = False
    def do_work(self):
        if not ClickBarbarianButton.coord:
            ClickBarbarianButton.coord = ImageCoordinate.is_on_screen('images/btnBarb')
        if ClickBarbarianButton.coord:
            clicker.move_click(ClickBarbarianButton.coord)
        else:
            pass
        self.next()


class ClickResetLevelButton(AbstractMethods.ProcessHandler): 
    coord = False
    def do_work(self):
        if not ClickResetLevelButton.coord:
            ClickResetLevelButton.coord = ImageCoordinate.is_on_screen('images/search_minus_button')
        if ClickResetLevelButton.coord:
            clicker.move_click(ClickResetLevelButton.coord, clicks=25, interval=0.15)
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
    coord = False
    def do_work(self):
        if not ClickSetLevelButton.coord:
            ClickSetLevelButton.coord = ImageCoordinate.is_on_screen('images/search_plus_button')
        if ClickSetLevelButton.coord:
            clicker.move_click(ClickSetLevelButton.coord, clicks=self.get_level()-1, interval=0.3)
        else:
            print('fail setlevel')
            sys.exit('search_plus_button not found. Time: ' + str(time.time()))
        self.next()


class ClickSearchButton(AbstractMethods.ProcessHandler):
    coord = False
    def do_work(self):
        if not ClickSearchButton.coord:
            ClickSearchButton.coord = ImageCoordinate.is_on_screen('images/search')
        if ClickSearchButton.coord:
            clicker.move_click(ClickSearchButton.coord)
            clicker.move(500, -160)
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
            sleep(1)
            DecreaseLevel().do_work()
            sleep(1)
            coord = ImageCoordinate.coords('images/search', shot=True)
            clicker.move_click(coord)
        else:
            clicker.move(0, -127)
            clicker.click(clicker.mouse_pos())
        self.next()


class ClickAttackButton(AbstractMethods.ProcessHandler):
    def do_work(self):
        coord = ImageCoordinate.is_on_screen('images/btnAttack')
        if coord:
            clicker.move_click(coord)
        else:
            print('fail')
            sys.exit('wrong number')
        self.next()


class ClickGatherButton(AbstractMethods.ProcessHandler):
    coord = False
    def do_work(self):
        if not ClickGatherButton.coord:
            ClickGatherButton.coord = ImageCoordinate.is_on_screen('images/gather_button')
        if ClickGatherButton.coord:
            clicker.move_click(ClickGatherButton.coord)
        self.next()


class ClickNewTroopButton(AbstractMethods.ProcessHandler):
    coord = False
    def do_work(self):
        if not ClickNewTroopButton.coord:
            ClickNewTroopButton.coord = ImageCoordinate.is_on_screen('images/NewTroops')
        if ClickNewTroopButton.coord:
            clicker.move_click(ClickNewTroopButton.coord)
        else:
            ClickNewTroopButton.coord = ImageCoordinate.is_on_screen('images/NewTroops')
            if ClickNewTroopButton.coord:
                clicker.move_click(ClickNewTroopButton.coord)
            else:
                clicker.click(clicker.mouse_pos())
        self.next()


class ClickNewTroopButtonForGathering(AbstractMethods.ProcessHandler):
    coord = False
    def do_work(self):
        if not ClickNewTroopButtonForGathering.coord:
            ClickNewTroopButtonForGathering.coord = ImageCoordinate.is_on_screen('images/NewTroops')
        if ClickNewTroopButtonForGathering.coord:
            clicker.move_click(ClickNewTroopButtonForGathering.coord)
        else:
            ClickNewTroopButtonForGathering.coord = ImageCoordinate.is_on_screen('images/NewTroops')
            if ClickNewTroopButtonForGathering.coord:
                clicker.move_click(ClickNewTroopButtonForGathering.coord)
            else:
                clicker.click(clicker.mouse_pos())
        self.next()


class IsQueueAvailable(AbstractMethods.ProcessHandler):
    def do_work(self):
        coord = ImageCoordinate.is_on_screen('images/new_troop_controller')
        if coord:
            pass
        else:
            sys.exit('No queue, please wait.')
        self.next()


class ClickMarch(AbstractMethods.ProcessHandler):
    coord = False
    def do_work(self):
        if not ClickMarch.coord:
            ClickMarch.coord = ImageCoordinate.is_on_screen('images/btnMarch')
        if ClickMarch.coord:
            clicker.move_click(ClickMarch.coord)
        else:
            ClickMarch.coord = ImageCoordinate.is_on_screen('images/btnMarch')
            if ClickMarch.coord:
                clicker.move_click(ClickMarch.coord)
        sleep(1)

        self.next()


class CheckHospital(AbstractMethods.ProcessHandler):
    def do_work(self):

        self.next()


class ClickMarchButton(AbstractMethods.ProcessHandler):
    coord = False
    def do_work(self):
        if not ClickMarchButton.coord:
            ClickMarchButton.coord = ImageCoordinate.is_on_screen('images/btnMarch')
        if ClickMarchButton.coord:
            clicker.move_click(ClickMarchButton.coord)
            clicker.click(coord)

        else:
            ClickMarchButton.coord = ImageCoordinate.is_on_screen('images/btnMarch')
            if ClickMarchButton.coord:
                clicker.move_click(ClickMarchButton.coord)
        self.next()


class CheckActionPoint(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/end_of_ap'):
            coord =  ImageCoordinate.is_on_screen('images/useap')
            clicker.move_click(coord, clicks=3, interval=0.15)
        else:
            print('Action Points are sufficient')
        self.next()


class CheckAntibot(AbstractMethods.ProcessHandler):
    def do_work(self):
        coord = ImageCoordinate.is_on_screen('images/is_antibot_active')
        if coord:
            winsound.Beep(2500, 1500)
            print('Antibot! Antibot! Antibot!')
            clicker.click(coord)
        else:
            print('Bot test is not active, continue playing game.')
        if ImageCoordinate.is_on_screen('images/verify_button'):
            print('Verify the bot test please')
            coord = ImageCoordinate.coords('images/verify_button')
            clicker.click(coord)
            usethis = ImageCoordinate.is_on_screen('images/usethis')
            confirmgee = ImageCoordinate.is_on_screen('images/confirmgee')

            solvegee(usethis,confirmgee)
        else:
            print('Verification is not required. Continue...')
        self.next()

            
class ClickToHospital(AbstractMethods.ProcessHandler):
    def do_work(self):
        clicker.move(368 * 2+150, -127 * 2-100)
        # sys.exit('Adjust hospital')
        clicker.click(clicker.mouse_pos())
        clicker.repeat_click(3)
        print('Clicked on hospital')
        self.next()


class ClickOnHealMenuButton(AbstractMethods.ProcessHandler):
    coord = False
    def do_work(self):
        if not ClickOnHealMenuButton.coord:
            ClickOnHealMenuButton.coord = ImageCoordinate.is_on_screen('images/red_cross_hospital')
        if ClickOnHealMenuButton.coord:
            clicker.click(ClickOnHealMenuButton.coord)
        else:
            print('I do not see any red cross, it means that troops are ok for now.')
        self.next()


class ClickOnHealButton(AbstractMethods.ProcessHandler):
    coord = False
    def do_work(self):
        if not ClickOnHealButton.coord:
            ClickOnHealButton.coord = ImageCoordinate.is_on_screen('images/heal_button')
        if ClickOnHealButton.coord:
            clicker.click(ClickOnHealButton.coord)
        else:
            print('Troops are healthy... No need to heal.')
            pass
        self.next()


class AskHelp(AbstractMethods.ProcessHandler):
    coord = False
    def do_work(self):
        sleep(1)
        if not AskHelp.coord:
            AskHelp.coord = ImageCoordinate.is_on_screen('images/ask_help_button')
        if AskHelp.coord:
            clicker.move_to(AskHelp.coord)
            clicker.repeat_click(5, -20, 40)
            print('Clicked on help request')
        else:
            print('Help is not required')
        self.next()


class HelpOthers(AbstractMethods.ProcessHandler):
    coord = False
    def do_work(self):
        if not HelpOthers.coord:
            HelpOthers.coord = ImageCoordinate.is_on_screen('images/help_others')
        if HelpOthers.coord:
            clicker.move_to(HelpOthers.coord)
            clicker.repeat_click(5, -20, 40)
            print('Helped alliance members')
        else:
            print('Alliance members do not need any help')
        self.next()


class DragScreen():
    @staticmethod
    def start(xOffset, yOffset, duration):
        pyautogui.dragRel(xOffset, yOffset, duration)
