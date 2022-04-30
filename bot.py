import pyautogui
from time import sleep
import json

rising_counter = 0
alien_counter = 0

rising_energy_cooldown = 50
rising_cooldown = False
rising_cooldown_counter = 0

with open('records/alienscounter.json', 'r') as openfile:
    alien_counter = json.load(openfile)

with open('records/risingcounter.json', 'r') as openfile:
    rising_counter = json.load(openfile)

counter = 0


print("\n\n\n---------------------------------------- Counters ----------------------------------------")
print("\nAlien Worlds Counter: " + str(alien_counter))
print("Rising Star Counter: " + str(rising_counter))
print("Tries Counter: " + str(counter))
print("\n------------------------------------------------------------------------------------------\n\n\n")



while True:
    try:
        sleep(1)


        """ Rising Star """
        if (rising_cooldown) :
            rising_cooldown_counter += 1
            if (rising_cooldown_counter > rising_energy_cooldown): rising_cooldown = False
    
        else:
            illegal = pyautogui.locateOnScreen('img/illegal.png', confidence=0.9)
            if illegal is not None:
                pyautogui.click(illegal[0] + 10, illegal[1] + 10)
                pyautogui.moveTo(100,100)

            
            illegal = pyautogui.locateOnScreen('img/illegal.png', confidence=0.9)
            illegalSelected = pyautogui.locateOnScreen('img/illegalSelected.png', confidence=0.9)
            start = pyautogui.locateOnScreen('img/start.png', confidence=0.9)
            if start is not None and illegalSelected is not None and illegal is None:
                pyautogui.click(start[0] + 10, start[1] + 10)
                pyautogui.moveTo(100,100)
                rising_counter += 1

            
            needs = pyautogui.locateOnScreen('img/needs.png', confidence=0.9)
            if needs is not None:
                rising_cooldown = True
                rising_cooldown_counter = 0
                pyautogui.click(needs[0] + 10, needs[1] + 10)
                pyautogui.press('f5')
                pyautogui.moveTo(100,100)

            
            startamission = pyautogui.locateOnScreen('img/startamission.png', confidence=0.9)
            if startamission is not None:
                pyautogui.click(startamission[0] + 10, startamission[1] + 10)
                pyautogui.moveTo(100,100)


            risinglogin = pyautogui.locateOnScreen('img/risinglogin.png', confidence=0.9)
            if risinglogin is not None:
                pyautogui.click(risinglogin[0] + 10, risinglogin[1] + 10)
                pyautogui.write("name")
                pyautogui.moveTo(100,100)


            loginaccept = pyautogui.locateOnScreen('img/loginaccept.png', confidence=0.9)
            if loginaccept is not None:
                pyautogui.click(loginaccept[0] + 10, loginaccept[1] + 10)
                pyautogui.moveTo(100,100)

        
        


        """ Alien Worlds """
        mine = pyautogui.locateOnScreen('img/mine.png', confidence=0.9)
        if mine is not None:
            pyautogui.click(mine[0] + 10, mine[1] + 10)
            pyautogui.moveTo(100,100)
            sleep(5)


        mine = pyautogui.locateOnScreen('img/mine.png', confidence=0.9)    
        claim = pyautogui.locateOnScreen('img/claim.png', confidence=0.9)
        if claim is not None and mine is None:
            pyautogui.click(claim[0] + 10, claim[1] + 10)
            pyautogui.moveTo(100,100)
            sleep(10)


        approve = pyautogui.locateOnScreen('img/approve.png', confidence=0.9)
        if approve is not None:
            pyautogui.click(approve[0] + 10, approve[1] + 10)
            pyautogui.moveTo(100,100)
            alien_counter += 1
            sleep(5)



        counter += 1
        print("\n\n\n---------------------------------------- Counters ----------------------------------------")
        print("\nAlien Worlds Counter: " + str(alien_counter))
        print("Rising Star Counter: " + str(rising_counter))
        print("Tries Counter: " + str(counter))
        print("\n------------------------------------------------------------------------------------------\n\n\n")

        with open("records/alienscounter.json", "w") as outfile:
            json_object = json.dumps(alien_counter, indent = 4)
            outfile.write(json_object)

        with open("records/risingcounter.json", "w") as outfile:
            json_object = json.dumps(rising_counter, indent = 4)
            outfile.write(json_object)

    except:
        pass