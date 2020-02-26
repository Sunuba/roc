from tkinter import *
from classes.AttackBarbarians import AttackBarbarians
from classes.ExploreFog import ExploreFog
from classes.Screenshot import Screenshot
from classes.tester import Tester

starter = Tk()
starter.winfo_toplevel().title('Rise of Kingdom - Automator')
starter.geometry('250x500')


class MainInterface:
    v=StringVar()
    v.set('BlueStacks')
    i=IntVar()
    i.set(26)
    q=IntVar()
    q.set(35)
    x=IntVar()
    x.set(4)
    txt_process_name = Entry(starter,text=v)
    txt_minbarb_level = Entry(starter,text=i)
    txt_maxbarb_level = Entry(starter,text=q)
    txt_troop_count = Entry(starter,text=x)

    def __init__(self, barb_level, function):
        self.barb_level = barb_level
        self.function = function
        

    def barb_allday(self):
        process_name = self.txt_process_name.get()
        minbarb_level = self.txt_minbarb_level.get()
        maxbarb_level = self.txt_maxbarb_level.get()

        troop_count = self.txt_troop_count.get()
        while True:
            attack = AttackBarbarians(minbarb_level,maxbarb_level,troop_count,process_name)
            attack.start()
    def test_start(self):
        Tester.start()

    def start_explore(self):
        ExploreFog.start()

    def take_screenshot(self):
        Screenshot.shot('default.png')

    def start_interface(self):
        lbl_process_name = Label(starter, text="Enter process name")

        lbl_minbarb_attack = Label(starter, text="Enter barbarian minlevel")
        lbl_maxbarb_attack = Label(starter, text="Enter barbarian maxlevel")

        lbl_barb_troop = Label(starter, text="Enter troop number and press button")

        #btn_barb_attack = Button(starter, text="Attack Barbarian", command=(lambda: self.start_attack()))
        #btn_explore = Button(starter, text="Explore Kingdom", command=(lambda: self.start_explore()))

        #btn_test = Button(starter, text="test method", command=(lambda: self.test_start()))

        btn_take_screenshot = Button(starter, text="Screenshot", command=(lambda: self.take_screenshot()))
        #lbl_barb_allday = Label(starter, text="barb_allday")
        btn_barb_allday = Button(starter, text="barb_allday", command=(lambda: self.barb_allday()))
        
        lbl_process_name.pack()
        self.txt_process_name.pack()
        lbl_minbarb_attack.pack()
        self.txt_minbarb_level.pack()
        lbl_maxbarb_attack.pack()
        self.txt_maxbarb_level.pack()
        lbl_barb_troop.pack()
        self.txt_troop_count.pack()

        #btn_barb_attack.pack()
        #btn_explore.pack()
        #btn_test.pack()
        btn_take_screenshot.pack()
#        lbl_barb_allday.pack()
        btn_barb_allday.pack()

 

        starter.mainloop()


interface = MainInterface(barb_level=12, function='start_attack()')
interface.start_interface()



