from tkinter import *
from AttackBarbarians import AttackBarbarians
from ExploreFog import ExploreFog
from classes.Screenshot import Screenshot


starter = Tk()
starter.winfo_toplevel().title('Rise of Civilization - Automator')
starter.geometry('250x500')


class MainInterface:

    txt_barb_level = Entry(starter)

    def __init__(self, barb_level, function):
        self.barb_level = barb_level
        self.function = function

    def start_attack(self):
        barb_level = self.txt_barb_level.get()
        attack = AttackBarbarians(barb_level)
        attack.start()

    def start_explore(self):
        ExploreFog.start()

    def take_screenshot(self):
        Screenshot.shot('default.png')

    def start_interface(self):
        lbl_barb_attack = Label(starter, text="Enter barbarian level and press button")
        btn_barb_attack = Button(starter, text="Attack Barbarian", command=(lambda: self.start_attack()))
        lbl_explore = Label(starter, text="Explore Kingdom")
        btn_explore = Button(starter, text="Explore Kingdom", command=(lambda: self.start_explore()))
        lbl_take_screenshot = Label(starter, text="Take Screenshot")
        btn_take_screenshot = Button(starter, text="Screenshot", command=(lambda: self.take_screenshot()))
        lbl_barb_attack.pack()
        self.txt_barb_level.pack()
        btn_barb_attack.pack()
        lbl_explore.pack()
        btn_explore.pack()
        lbl_take_screenshot.pack()
        btn_take_screenshot.pack()

        starter.mainloop()


interface = MainInterface(barb_level=12, function='start_attack()')
interface.start_interface()



