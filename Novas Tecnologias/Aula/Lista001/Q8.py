from typing import List

def numSplit(sequence: int):
    s = str(sequence)
    if  len(s) != 4 or not s.isdigit():
        print("O número deve conter APENAS quatro digitos inteiros.")
        return None
    
    digits = [(int(ch) + 7) % 10 for ch in s]
    return digits

def numSwap(sequence: List[int]) -> List[int]:
    sequence[0], sequence[2] = sequence[2], sequence[0]
    sequence[1], sequence[3] = sequence[3], sequence[1]
    return sequence
    
entry = input("Digite um número de quatro dígitos: ")
num = numSplit(entry)
swap = numSwap(num)
print(swap)
