# Desafio técnico Python para a vaga na MaisTodos

## Este projeto consiste em uma API que intermedia a requisição da ERP do varegista à API do MaisTodos

## Fluxograma

1. ERP do varegista faz a requisição nesta API (note que o endereço foi customizado):
```
POST /cashApi/sale 
```

```
{
    "sold_at": "2026-01-02 00:00:00",
    "customer": {
       "document": "00000000000",
       "name": "JOSE DA SILVA",
    },
    "total": "100.00",
    "products": [
       {
          "type": "A",
          "value": "10.00",
          "qty": 1,
       },
       {
          "type": "B",
          "value": "10.00",
          "qty": 9,
       }
    ],
}
```

### Observações:
- Somente é possível enviar qualquer requisição utilizando um Token de acesso e incluindo-o no cabeçalho da requisição, conforme mostrado abaixo:

```
 header = {
    'Authorization': 'Token <Token>'
 } 
```

- A API fará a validação do CPF e do somatório dos valores totais dos produtos. Compras com datas futuras ou com tipos não listados não serão aceitos.

3. Após a validação dos dados, a API calcula o valor do cashback e armazena todos os dados recebidos.

4. Em seguida, repassa os valores calculados para a API da MaisTODOS.


## Referências

Também foram documentadas as pesquisas ao longo do projeto. O acesso a essas informações pode ser feito através do [link](https://www.notion.so/Desafio-t-cnico-MaisTODOS-66e06f6d18494fe8b901e26a0f43d909)
