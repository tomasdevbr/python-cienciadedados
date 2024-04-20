lista_glicemias = [100,98,100,98]

lista_moda = []
qtd_moda = 0
for item in lista_glicemias:
    ocorrencias = 0
    for outro_item in lista_glicemias:
        if(item == outro_item):
            ocorrencias += 1
    
    if(ocorrencias >= qtd_moda and item not in lista_moda):
        lista_moda.append(item)
        valor_moda = item
        qtd_moda = ocorrencias
    
print(qtd_moda)
print(lista_moda)