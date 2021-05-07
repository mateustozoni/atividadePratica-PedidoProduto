"""
Atividade Prática - Pedido Produto - Angela
Alunos:
    Mateus José Pretti Tozoni - 21002275
    Henrique [completar] - [ra]
    Guilherme [completar] - [ra]
"""

from pprint import pprint

def products():
    return {
        111: {
            'nome': 'Feijão Preto',
            'valor': 5.5
        },
        112: {
            'nome': 'Feijão Carioca',
            'valor': 3.5
        },
        221: {
            'nome': 'Arroz Branco',
            'valor': 3.25
        },
        331: {
            'nome': 'Contra-filé',
            'valor': 2.25
        },
        332: {
            'nome': 'Frango Grelhado',
            'valor': 1.5
        },
        333: {
            'nome': 'File Mignon',
            'valor': 4.5
        },
        335: {
            'nome': 'Picanha',
            'valor': 7.5
        },
        441: {
            'nome': 'Fritas',
            'valor': 2.5
        },
        442: {
            'nome': 'Polenta',
            'valor': 2.5
        },
        443: {
            'nome': 'Salgadinhos',
            'valor': 2.5
        },
        444: {
            'nome': 'Batata assada',
            'valor': 2.5
        },
    }

def getProduct(id):
    return products()[id]

def lerPedido():
    #Pedir prods por pedido utilizando seguinte esquema
    """
    No. pedido: 1000
        Quantos produtos desse pedido? : 3
            No produto: 234
            Quantidade: 5
            No produto: 456
            Quantidade: 10
            No. produto: 225
            Quantidade: 25

    PARAR QUANDO O PEDIDO DIGITADO FOR -1
    """
    pedido = int(input("No. pedido: "))
    # TODO: Add error handler
    if pedido == -1:
        return None

    else:
        quantidade = int(input("\tQuantidade de produtos: "))
        # TODO: Add error handler
        produtos = {}

        for i in range(quantidade):
            # TODO: Add error handler
            prod = int(input('\t\tNo produto: '))
            qtd = int(input('\t\tQuantidade: '))
            produtos.update({prod: qtd})

        return {pedido: [quantidade, produtos]}

def main():
    pedidos = {}
    while True:
        pedido = lerPedido()
        if pedido is None:
            break
        pedidos.update(pedido)
    return pprint(pedidos)

if __name__ == '__main__':
    main()
