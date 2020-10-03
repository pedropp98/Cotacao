# Cotação Dólar
API que pega a cotação do dólar comercial na moeda brasileira em tempo real.

## Requerimentos
Antes de utilizar as funções desse modúlo, certifique-se que seu environment tenha os módulos`lxml` e `requests` instalados. 
Para isso, pode-se utilizar:
```
pip install -r requirements.txt
```

## Como utilizar
Depois, importe `cotacao.py` e utilize os métodos
` import cotacao `

## Métodos
* `getDolar()`

O método `getDolar()` retorna uma string contendo o valor do dólar comercial em reais.

Exemplo
```
>>> import cotacao
>>> cotacao.getDolar()
R$ 5,32
```


* `DolarToFloat()`

O método `DolarToFloat()` retorna o valor do dólar comercial como uma variável do tipo float com duas casas decimais, que pode ser utilizada em operações matemáticas.

Exemplo
```
>>> import cotacao
>>> cotacao.DolarToFloat()
5.32
```
