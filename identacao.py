

def sacar(valor):
    saldo = 500
    
    if saldo >= valor:
        saldo -= valor
        print("valor sacado!")
        print(saldo)
          
sacar(100)
