eventos = {
    1: ("Você irá reencarnar como palmeirense.", "Tragédia sem precedentes."),
    2: ("O Corinthians será rebaixado esse ano.", "Infortúnio."),
    3: ("Vasco da Gama.", "Coitado."),
    4: ("Corinthians será campeão da CDB novamente!", "Sorte."),
    5: ("Palmeiras irá declarar falência!", "Riqueza."),
    6: ("Corinthians campeão da Libertadores 2026!", "Fortuna incomensuravél.")
}

def eventSort(rnum):
    mensagem, resultado = eventos.get(rnum, ("Evento desconhecido.", "Nada novo sob a luz do sol..."))
    print(mensagem)
    return resultado