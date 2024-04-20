with open('data2.dat', 'w', encoding='utf-8') as file:
    file.write('123;223;20')
    file.flush()

procurador_leitura = open('data2.dat', 'r', encoding='utf-8')
procurador_leitura.close()

with open('data2.dat', 'r', encoding='utf-8') as file:
    print(file.readline())
    file.seek(0)
    print(file.readlines())

with open('data2.dat', 'w', encoding='utf-8') as file:
    file.writelines(['teste 1\n', 'teste 2\n'])
    # for linha in file:
    #     print(linha, end='')