from typing import List

def numDecrypt(sequence: int):
    s = str(sequence)
    if len(s) != 4 or not s.isdigit():
        print("O número criptografado deve conter quatro digitos.")
        return None
    
    decrypt = [(int(ch) - 7) % 10 for ch in s]
    return decrypt

def numReverse(sequence: List[int]) -> List[int]:
    sequence[2], sequence[0] = sequence[0], sequence[2]
    sequence[3], sequence[1] = sequence[1], sequence[3]
    return sequence
    
entry = input("Insira o número criptografado: ")
num = numDecrypt(entry)
decrypt = numReverse(num)
print(decrypt)