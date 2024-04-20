lista_glicemias = []

with open('data.dat', 'r', encoding='utf-8') as dados:
    for linha in dados:
        vetor_linha = linha.split(';')
        valor_corrigido = vetor_linha[1].replace('\n','')
        lista_glicemias.append(valor_corrigido)

print(lista_glicemias)