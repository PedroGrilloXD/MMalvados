import pyaes

filename = 'image.png.pyransom'
KEY = b'brunobrunobruno1'

with open(filename, 'rb') as file:
    conteudo = file.read()

decrypt_data = pyaes.AESModeOfOperationCTR(KEY).decrypt(conteudo)

new_filename = filename.replace('.pyransom', '')
with open(new_filename, 'wb') as file:
    file.write(decrypt_data)
