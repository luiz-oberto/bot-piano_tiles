# Projeto 3 - zerar game piano tiles com Pyautogui
import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

# link para o jogo https://gameforge.com/pt-BR/littlegames/magic-piano-tiles/#

# para dar start no jogo
pyautogui.click(1404,508, duration=1)

# Função de clicar na tecla
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

while keyboard.is_pressed('1') == False: # se apertar 1 o programa vai parar de funcionar
    if pyautogui.pixelMatchesColor(1267,416, (0,0,0)):
        click(1267,416)
    if pyautogui.pixelMatchesColor(1357,417, (0,0,0)):
        click(1357,417)
    if pyautogui.pixelMatchesColor(1443,420, (0,0,0)):
        click(1443,420)
    if pyautogui.pixelMatchesColor(1545,411, (0,0,0)):
        click(1545,411)
