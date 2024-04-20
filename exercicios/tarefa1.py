from statistics import mean, median, mode, quantiles

class Glicemia:
    def __init__(self, dia_semana, ano, valor_glicemia, valor_insulina, kcal, carb, qualidade_sono):
        self.dia_semana = dia_semana
        self.ano = ano
        self.valor_glicemia = valor_glicemia
        self.valor_insulina = valor_insulina
        self.kcal = kcal
        self.carb = carb
        self.qualidade_sono = qualidade_sono

    def __repr__(self) -> str:
        monta_str = ', '.join([f'{key}: {value}' for key, value in vars(self).items()])
        return f'{ {monta_str} }'


glicemias = []
with open('dados_glicemia.csv', 'r', encoding='utf-8') as data:
    for linha in data.readlines():
        glicemia = linha.replace('\n', '').split(';')
        glicemia.remove(glicemia[2])
        glicemias.append(Glicemia(*glicemia))

valores_de_glicemia = [int(glicemia.valor_glicemia) for glicemia in glicemias]
valores_de_kcal = [int(glicemia.kcal) for glicemia in glicemias]
valores_de_carb = [int(glicemia.carb) for glicemia in glicemias]

print('A média do valor da glicemia é: ', mean(valores_de_glicemia))
print('A mediana do valor da glicemia é: ', median(valores_de_glicemia))
print('A moda do valor da glicemia é: ', mode(valores_de_glicemia))

print('A média do valor de kcal é: ', mean(valores_de_kcal))
print('A mediana do valor de kcal é: ', median(valores_de_kcal))
print('A moda do valor de kcal é: ', mode(valores_de_kcal))

print('A média do carboidrato é: ', mean(valores_de_carb))
print('A mediana do carboidrato é: ', median(valores_de_carb))
print('A moda do carboidrato é: ', mode(valores_de_carb))