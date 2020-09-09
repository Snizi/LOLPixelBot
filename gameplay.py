import time

import keyboard
import pyautogui
import win32gui
from pynput.mouse import Button, Controller

from LOLPixelBot.directkeys import P, A, PressKeyPynput, ReleaseKeyPynput, N1, N2, N3, N4
from LOLPixelBot.imagesearch import imagesearch_loop

mouse = Controller()



def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        pass
    if 'League of Legends (TM) Client' in win32gui.GetWindowText(hwnd):
        win32gui.MoveWindow(hwnd, 0, 0, 1024, 768, True)


# Point(x=55, y=171) initial item
# Point(x=104, y=174) pot
# Point(x=815, y=502) player 1 to heal
# Point(x=871, y=503) player 2 to heal
# Point(x=930, y=504) player 3 to heal
# Point(x=985, y=503) player 4 to heal
# (x=457, y=748) recall time
# 1:30 minions começam a se hitar no mid
# A partir de 1:05 a cada 30 segundos uma wave sai do nexus
#midlane T1 coords = (x=879, y=661)


def BuyItems():
    # creating buyInitialItems function
    def BuyInitialItems():
        time.sleep(2)
        pyautogui.moveTo(initialItem)
        mouse.click(Button.right)
        time.sleep(2)

        pyautogui.moveTo(healthPot)
        time.sleep(2)
        mouse.click(Button.right)
        time.sleep(2)

    initialItem = (55, 171)
    healthPot = (104, 174)
    firstSlotX, firstSlotY = 601, 718
    emptySlotRGB = (5, 13, 11)


    keyboard.press_and_release(P)

    while pyautogui.pixelMatchesColor(firstSlotX, firstSlotY, (emptySlotRGB)):
        BuyInitialItems()

    keyboard.press_and_release(P)


def AlternatePlayer(player):
    keyboard.press_and_release(player)

    mouse.position = (378, 513)
    mouse.press(Button.right)
    mouse.release(Button.right)

    time.sleep(0.5)
    PressKeyPynput(A)
    ReleaseKeyPynput(A)


def PlayAsSoraka():
    alternate_player = 1200

    while True:

        alternate_player -= 1

        time.sleep(1)

        if alternate_player <= 1200 and alternate_player >= 1080:
            AlternatePlayer(N1)
            if pyautogui.pixelMatchesColor(838, 505, (19, 19, 19)):
                pyautogui.moveTo(838, 505)
                time.sleep(0.5)

                keyboard.press_and_release('k')  # level up the W
                keyboard.press_and_release('w')  # cast the W

        if alternate_player <= 1080 and alternate_player >= 960:
            AlternatePlayer(N2)
            if pyautogui.pixelMatchesColor(888, 505, (19, 19, 19)):
                pyautogui.moveTo(888, 505)
                time.sleep(0.5)

                keyboard.press_and_release('k')  # level up the W
                keyboard.press_and_release('w')  # cast the W

        if alternate_player <= 960 and alternate_player >= 720:
            AlternatePlayer(N3)
            if pyautogui.pixelMatchesColor(947, 505, (19, 19, 19)):
                pyautogui.moveTo(947, 505)
                time.sleep(0.5)

                keyboard.press_and_release('k')  # level up the W
                keyboard.press_and_release('w')  # cast the W

        if alternate_player <= 720 and alternate_player >= 0:
            AlternatePlayer(N4)
            if pyautogui.pixelMatchesColor(1006, 505, (19, 19, 19)):
                pyautogui.moveTo(1006, 505)
                time.sleep(0.5)

                keyboard.press_and_release('k')  # level up the W
                keyboard.press_and_release('w')  # cast the W


def PlayAsCarry():
    midSafezone = (899, 648)

    #enemy nexus coords x=985, y=558
    pyautogui.click(midSafezone, button='Right')
    keyboard.press_and_release(A)


            #PUSH WAVE
            #BACK TO THE TOWER
            #WAIT FOR THE NEXT WAVE
            # REPEAT


def Gameplay():
    t1Coords = (879, 661)
    minionWave = 30

    imagesearch_loop(R"images\corner.png", 0.2)
    win32gui.EnumWindows(enumHandler, None)

    # BuyItems()

    # pyautogui.click(t1Coords, button='Right')

    while True:
        time.sleep(1)
        minionWave -= 1
        print(minionWave)
        if minionWave == 0 :
            PlayAsCarry()
            minionWave = 30



time.sleep(3)
win32gui.EnumWindows(enumHandler, None)
print(pyautogui.position())