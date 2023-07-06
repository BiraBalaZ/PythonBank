from conta import Conta

# A variável 'conta' recebe a Classe 'conta'
# conta = Conta('0000-1', 'Erick', 120.0)

contaErick = Conta('0000-1', 'Erick', 120.0)
contaRenato = Conta('0000-2', 'Renato', 143.0)

print(contaErick.numero)
print(contaErick.titular)
print(contaErick.saldo)
print(contaErick.limite)