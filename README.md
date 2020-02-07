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
