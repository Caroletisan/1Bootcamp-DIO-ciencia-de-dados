def sacar(valor): # inicio do bloco de método
    saldo = 500

    if saldo >= valor: # inicio do bloco do if
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.") 
    # fim do bloco if

    print("Obrigado por ser nosso cliente, tenha um bom dia!")


def depositar(valor):
    saldo = 500
    saldo += valor
# fim do bloco do método

sacar(1000)
