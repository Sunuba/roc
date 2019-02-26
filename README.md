I tried to automate some of the actions in Rise of Civilization.

    Features:
    - Attack


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

    It helps you graphicalls start attack on barbarians, explore kingdom automatically
    and take a screenshot