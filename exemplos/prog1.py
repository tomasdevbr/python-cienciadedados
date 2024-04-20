linha = '2024;146;20 0;20'
linha = linha.replace(' ', ';')
vetor_linha = linha.split(';')
print(vetor_linha)
# print(len(vetor_linha))
# print(range(len(vetor_linha)))
# for item in vetor_linha:
#     print(item)
# for i in range(len(vetor_linha)):
#     print(vetor_linha[i])

if int(vetor_linha[1]) < 80:
    vetor_linha[1] = 'Abaixo'
elif int(vetor_linha[1]) < 140:
    vetor_linha[1] = 'Normal'
else:
    vetor_linha[1] = 'Acima'

print(vetor_linha)

if int(vetor_linha[3]) < 100:
    vetor_linha[3] = 'Abaixo'
elif int(vetor_linha[1]) < 200:
    vetor_linha[3] = 'Normal'
else:
    vetor_linha[3] = 'Acima'

print(vetor_linha)