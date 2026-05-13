from jogo.dados import diceRoll
from jogo.eventos import eventSort

tigrinho = diceRoll()
resultado = eventSort(tigrinho)

print(f"Face do dado: {tigrinho}")
print(f"Divinação: {resultado}")