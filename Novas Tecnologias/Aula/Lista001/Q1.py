s = {
    "Caixa": ["""
    ************
    *          *
    *          *
    *          *
    ************
    """],

    "Oval": ["""
        *****
      *       *
     *         *
     *         *
     *         *
      *       *
        *****
    """], #Não é o melhor ovo mas é o que deu pra fazerkkkkkkkk

    "Seta": ["""
        *
       ***
      *****
     *******
        *
        *
        *
        *
    """],

    "Losango": ["""
        *
      *   *
     *     *
    *       *
     *     *
      *   *
        *
    """]
}

for name, shape in s.items():
    print(name)
    print("\n".join(shape))
    print()