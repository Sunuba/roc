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
from classes.breakgeetest import *

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


class SimpleClick(AbstractMethods.ProcessHandler):
    '''
    confirm,close_window,
    gathering_report,war_report,explore_mail,receive

    claim_gift,nida_image,apci,
    investigate_button, send_scout_button, explore_button, durbin_butonu

    attack_button,isOutside,teleskop_button,
    btnWood,btnFood,btnGold,btnStone
    '''
    path = ''

    def __init__(self, option):
        super().__init__()
        self.path = option
    def do_work(self):
        sleep(0.5)
        print('clicking '+self.path)

        coord = ImageCoordinate.is_on_screen('images/'+self.path)
        if coord:
            clicker.click(coord)
        self.next()

class GatherCityrss(AbstractMethods.ProcessHandler):
    def do_work(self):
        SimpleClick('btnFood').do_work()
        SimpleClick('btnWood').do_work()
        SimpleClick('btnGold').do_work()
        SimpleClick('btnStone').do_work()

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

class CountOccurrence(AbstractMethods.ProcessHandler):
    def do_work(self):
        ImageCoordinate.count_occurrence('images/callback_button')
        pass


class IsMarchButtonVisible(AbstractMethods.ProcessHandler):
    def do_work(self):
        while ImageCoordinate.is_on_screen('images/btnMarch') and ImageCoordinate.is_on_screen('images/unitqueue'):
            clicker.repeat_click(1)
            print('No queue available, quit attack.')
            print('waiting for some time...')
        else:
            pass
        self.next()


class IsTroopWalks(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(1)
        while ImageCoordinate.is_on_screen('images/walking') and ImageCoordinate.is_on_screen('images/unitqueue'):
            print('Troops are walking. Timestamp: ' + str(time.time()))
            sleep(0.5)
        else:
            pass
        self.next()


class IsTroopFights(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(1)
        while (ImageCoordinate.is_on_screen('images/fighting')) and ImageCoordinate.is_on_screen('images/unitqueue'):
            print('Troops are fighting now. Timestamp: ' + str(time.time()))
            sleep(0.5)
        else:
            pass
        self.next()


class IsTroopReturns(AbstractMethods.ProcessHandler):
    def do_work(self):
        sleep(1)
        while ImageCoordinate.is_on_screen('images/returning')  and ImageCoordinate.is_on_screen('images/unitqueue'):
            print('Troops are returning, let\'s wait them. Timestamp: ' +
                  str(time.time()))
            sleep(0.50)
        else:
            pass
        self.next()


class OpensystemMail(AbstractMethods.ProcessHandler):
    def do_work(self):

        coord = ImageCoordinate.coords('images/systemmail')
        
        if coord:
            clicker.move_click(coord)
        else:
            coord = ImageCoordinate.coords('images/systemmailblue')
            print('clicking system blue')
            if coord:
                pass
            else:
                coord = ImageCoordinate.coords('images/systemmail')
                if coord:
                    clicker.move_click(coord)

        self.next()


class OpenMail(AbstractMethods.ProcessHandler):
    def do_work(self):
        while not ImageCoordinate.is_on_screen('images/mail_button'):
            print('looking for mail')
            coord = ImageCoordinate.coords('images/close_window')
            clicker.click(coord)
        else:
            coord = ImageCoordinate.coords('images/mail_button')
            print('will click mail')
            if coord:
                clicker.move_click(coord)
                print('clicked mail')
        print('process done')
        self.next()


class ClickReport(AbstractMethods.ProcessHandler):
    def do_work(self):
        if ImageCoordinate.is_on_screen('images/report_selected'):
            pass
        else:
            coord = ImageCoordinate.coords('images/report_button')
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


class MoveToScoutCampAndClick(AbstractMethods.ProcessHandler):
    def do_work(self):
        print('Moving over scout camp and clicking on it to open scout menu')
        clicker.move(368*2-140, -127*2-140)
        clicker.click(clicker.mouse_pos())
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
        else:
            print('Continue exploration...')
            # Speak().speak('Continue exploration!')
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
        print('outing done')
        self.next()


class ClickSearchTargetButton(AbstractMethods.ProcessHandler):
    coord = False
    def __init__(self,force =0):
        super().__init__()
        self.force = force
    def do_work(self):
        if not self.force:
            coords = ImageCoordinate.is_on_screen('images/btnSearch')
            if coords:
                if not ImageCoordinate.is_on_screen('images/hammer'):
                    print('this is not hammer')
                else:
                    print('this is hammer')
                    GoOutside().do_work()
                clicker.move_click(coords)
                ClickSearchTargetButton.coord = coords
                print('Now, you are at clicked')
            else:
                sys.exit('btnSearch is not visible.')
        else:
            clicker.move_click(ClickSearchTargetButton.coord)

        self.next()


class ClickBarbarianButton(AbstractMethods.ProcessHandler):
    coord = False

    def do_work(self):
        if not ClickBarbarianButton.coord:
            ClickBarbarianButton.coord = ImageCoordinate.is_on_screen(
                'images/btnBarb')
        if ClickBarbarianButton.coord:
            clicker.move_click(ClickBarbarianButton.coord)
        else:
            pass
        self.next()


class ClickResetLevelButton(AbstractMethods.ProcessHandler):
    coord = False

    def do_work(self):
        if not ClickResetLevelButton.coord:
            ClickResetLevelButton.coord = ImageCoordinate.is_on_screen(
                'images/search_minus_button')
        if ClickResetLevelButton.coord:
            clicker.move_click(ClickResetLevelButton.coord,
                               clicks=25, interval=0.15)
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
            ClickSetLevelButton.coord = ImageCoordinate.is_on_screen(
                'images/search_plus_button')
        if ClickSetLevelButton.coord:
            clicker.move_click(ClickSetLevelButton.coord,
                               clicks=self.get_level()-1, interval=0.3)
        else:
            print('fail setlevel')
            sys.exit('search_plus_button not found. Time: ' + str(time.time()))
        self.next()


class ClickSearchButton(AbstractMethods.ProcessHandler):
    coord = False

    def do_work(self):
        if not ClickSearchButton.coord:
            ClickSearchButton.coord = ImageCoordinate.is_on_screen(
                'images/search')
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
class ClickGatherButton(AbstractMethods.ProcessHandler):
    coord = False

    def do_work(self):
        if not ClickGatherButton.coord:
            ClickGatherButton.coord = ImageCoordinate.is_on_screen(
                'images/gather_button')
        if ClickGatherButton.coord:
            clicker.move_click(ClickGatherButton.coord)
        self.next()


class ClickNewTroopButton(AbstractMethods.ProcessHandler):
    coord = False

    def do_work(self):
        if not ClickNewTroopButton.coord:
            ClickNewTroopButton.coord = ImageCoordinate.is_on_screen(
                'images/NewTroops')
        if ClickNewTroopButton.coord:
            clicker.move_click(ClickNewTroopButton.coord)
        else:
            ClickNewTroopButton.coord = ImageCoordinate.is_on_screen(
                'images/NewTroops')
            if ClickNewTroopButton.coord:
                clicker.move_click(ClickNewTroopButton.coord)
            else:
                clicker.click(clicker.mouse_pos())
        self.next()


class ClickNewTroopButtonForGathering(AbstractMethods.ProcessHandler):
    coord = False

    def do_work(self):
        if not ClickNewTroopButtonForGathering.coord:
            ClickNewTroopButtonForGathering.coord = ImageCoordinate.is_on_screen(
                'images/NewTroops')
        if ClickNewTroopButtonForGathering.coord:
            clicker.move_click(ClickNewTroopButtonForGathering.coord)
        else:
            ClickNewTroopButtonForGathering.coord = ImageCoordinate.is_on_screen(
                'images/NewTroops')
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


class ClickMarchButton(AbstractMethods.ProcessHandler):
    coord = False

    def do_work(self):
        pass_ap=False
        if not ClickMarchButton.coord:
            ClickMarchButton.coord = ImageCoordinate.is_on_screen(
                'images/btnMarch')
        if ClickMarchButton.coord:
            clicker.move_click(ClickMarchButton.coord)
        else:
            ClickMarchButton.coord = ImageCoordinate.is_on_screen(
                'images/btnMarch')
            if ClickMarchButton.coord:
                clicker.move_click(ClickMarchButton.coord)
                SimpleClick('close_window').do_work()
                pass_ap = True

        if CheckActionPoint() and not pass_ap:
             clicker.move_click(ClickMarchButton.coord)
        self.next()


def CheckActionPoint():
    #sleep(0.5)
    coord = ImageCoordinate.is_on_screen('images/useap')
    if coord:
        clicker.move_click(coord, clicks=6, interval=0.15)
        SimpleClick('close_window').do_work()

        return 1
    else:
        print('Action Points are sufficient')
        return 0


class CheckAntibot(AbstractMethods.ProcessHandler):
    accuracy = 0

    def __init__(self, accuracy=0.1):
        self.accuracy = accuracy
        super().__init__()

    def do_work(self):
        sleep(3)
        coord = ImageCoordinate.is_on_screen(
            'images/is_antibot_active', accuracy=self.accuracy)
        if coord:
            winsound.Beep(2500, 1500)
            print('Antibot! Antibot! Antibot!')
            clicker.click(coord)
            if ImageCoordinate.is_on_screen('images/verify_button'):
                print('Verify the bot test please')
                coord = ImageCoordinate.coords('images/verify_button')
                clicker.click(coord)
                sleep(5)
                usethis = ImageCoordinate.is_on_screen('images/usethis')
                confirmgee = ImageCoordinate.is_on_screen('images/confirmgee')
                print(usethis)
                print(confirmgee)
                solvegee(usethis, confirmgee)
            else:
                print('Verification is not required. Continue...')
        else:
            print('Bot test is not active, continue playing game.')

        self.next()


class ClickToHospital(AbstractMethods.ProcessHandler):
    def do_work(self):
        clicker.move(368 * 2+150, -127 * 2-100)
        clicker.click(clicker.mouse_pos())
        clicker.repeat_click(1)
        print('Clicked on hospital')
        self.next()


class ClickOnHealMenuButton(AbstractMethods.ProcessHandler):
    coord = False

    def do_work(self):
        if not ClickOnHealMenuButton.coord:
            ClickOnHealMenuButton.coord = ImageCoordinate.is_on_screen(
                'images/red_cross_hospital')
        if ClickOnHealMenuButton.coord:
            clicker.click(ClickOnHealMenuButton.coord)
        else:
            print('I do not see any red cross, it means that troops are ok for now.')
        self.next()


class ClickOnHealButton(AbstractMethods.ProcessHandler):
    coord = False

    def do_work(self):
        if not ClickOnHealButton.coord:
            ClickOnHealButton.coord = ImageCoordinate.is_on_screen(
                'images/heal_button')
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
            AskHelp.coord = ImageCoordinate.is_on_screen(
                'images/ask_help_button')
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
            HelpOthers.coord = ImageCoordinate.is_on_screen(
                'images/help_others')
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
