import requests

BASE = 'http://127.0.0.1:5000/'



resposta = requests.get(BASE + "videos")
print(resposta.json())

"""
dados = [
    {
        "likes": 70,
        "nome": "João",
        "visualizacoes": 1000
    },
    {
        "likes": 70,
        "nome": "Pedro",
        "visualizacoes": 2000
    },
    {
        "likes": 70,
        "nome": "Carlos",
        "visualizacoes": 1000
    },
    {
        "likes": 70,
        "nome": "Peter",
        "visualizacoes": 1000
    },
    {
        "likes": 70,
        "nome": "Pierre",
        "visualizacoes": 1000
    }
]

resposta = requests.post(
    BASE + "video/2",
    {
        "likes": 70,
        "nome": "João",
        "visualizacoes": 1000
    }
)

for indice, dado in enumerate(dados):
    resposta = requests.post(
        BASE + f'video/{indice+10}',
        {
            "likes": dado['likes'],
            "nome": dado['nome'],
            "visualizacoes": dado['visualizacoes']
        }
    )

print(resposta.json())

input()

resposta = requests.get(BASE + "video/1")
print(resposta.json())
"""