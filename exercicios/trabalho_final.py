import sys
sys.path.append('/content/drive/MyDrive/especializacao/')

import matplotlib.pyplot as plt
import pandas as pd


arquivo = '/content/drive/MyDrive/especializacao/glicose_data_suja.csv'
df = pd.read_csv(arquivo)
df.drop('Antes Comer / Depois Comer ', axis=1, inplace=True)
df.dropna(inplace=True)

media_glicemia = df['Resultado'].mean()
media_kcal = df['kcal'].mean()
media_carb = df['carb'].mean()

mediana_glicemia = df['Resultado'].median()
mediana_kcal = df['kcal'].median()
mediana_carb = df['carb'].median()

moda_glicemia = df['Resultado'].mode()
moda_kcal = df['kcal'].mode()
moda_carb = df['carb'].mode()

df_final = pd.DataFrame(
    {
      'glicemia': {
          'media': media_glicemia,
          'mediana': mediana_glicemia,
          'moda': ', '.join([str(value) for value in moda_glicemia.values])
      },
      'kcal': {
          'media': media_kcal,
          'mediana': mediana_kcal,
          'moda': ', '.join([str(value) for value in moda_kcal.values])
      },
      'carb': {
          'media': media_carb,
          'mediana': mediana_carb,
          'moda': ', '.join([str(value) for value in moda_carb.values])
      }
    }
)

df_final