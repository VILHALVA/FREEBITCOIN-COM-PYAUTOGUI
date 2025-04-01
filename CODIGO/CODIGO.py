import pyautogui
import subprocess
import time

url = "https://freebitco.in/?op=home"

caminho_chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

subprocess.Popen([caminho_chrome, url])

time.sleep(15)

for _ in range(5):  
    pyautogui.scroll(-500)  
    time.sleep(1) 

botoes = ["./ROLAR.jpg", "./ROLL.jpg"]

while True:
    try:
        for botao in botoes:
            botao_posicao = pyautogui.locateCenterOnScreen(botao, confidence=0.8)
            if botao_posicao:
                pyautogui.click(botao_posicao)  
                print(f"✅ Botão '{botao}' clicado com sucesso!")
                exit()  
    except pyautogui.ImageNotFoundException:
        print("🔴 Nenhuma imagem encontrada. Tentando novamente...")
    
    time.sleep(1)  