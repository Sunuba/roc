I tried to automate some of the actions in Rise of Civilization.

    Features:
    - Attack


**REQUIREMENTS**

    pyttsx3 - for speaking
    pyautogui - for all other actions
    
    I have checked the scripts on Nox Player and Bluestacks. It works perfectly on both.
    My emulator window size is 1280x720. You can easily set this parameter from settings of
    your choice of emulator.


**TODO:**

    1. During attack or after attack check hospital, click heal and request help
    2. Imrpove mail reading. When reading mail, send only one scout to one cave.

**How to attack barbarians?**

    attack = AttackBarbarians(level=11) - set barbarian level here.
    attack.start()
    
    # When you attack barbarians, it will wait till the end your troop returns to home.
    Then it will start new attack on barbarians.
    
You may need to write your own loop to continuously attack barbarians.
    

**How to explore automatically?**

The code below will start exploration until you stop it.

    from AttackBarbarians import AttackBarbarians
    from ExploreFog import ExploreFog
    from time import sleep
    
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