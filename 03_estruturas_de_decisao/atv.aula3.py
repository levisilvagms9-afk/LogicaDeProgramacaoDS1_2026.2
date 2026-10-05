# TODO: Implemente o menu utilizando match-case ou elif
opcao = int(input("Digite a opção desejada (1, 2 ou 3): "))
if opcao == 1:
    print("consultar livro")
elif opcao == 2:
    print("realizar emprestimo")
elif opcao == 3:
    print("devolver livro")
else:
    print("opção invalido")