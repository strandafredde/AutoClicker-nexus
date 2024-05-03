import pyautogui as pt
from time import sleep

class Clicker:
    def __init__(self, target_image, speed):
        self.target_image = target_image
        self.speed = speed
        pt.FAILSAFE = True
        self.move_x = 15
        self.move_y = 75
    def nav_to_image(self):
        try:
            position = pt.locateOnScreen(self.target_image, confidence=.8)
            pt.moveTo(position[0] + self.move_x, position[1] + self.move_y, duration=self.speed)
            pt.click()

        except Exception as e:
            print(f"Could not find target image: {e}")
            return 0
    
if __name__ == "__main__":
    sleep(2)
    clicker = Clicker("Images\slow-download.png", 0.01)
    end = 0

    while True:
       if clicker.nav_to_image() == 0:
           end += 1

           if end > 100:
               break
