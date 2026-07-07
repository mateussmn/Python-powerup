import pyautogui, time, pandas as pd

#1 Entrar no sistema da empresa
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")

#2 Fazer o login no sistema
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(4) #Pausa para carregar o site
pyautogui.click(x=613, y=556)
pyautogui.write("xdd")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3) #Pausa para carregar o site

#3 Abrir a base de dados
tabela = pd.read_csv("produtos.csv")

#4 Cadastrar os produtos da tabela
for linha in tabela.index:
    #codigo
    codigo = str(tabela.loc[linha,"codigo"])
    pyautogui.click(x=721, y=389)
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #categoria
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    #preco_unitario
    preco_unitario = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    #custo
    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    #obs
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)