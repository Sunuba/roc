**How to start exe file?**

executable program is in /dist folder simply click Graphical.exe
then you can see barb_allday. this one catches barbarian all day. 

**TODO**

1. need to update 
[BreakGeetest](classes/breakgeetest.py)

Geetest has been updated and need to break this one. 

    1. crop modification
        -on progress, but still need to capture exact position
        
    2. template matching
        -it's hard only using grayscale template matching, cause geetest block contour matching by modifying colour



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
