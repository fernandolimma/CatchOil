import pyautogui
import schedule
import time
import os
from winotify import Notification, audio

pyautogui.PAUSE = 2

# tela de notificação no windows
time.sleep(2)
notificacao = Notification(app_id="Vórtice Consulting & Tech", title="Iniciando automação!", msg="O processo de automação ocorrerá a cada (1) minuto.", icon=r"C:\CatchOil\logo_1.png")
notificacao.set_audio(audio.LoopingAlarm, loop=False)
notificacao.show()

def tarefa():
    print("Iniciando processo. Não mexa!")

    # tela de notificação no windows
    time.sleep(2)
    notificacao = Notification(app_id="Vórtice Consulting & Tech.", title="Aviso de automação!!!", msg="Não utilize o mouse e o teclado, até o processo terminar!", icon=r"C:\CatchOil\logo_2.png")
    notificacao.set_audio(audio.LoopingAlarm, loop=False)
    notificacao.show()

    time.sleep(6)
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save("screenshot.png")

    # Executa o atalho guest.lnk na raiz da aplicação
    time.sleep(10)
    os.startfile(os.path.join(os.getcwd(), "guest.lnk"))

    # Deixa o chrome em tela cheia
    time.sleep(4)
    pyautogui.hotkey("winleft", "up")

    # Logar na plataforma da Vórtice
    time.sleep(10)
    pyautogui.write("upload-ibama.vercel.app")
    time.sleep(4)
    pyautogui.press("enter")
    time.sleep(4)
    pyautogui.press("tab")
    time.sleep(4)
    pyautogui.write("fernandoaslima70@gmail.com")
    time.sleep(4)
    pyautogui.press("tab")
    time.sleep(4)
    pyautogui.write("1234")
    time.sleep(4)
    pyautogui.press("enter")

    # clica na posição do botão de upload
    time.sleep(4)
    pyautogui.click(x=683, y=403)

    # Faz upload
    time.sleep(4)
    pyautogui.write(r"C:\CatchOil\screenshot.png")
    time.sleep(4)
    pyautogui.press("enter")
    time.sleep(4)
    pyautogui.press("tab")
    time.sleep(4)
    pyautogui.press("enter")

    # Faz logout da Vórtice
    time.sleep(4)
    pyautogui.click(x=1321, y=146)

    # Fecha a janela do navegador
    time.sleep(2)
    pyautogui.hotkey("fn", "alt", "f4")

    # exclui a última imagem
    time.sleep(2)
    os.unlink("screenshot.png")

    # tela de notificação no windows
    time.sleep(2)
    notificacao = Notification(app_id="Vórtice Consulting & Tech..", title="Fim da automação!", msg="Equipamento liberado, obrigado.", icon=r"C:\CatchOil\logo_3.png")
    notificacao.set_audio(audio.LoopingAlarm, loop=False)
    notificacao.show()

    print("Processo finalizado!")

# schedule.every(5).seconds.do(tarefa)
schedule.every(1).minutes.do(tarefa)
# schedule.every(5).hours.do(tarefa)
# schedule.every(5).weeks.do(tarefa)
# schedule.every().day.at("06:18").do(tarefa)

while True:
    schedule.run_pending()
    time.sleep(2)
