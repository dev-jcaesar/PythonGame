# 1. Importar bibliotecas necessárias
import pywhatkit
import keyboard
import time
from datetime import datetime
# 2. Definir para quais contatos iremos enviar as mensagens
contatos = ['+5521999955889']
# 3. Definir intervalos de envio
while len(contatos) >= 1:
    # enviar mensagens
    pywhatkit.sendwhatmsg(contatos[0],'Eu te amo!',datetime.now().hour,datetime.now().minute)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_realease('ctrl + w')
# 4. Testar!