from itertools import combinations

def targetNumber(nums: list[int], target: int) -> bool:
    for r in range(len(nums) + 1):
        for subset in combinations(nums, r):
            if sum(subset) == target:
                return True
    return False
    
    
casos = [
    ([3, 34, 4, 12, 5, 2], 9, True),
    ([3, 34, 4, 12, 5, 2], 30, False),
    ([1, 2, 3], 6, True),
    ([1, 2, 3], 7, False),
]

for nums, target, esperado in casos:
    resultado = targetNumber(nums, target)
    status = "Existe!" if resultado == esperado else "Não existe!"
    print(f"{status} {nums}, alvo = {target} -> {resultado}")