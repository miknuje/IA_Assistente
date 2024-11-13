import pyautogui
import time

def abrir_navegador():
    pyautogui.hotkey("ctrl", "alt", "t")  # Exemplo para Linux
    time.sleep(1)
    pyautogui.write("firefox\n")
    time.sleep(3)

def digitar_texto(texto):
    pyautogui.write(texto, interval=0.1)