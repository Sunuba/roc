I tried to automate some of the actions in Rise of Civilization.

    Features:
    - Attack and Heal Troops
    - Explore Fog
    - Read mails, delete unnecessary mails, collect presents, explore caves.


**TODO:**

    1. Gather
    2. Improve mail reading. When reading mail, send only one scout to one cave.
    

**REQUIREMENTS**

    pyttsx3 - for speaking
    pyautogui - for all other actions


**INSTRUCTIONS** 
   
    1. I have checked the scripts on Nox Player and Bluestacks. It works perfectly on both.
    My emulator window size is 1280x720. You can easily set this parameter from settings of
    your choice of emulator.
    
    2. Your City Hall layout should be in this way:
![alt text](https://github.com/Sunuba/roc/blob/master/images/layout.png "City Hall Layout")


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