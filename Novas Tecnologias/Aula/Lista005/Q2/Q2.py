from estatistica.leitor import ler_csv
from estatistica.analise import estatisticas

dados =  ler_csv(r"Novas Tecnologias\Aula\Lista005\Q2\estatistica\dados.csv")

resultado = estatisticas(dados, 'idade')

print(resultado)