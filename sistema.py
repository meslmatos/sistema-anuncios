from datetime import datetime

def diferenca_datas(date1, date2):
    d1 = datetime.strptime(date1, "%d/%m/%Y")
    d2 = datetime.strptime(date2, "%d/%m/%Y")
    return abs((d2 - d1).days)

def cadastrar_anuncio():
    print("Cadastro de Anúncios")
    print("Informe o nome do anúncio que será cadastrado:")
    nome = input()
    print("Informe o cliente:")
    cliente = input()
    print("Informe a data de início:")
    data_inicio = input()
    print("Informe a data de término:")
    data_termino = input()
    print("Informe o investimento diário:")
    investimento_diario = int(input())

    periodo = diferenca_datas(data_inicio, data_termino)
    total_investimento = periodo*investimento_diario
    print("O valor total investido é:", total_investimento)

    visualizacao_final = 0
    clique_final =0
    investimento = total_investimento

    visualizacao_original = investimento*30
    visualizacao_final = visualizacao_original

    cliques = visualizacao_original/100 * 12

    contador = 0 
    clique_final = cliques

    compartilhamento_final = 0

    while (contador < 4):
        compartilhamento= cliques/20 *3
        novas_visualizacoes = compartilhamento * 40
        cliques = novas_visualizacoes/100 * 12
        
        clique_final = clique_final + cliques
        visualizacao_final = visualizacao_final+novas_visualizacoes
        compartilhamento_final = compartilhamento_final+compartilhamento
        contador = contador+1  

    print()
    print("A quantidade máxima de visualizações é:",visualizacao_final)
    print("A quantidade máxima de cliques é:", clique_final)
    print("A quantidade máxima de compartilhamentos é:", compartilhamento_final)
    print()

    return { 
        "nome": nome, 
        "cliente": cliente,
        "data_inicio": data_inicio,
        "data_termino": data_termino,
        "investimento_diario": investimento_diario,
        "visualizacao_final": visualizacao_final,
        "clique_final": clique_final,
        "compartilhamento_final": compartilhamento_final
    }

def buscar_anuncios(anuncios):
    print("Digite o cliente para ser buscado:")
    cliente = input()
    resultado = next(item for item in anuncios if item["cliente"] == cliente)
    print()
    print(resultado)
    print()
    

anuncios = []
opcao = 0
while(opcao != 3):
    print("Escolha uma das opções")
    print("1-Cadastrar Anúncio")
    print("2-Buscar Anúncio")
    print("3-Sair do Sistema")
    opcao = int(input(">>>> "))
    print()

    if opcao == 1:
        anuncio = cadastrar_anuncio()
        anuncios.append(anuncio)
    elif (opcao==2):
        buscar_anuncios(anuncios)


    
