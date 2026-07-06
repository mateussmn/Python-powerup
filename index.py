import pyautogui, time

#1 Entrar no sistema da empresa
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")

#2 Fazer o login no sistema
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3) #Pausa para carregar o site
pyautogui.press("tab")
#pyautogui.click(x=613, y=556)
pyautogui.write("xdd")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3) #Pausa para carregar o site