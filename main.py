import requests
from AcessoCep import BuscaEndereco

cep = 12081670
objeto_cep = BuscaEndereco(cep)


#r = requests.get("https://viacep.com.br/ws/01001000/json/")
#print(r.text)

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)
