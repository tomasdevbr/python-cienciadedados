lista_glicemias = [100,98,78,45,238,390,67,89,100,98,100,88,67,55]

lista_glicemias_categorizada = []

for item in lista_glicemias:
    if item < 55:
        lista_glicemias_categorizada.append("Risco Abaixo")
    if item < 75:
        lista_glicemias_categorizada.append("Abaixo")
    elif item < 140:
        lista_glicemias_categorizada.append("Normal")
    elif item < 180:
        lista_glicemias_categorizada.append("Acima")
    else:
        lista_glicemias_categorizada.append("Risco Acima")

print(lista_glicemias_categorizada)


vezes_hipoglicemia = 0
for item in lista_glicemias_categorizada:
    if item in ['Risco Abaixo', 'Abaixo']:
        vezes_hipoglicemia += 1

print(vezes_hipoglicemia)

qtd_moda = 0
for item in lista_glicemias_categorizada:
    ocorrencias = 0
    for outro_item in lista_glicemias_categorizada:
        if(item == outro_item):
            ocorrencias += 1
    
    if(ocorrencias > qtd_moda):
        valor_moda = item
        qtd_moda = ocorrencias
    
print(valor_moda, qtd_moda)