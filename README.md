I tried to automate some of the actions in Rise of Civilization.

    Features:
    - Attack




**How to attack barbarians?**

    attack = AttackBarbarians(level=11) - set barbarian level here.
    attack.start()
    
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
