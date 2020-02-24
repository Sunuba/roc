**How to start exe file?**

executable program is in /dist folder simply click Graphical.exe
then you can see barb_allday. this one catches barbarian all day.
It's process based so you should keep emulator on foreground.

*please change process name(emulator name) after executing program*

**TODO**

1. need to update 
[BreakGeetest](classes/breakgeetest.py)

Geetest has been updated and need to break this one. 

    1. crop modification
        -on progress, but still need to capture exact position
        
    2. template matching
        -it's hard only using grayscale template matching, cause geetest block contour matching by modifying colour


I tried to automate some of the actions in Rise of Civilization.

    Features:
    - Attack and Heal Troops
    - Explore Fog
    - Read mails, delete unnecessary mails, collect presents, explore caves.


**TODO:**

    1. Gather resources
    2. Improve mail reading. When reading mail, send only one scout to one cave.
    

**REQUIREMENTS**

    pyttsx3 - for speaking
    pyautogui - for all other actions


**INSTRUCTIONS** 
   
    1. I have checked the scripts on Nox Player and Bluestacks. It works perfectly on both.
    My emulator window size is 1280x720. You can easily set this parameter from settings of
    your choice of emulator.
    
    2. Your City Hall layout should be in this way:
![alt text](https://github.com/smallfish06/roc/blob/master/images/KakaoTalk_20200215_153042355.jpg "City Hall Layout")
    
    3. Actually, Alliance Center, Scout Camp and Hospital locations are important in the layout.
     The rest you can put wherever you want.
     4. You must create your own images so that script will recognize the, and click them as required
     For example, for attack ask_help_button, bot_test, btnSearch, help_others, isHome, isOutSide,
     red_cross_hospital, returning, search_plus_button, verify_button is required. If you do not
     screenshot and extract those images, the script probably will not work, as my computer and
     your comuter screen size (resolution) could be different. Please consider all these issues.
     5. In some cases you need to adjust clicker coordinates as well. After attack finishes the script
     will go and click hospital to heal troops. This action is implemented by the following class:
     class ClickToHospital(AbstractMethods.ProcessHandler):
        def do_work(self):
            clicker.move(368 * 2+150, -127 * 2-100)
            # sys.exit('Adjust hospital')
            clicker.click(clicker.mouse_pos())
            clicker.repeat_click(3)
            print('Clicked on hospital')
            self.next()
        
        Here I have added 150 to x and subtracted 100 from y coordinates in order to land on the hospital.
        You may need to correct these numbers as well. To cut a long story short you need to have a little
        bit of programming skills in order to have it run smoothly.


**How to attack barbarians?**

    from AttackBarbarians import AttackBarbarians
    
    
    attack = AttackBarbarians(level=11) - set barbarian level here.
    while True:
        attack.start()
    
    
You may need to write your own loop to continuously attack barbarians.

**How to read mails?**
    
    
    
    
    while True:
        ReadMail.start()

**How to explore automatically?**

The code below will start exploration until you stop it.

    from ExploreFog import ExploreFog
    
    
    try:
        while True:
            ExploreFog.start()
    except:
        pass


**Graphical.py**

    It helps you graphically start attack on barbarians, explore kingdom automatically
    and take a screenshot
    

**Can you improve it?**
    
    Do it! let's make it better!
