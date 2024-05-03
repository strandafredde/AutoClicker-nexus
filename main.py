import sys
import pyautogui as pt
import pygame
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
            position = pt.locateOnScreen(self.target_image, confidence=.9)
            pt.moveTo(position[0] + self.move_x, position[1] + self.move_y, duration=self.speed)
            pt.click()
            sleep(5)
        except pt.FailSafeException:
            print("FailSafe triggered, exiting program.")
            exit(0)
        except Exception as e:
            print(f"Could not find target image: {e}")
            return 0
    
if __name__ == "__main__":
    sleep(2)
    clicker = Clicker("Images\slow-download.png", 0.1)
    end = 0
    pygame.init()
    
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                print("E pressed: Exiting program.")
                pygame.quit()
                sys.quit()

        if clicker.nav_to_image() == 0:
            end += 1

            if end > 200:
                break
        else:
            end = 0