''' 
    Este código tem o objetivo de calcular o alcance de anúncio a partir do valor investido 
'''
visualizacao_final = 0
print("Digite valor que será investido?")
investimento = int(input())

visualizacao_original = investimento*30
visualizacao_final = visualizacao_original

cliques = visualizacao_original/100 * 12
contador = 0 

'''
#   Laço de repetição para calcular as sequências de compartilhamento
'''
while (contador < 4):
    compartilhamento= cliques/20 *3
    novas_visualizacoes = compartilhamento * 40
    cliques = novas_visualizacoes/100 * 12
    
    visualizacao_final = visualizacao_final+novas_visualizacoes
    contador = contador+1  

print("A quantidade máxima de visualizações é:",visualizacao_final)
