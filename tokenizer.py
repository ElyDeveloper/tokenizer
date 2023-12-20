import tokenize
from io import BytesIO

def contar_tokens(archivo):
  with open(archivo, 'r') as file:
    codigo = file.read()
    tokens = list(tokenize.tokenize(BytesIO(codigo.encode('utf-8')).readline))
  return len(tokens)

print(contar_tokens('archivo.txt'))
