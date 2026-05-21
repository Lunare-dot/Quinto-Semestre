from banco import Cliente, Conta

cliente = Cliente('João', 'Oliveira', '1111111111-1')
minha_conta = Conta('123-4', cliente, 120.0, 1000.0)

print(cliente)