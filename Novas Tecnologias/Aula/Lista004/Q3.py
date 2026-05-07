#3x^2 + 2x^1 + 1x^0

a = float(input("Entre com o coef. a: "))
b = float(input("Entre com o coef. b: "))
c = float(input("Entre com o coef. c: "))

poli1 = {2:a, 1:b, 0:c}

a = float(input("Entre com o coef. a: "))
b = float(input("Entre com o coef. b: "))
c = float(input("Entre com o coef. c: "))

poli2 = {2:a, 1:b, 0:c}

poliresult = {}

for i in range(3):
    poliresult[i] = poli1[i] * poli2[i]

print(f"{poliresult[2]}^2 + {poliresult[1]}^1 + {poliresult[0]}^0")