"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo
codigo=int(input("digite o codigo"))
quantidade=int(input("digite sua quantidade"))
if codigo == 1:
    preco=4.00
elif codigo ==2:
    comida="X-salada"
    preco=4.50
elif codigo ==3:
    comida="X-bacon"
    preco=5.00
elif codigo ==4:
    comida="torrada simples"
    preco=2.00
elif codigo ==5:
    comida="refrigerante"
    preco=1.50

total=preco * quantidade

print(f"comida:{comida}")
print(f"quantidade:{quantidade}")
print(f"total a pagar: R$ {total:2f}")
    
    
