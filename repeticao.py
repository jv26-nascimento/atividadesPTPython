""" for numero in range(0, 51, 5):
    print(numero, end=" ") """
    
    
    
    
opcao = -1
    
while opcao != 0:
    opcao = int(input("[1] sacar \n[2] extrato \n[0] sair \n: "))
    
    if opcao == 1:
        print("sacando...")
    elif opcao == 2:
        print("exibindo extrato...")
    elif opcao == 0:
        print("saindo...")
    else:
        print("opção inválida")