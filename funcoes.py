def mensagem():
    print("olá mundo")
    
def mensagem_2(nome):
    print(f"seja bem vindo {nome}!")
    
def mensagem_3(nome = "toninho"):
    print(f"seja bem vindo {nome}!")
    
""" mensagem()
mensagem_2(nome = "gui")
mensagem_2("gui")
mensagem_3()
mensagem_3(nome = "chapolin") """

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    if funcao == somar:
        sinal = "+"
    elif funcao == subtrair:
        sinal = "-"
    print(f"{a} {sinal} {b} = {resultado}")
    
exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)