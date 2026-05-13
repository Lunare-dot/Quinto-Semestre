from jogo.dados import diceRoll
from jogo.eventos import eventSort

trigrinho = diceRoll()
resultado = eventSort(trigrinho)

print(f"Face do dado: {trigrinho}")
print(f"Divinação: {resultado}")