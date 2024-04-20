lista_glicemias = [100,98,78,45,238,390,67,89,100,98,100,88,67,55]

soma = 0
for item in lista_glicemias:
    soma += int(item)
    if item < 75:
        print(item, "Abaixo")
    elif item < 140:
        print(item, "Normal")
    else:
        print(item, "Acima")

media = soma / len(lista_glicemias)
print('Média ->',media)

lista_glicemias.sort()
print(lista_glicemias)

indice_meio = int(len(lista_glicemias) / 2)
mediana = lista_glicemias[indice_meio]
print('Mediana ->', mediana)

vezes_hipoglicemia = 0
for item in lista_glicemias:
    if item < 70:
        vezes_hipoglicemia += 1

print('Quantidade de hipoglicemias ->', vezes_hipoglicemia)

#len(lista_glicemias) --- 100%
#vezes_hipoglicemia   --- x

porcentagem_hipoglicemia = vezes_hipoglicemia * 100 / len(lista_glicemias)
print(porcentagem_hipoglicemia)

moda = ''
qtd_moda = 0
for item in lista_glicemias:
    ocorrencias = 0
    for outro_item in lista_glicemias:
        if(item == outro_item):
            ocorrencias += 1
    
    if(ocorrencias > qtd_moda):
        valor_moda = item
        qtd_moda = ocorrencias




