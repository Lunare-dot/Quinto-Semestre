from banco import Cliente, Conta

cliente = Cliente('João', 'Oliveira', '1111111111-1')
minha_conta1 = Conta('123-4', cliente, 120.0, 1000.0)
minha_conta2 = Conta('123-5', cliente, 120.0, 1000.0)
minha_conta3 = Conta('123-6', cliente, 120.0, 1000.0)

print(minha_conta1.get_total_contas())