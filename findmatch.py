import time

import pyautogui

from LOLPixelBot.autoaccept import AutoAccept
from LOLPixelBot.imagesearch import imagesearch_loop, imagesearch, region_grabber, imagesearcharea


def FindMatch():
    play = imagesearch_loop(R"images\play.png", 0.5)
    pyautogui.moveTo(play, duration=2)
    pyautogui.click(play)

    coop = imagesearch_loop(R"images\co-op.png", 0.5)
    pyautogui.moveTo(coop, duration=2)
    pyautogui.click(coop)

    intermediate = imagesearch_loop(R"images\intermediate.png", 0.5)
    pyautogui.moveTo(intermediate, duration=2)
    pyautogui.click(intermediate)

    confirm = imagesearch_loop(R"images\confirm.png", 0.5)
    pyautogui.moveTo(confirm, duration=2)
    pyautogui.click(confirm)

    findmatch = imagesearch_loop(R"images\findmatch.png", 0.5)
    pyautogui.moveTo(findmatch, duration=2)
    pyautogui.click(findmatch)

    AutoAccept()
    time.sleep(15)


def ChampionSelect():
    im = region_grabber((0, 0, 1280, 720))

    for i in range(10):
        searchbar = imagesearcharea(R"images\search.png", 0, 0, 1280, 720, 0.8, im)
    if searchbar[0] != -1:
        print("In champion select")
        pyautogui.moveTo(searchbar, duration=1)
        pyautogui.click(searchbar)
        pyautogui.typewrite("soraka")

        time.sleep(2)
        for i in range(10):
            soraka = imagesearch(R"images\soraka.png")
        if soraka[0] != -1:
            print("soraka found")
            pyautogui.click(soraka)
            confirm = imagesearch_loop(R"images\lockin.png", 0.5)
            pyautogui.click(confirm)
            print("soraka locked")
    else:
        FindMatch()
