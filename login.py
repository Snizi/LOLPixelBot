import pyautogui
from LOLPixelBot.imagesearch import imagesearch_loop
import time
import win32gui
import os




def enumHandlerLauncherNew(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        pass
    if 'Riot Client' in win32gui.GetWindowText(hwnd):
        win32gui.MoveWindow(hwnd, 0, 0, 1280, 720, True)

def GetAccounts():
    list = []
    with open('accounts.txt', 'r') as (file):
        for line in file:
            list.append((line.split(':')[0], line.split(':')[1].replace('\n', '')))
        return list[0]


def Login():
    login = [GetAccounts()]

    os.startfile(R"C:\League of Legends\LeagueClient.exe")

    username = imagesearch_loop(R"images\username.png", 0.5)
    password = imagesearch_loop(R"images\password.png", 0.5)

    win32gui.EnumWindows(enumHandlerLauncherNew, None)  # Realocate the launcher window

    time.sleep(2)

    pyautogui.moveTo(username)
    pyautogui.click(username)
    pyautogui.write(login[0][0])

    pyautogui.moveTo(password)
    pyautogui.click(password)
    pyautogui.write(login[0][1])

    signin = imagesearch_loop(R"images\signin.png", 0.5)
    pyautogui.moveTo(signin)
    pyautogui.click(signin)



