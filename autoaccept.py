from LOLPixelBot.imagesearch import imagesearch_loop
import pyautogui

def AutoAccept():
    accept = imagesearch_loop(R"images\accept.png", 0.2)
    pyautogui.moveTo(accept, duration=2)
    pyautogui.click(accept) 