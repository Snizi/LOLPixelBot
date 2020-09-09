# import time
# import keyboard
# import pyautogui
# from pynput.mouse import Button, Controller
# import win32gui
# import cv2
# import numpy as np
# import imagesearch
# from directkeys import PressKeyPynput, ReleaseKeyPynput, P, F2, F3, F4, F5, SPACE, W, A, R, LCTRL, ENTER
# from gameplay import enumHandler, typedefClickNum, enumHandlerLauncher, click_image, imagesearcharea, typedefClickTypeNum
#
# mouse = Controller()
#
#
#
#
# def JoinMatch():
#             time.sleep(3)
#             play = pyautogui.locateOnScreen('images/play.png', grayscale=1, confidence=.8)
#             time.sleep(3)
#             pyautogui.click(play)
#
#             time.sleep(3)
#             coop = pyautogui.locateOnScreen('images/co-op.png', grayscale=1, confidence=.8)
#             time.sleep(3)
#             pyautogui.click(coop)
#
#             time.sleep(3)
#             medium = pyautogui.locateOnScreen('images/intermediate.png', grayscale=1, confidence=.8)
#             time.sleep(3)
#             pyautogui.click(medium)
#
#             time.sleep(3)
#             confirm = pyautogui.locateOnScreen('images/confirm.png', grayscale=1, confidence=.8)
#             time.sleep(3)
#             pyautogui.click(confirm)
#
#             time.sleep(3)
#             match = pyautogui.locateOnScreen('images/match.png', grayscale=1, confidence=.8)
#             time.sleep(3)
#             pyautogui.click(match)
#
#
# def AutoAccept():
#     while 1:
#         accbutt = pyautogui.locateOnScreen('images/accept.png', grayscale=True, confidence=.8)
#         time.sleep(3)
#         if accbutt is not None:
#             pyautogui.click(accbutt)
#             print('Match accepted')
#             break
#         pass
#
#
# def PickChampion():
#         try:
#             search = imagesearch.imagesearch_numLoop('images/search.png', 1, 20)
#             lobby = pyautogui.locateOnScreen('images/match.png', confidence=0.8, grayscale=1)
#             if lobby is not None:
#                 time.sleep(3)
#                 pyautogui.click(lobby)
#                 AutoAccept()
#                 pass
#             time.sleep(2)
#             if search is not None:
#
#                 pyautogui.click(search)
#                 time.sleep(1)
#                 pyautogui.click(search)
#                 pyautogui.typewrite('soraka')
#
#                 time.sleep(2)
#                 soraka = pyautogui.locateOnScreen('images/soraka.png', grayscale=1, confidence=.8, region=(0,0, 1200, 800))
#                 pyautogui.click(soraka)
#                 time.sleep(2)
#                 confirm = pyautogui.locateOnScreen('images/confirm.png', grayscale=1, confidence=.7, region=(0,0, 1200, 800))
#                 time.sleep(3)
#                 pyautogui.click(confirm)
#                 print('Soraka Locked')
#
#                 time.sleep(2)
#                 chat = pyautogui.locateOnScreen('images/chat.png', grayscale=1, confidence=.8, region=(0,0, 1200, 800))
#                 pyautogui.click(chat)
#                 pyautogui.typewrite('suporte do time')
#                 time.sleep(2)
#                 pyautogui.click(chat)
#                 PressKeyPynput(ENTER)
#                 ReleaseKeyPynput(ENTER)
#         except:
#
#             annie = pyautogui.locateOnScreen('images/annie.png', grayscale=1, confidence=.8, region=(0, 0, 1200, 800))
#             if annie is not None:
#                 pyautogui.click(annie)
#                 time.sleep(2)
#                 confirm = pyautogui.locateOnScreen('images/confirm.png', grayscale=1, confidence=.7,region=(0, 0, 1200, 800))
#                 time.sleep(3)
#                 pyautogui.click(confirm)
#                 print('Annie Locked')
#
#
#
#
#
#
# def InGame():
#     while imagesearch('images/corner.png')[0] == -1:
#         time.sleep(2)
#         print('Loading game...')
#
#     print('Game loaded...')
#     Gameplay()
#
#
# def GetRewards():
#     while 1:
#         time.sleep(3)
#         ok = pyautogui.locateOnScreen('images/leved.png', confidence=.8, grayscale=1, region=(0,0, 1200, 800))
#         if ok is None:
#             break
#         pyautogui.click(ok)
#
#
# def Player2():
#     keyboard.press_and_release('1')
#
#     mouse.position = (670, 533)
#     mouse.press(Button.right)
#     mouse.release(Button.right)
#
#     time.sleep(0.5)
#     PressKeyPynput(A)
#     ReleaseKeyPynput(A)
#
#
# def Player3():
#     keyboard.press_and_release('2')
#
#     mouse.position = (670, 533)
#     mouse.press(Button.right)
#     mouse.release(Button.right)
#
#     time.sleep(0.5)
#     PressKeyPynput(A)
#     ReleaseKeyPynput(A)
#
#
# def Player4():
#     keyboard.press_and_release('3')
#
#     mouse.position = (670, 533)
#     mouse.press(Button.right)
#     mouse.release(Button.right)
#
#     time.sleep(0.5)
#     PressKeyPynput(A)
#     ReleaseKeyPynput(A)
#
#
# def Player5():
#     keyboard.press_and_release('4')
#
#
#     mouse.position = (670, 533)
#     mouse.press(Button.right)
#     mouse.release(Button.right)
#
#     time.sleep(0.5)
#     PressKeyPynput(A)
#     ReleaseKeyPynput(A)
#
#
# def Skill(player, x, y):
#     ReleaseKeyPynput(player)
#
#     skill = 0
#     PressKeyPynput(SPACE)
#     ReleaseKeyPynput(SPACE)
#
#     mouse.press(Button.right)
#     mouse.release(Button.right)
#
#     time.sleep(1)
#     mouse.position = (x, y)
#     time.sleep(1)
#
#     CastW()
#
#     return skill
#
#
# def CastW():
#     # level up the W
#     keyboard.press_and_release('k')
#
#     # cast the w
#     keyboard.press_and_release('w')
#
#
# def CastR():
#     # level up the r
#     PressKeyPynput(LCTRL)
#     PressKeyPynput(R)
#     ReleaseKeyPynput(LCTRL)
#     ReleaseKeyPynput(R)
#
#     # cast the r
#     PressKeyPynput(R)
#     ReleaseKeyPynput(R)
#
#
# def Gameplay():
#     skill_cooldown = 0
#     ultimate = 0
#     alternate_player = 1200
#
#     time.sleep(2)
#
#     mouse.position = (724, 366)
#     mouse.click(Button.left, 2)
#     win32gui.EnumWindows(enumHandler, None)
#
#
#     time.sleep(2)
#     # BuyEdge()
#     while True:
#         try:
#             alternate_player -= 1
#             time.sleep(1)
#
#
#             if alternate_player <= 1200 and alternate_player >= 1080:
#                 print(alternate_player)
#                 Player2()
#                 #player health bar x,y and the rgb tuple
#                 if pyautogui.pixelMatchesColor(838, 505, (19, 19, 19)):
#                     pyautogui.moveTo(838, 505)
#                     time.sleep(1)
#                     CastW()
#
#
#             if alternate_player <= 1080 and alternate_player >= 960:
#
#                 print(alternate_player)
#                 Player3()
#                 # player health bar x,y and the rgb tuple
#                 if pyautogui.pixelMatchesColor(888, 505, (19, 19, 19)):
#                     pyautogui.moveTo(888, 505)
#                     time.sleep(1)
#                     CastW()
#
#
#             if alternate_player <= 960 and alternate_player >= 720:
#                 print(alternate_player)
#                 Player4()
#                 # player health bar x,y and the rgb tuple
#                 if pyautogui.pixelMatchesColor(947, 505, (19, 19, 19)):
#                     pyautogui.moveTo(947, 505)
#                     time.sleep(1)
#                     CastW()
#
#             if alternate_player <= 720 and alternate_player >= 0:
#                 print(alternate_player)
#                 Player5()
#                 # player health bar x,y and the rgb tuple
#                 if pyautogui.pixelMatchesColor(1006, 505, (19, 19, 19)):
#                     pyautogui.moveTo(1006, 505)
#                     time.sleep(1)
#                     CastW()
#
#
#             next = pyautogui.locateOnScreen('images/next.png', grayscale=1, confidence=.8, region=(0,0, 1200, 800))
#             if next is not None:
#                 print('next image found')
#                 time.sleep(2)
#                 pyautogui.click(next)
#                 GoNext()
#                 break
#         except:
#             continue
#
#
# def BuyEdge():
#     # open the store
#     try:
#         print('Buying Edge')
#         PressKeyPynput(P)
#         time.sleep(1)
#         gume = pyautogui.center(pyautogui.locateOnScreen('images/gume.png', confidence=0.8, grayscale=1, region=(0,0, 1200, 800)))
#         time.sleep(1)
#         mouse.position = (gume.x, gume.y)
#         mouse.press(Button.right)
#         mouse.release(Button.right)
#         time.sleep(1)
#
#         close = pyautogui.center(pyautogui.locateOnScreen('images/close_store.png', confidence=0.8, grayscale=1, region=(0,0, 1200, 800)))
#         time.sleep(1)
#         mouse.position = (close.x, close.y)
#         time.sleep(1)
#         mouse.click(Button.left, 2)
#         print('Edge buyed')
#     except:
#         print('Coudnt buy edge =(')
#         print('Closing store')
#         close = pyautogui.center(
#             pyautogui.locateOnScreen('images/close_store.png', confidence=0.8, grayscale=1, region=(0, 0, 1200, 800)))
#         time.sleep(1)
#         mouse.position = (close.x, close.y)
#         time.sleep(1)
#         mouse.click(Button.left, 2)
#         # close the store
#
#
#
# def GoNext():
#     while True:
#         play_again = pyautogui.locateOnScreen('images/play_again.png', grayscale=1, confidence=.8, region=(0, 0, 1200, 800))
#         if play_again is not None:
#             reward = pyautogui.locateOnScreen('images/ok.png', grayscale=1, confidence=.8, region =(0, 0, 1200, 800))
#             while reward is not None:
#                 reward = pyautogui.locateOnScreen('images/ok.png', grayscale=1, confidence=.8)
#                 time.sleep(3)
#                 pyautogui.click(reward)
#             time.sleep(2)
#             pyautogui.click(play_again)
#             time.sleep(3)
#             while True:
#                 match = pyautogui.locateOnScreen('images/match.png', grayscale=1, confidence=.8, region=(0, 0, 1200, 800))
#                 if match is not None:
#                     time.sleep(3)
#                     pyautogui.click(match)
#                     AutoAccept()
#                     break
#             break
#
#         continue
#
# def checkLeaver():
#     pos = imagesearcharea('images/oklevelup.png', 0, 150, 1280, 720)
#     if pos[0] != -1:
#         if imagesearch('images/leaverbuster.png')[0] != -1:
#             typedefClickNum('images/leaverbuster.png')
#             time.sleep(1)
#             pyautogui.typewrite('I Agree')
#         click_image('images/oklevelup.png', (pos[0], pos[1] + 150), 'left', 1)
#
#
# def endgame():
#     time.sleep(5)
#     typedefClickNum('images/next.png', 10)
#     win32gui.EnumWindows(enumHandlerLauncher, None)
#     win32gui.EnumWindows(enumHandlerLauncher, None)
#     checkLeaver()
#     pos = imagesearcharea('images/ok.png', 0, 150, 1280, 720)
#     while pos[0] != -1:
#         click_image('images/oklevelup.png', (pos[0], pos[1] + 150), 'left', 1)
#
#
#
# def enumHandler(hwnd, lParam):
#     if win32gui.IsWindowVisible(hwnd):
#         pass
#     if 'League of Legends (TM) Client' in win32gui.GetWindowText(hwnd):
#         win32gui.MoveWindow(hwnd, 0, 0, 1024, 768, True)
#
#
# JoinMatch()
# while True:
#     AutoAccept()
#     PickChampion()
#     InGame()
#
#
#
#
