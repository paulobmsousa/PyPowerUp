import pyautogui
import time
import pandas

'''
Pyautogui commands:
- pyautogui.click -> click in some place
- pyautogui.press -> press a key (1)
- pyautogui.write -> write a text
- pyautogui.hotkey -> press a combination of keys (shortcut)
'''
pyautogui.PAUSE = 0.5
# Step 1: Enter enterprise site
# 1.1. Open chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
# 1.2. Enter the site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
# Wait a little
time.sleep(3)

# Step 2: Login
# Email fulfill
pyautogui.click(x=649, y=477)
pyautogui.write("pythonimpressionador@gmail.com")
# Password fulfill
pyautogui.press("tab")
pyautogui.write("minhasenhasupersecreta")
# Submit
pyautogui.press("tab")
pyautogui.press("enter")

# Step 3: Import database
tabela = pandas.read_csv('produtos.csv')
print(tabela)

# Step 4: Record products
for linha in tabela.index:
    pyautogui.click(x=613, y=328)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    # Return to beginning
    pyautogui.scroll(10000)

# Step 5: Repeat to all products
