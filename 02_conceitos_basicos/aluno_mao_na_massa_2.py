# TODO: Desenvolva seu algoritmo aqui
# 1. Leia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pessoa
# 4. Imprima formatado usando f-string
valor = float(input("digite o valor da conta"))
numero = int(input("digite o numero de pessoas"))
valor_dividido = valor / numero
print(f"o9 valor que vai ficar para cada pessoa é {valor_dividido: .2f}")