
valor_investido = float(input("Digite o valor Investido: "))

cliques = 0.0
pessoas = 0
compartilhamento = 0.0
# Este ponto aqui para o primeiro desafio não coloquei pq acho que não precisa
# Para cada 100 pessoas que visualizam o anúncio 12 clicam nele.

cliques =  100 / 12

# //a cada 20 pessoas que clicam no anúncio 3 compartilham nas redes sociais

compartilhamento = (20 * cliques) * 3

# cada compartilhamento nas redes sociais gera 40 novas visualizações.
# o mesmo anúncio é compartilhado no máximo 4 vezes em sequência
visualizacoes_compartilhada = (compartilhamento * 40) / 4

# 30 pessoas visualizam o anúncio original (não compartilhado) a cada R$ 1,00 investido.

visualizacoes_original = valor_investido * 30

print('Para o valor Investido de R$ {}, anúncio original irá alcançar {} Pessoas'.format(
    valor_investido, visualizacoes_original))
print('Para o valor Investido de R$ {}, o anúncio compartilhado irá alcançar {:.2f} Pessoas'.format(
    valor_investido, visualizacoes_compartilhada))
