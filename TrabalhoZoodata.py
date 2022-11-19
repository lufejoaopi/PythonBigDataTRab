import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
dataset = pd.read_csv('C:/Users/bened/Downloads/zoo.data')

dataset.head()
print(dataset)
print("Tipo de dado de cada coluna")
mostra = dataset.dtypes 
print(mostra)
print('mostra cada atributo das colunas')
coluna = list(dataset.columns)
print (coluna)
display(dataset)
input("Aperte <enter> para continuar")

print( '__Media das Colunas__')
print('Media da coluna 14\n ', dataset['legs'].mean())
print('Media da coluna 18\n ', dataset['type'].mean())

print('___Desvio Padrao___')
print('Desvio padrão da coluna 14\n ', dataset['legs'].std())
print('Desvio padrão da coluna 18\n ', dataset['type'].std())

print('_______Moda_______')
print('Moda da coluna 14\n ', dataset['legs'].mode())
print('Moda da coluna 18\n ', dataset['type'].mode())

print('_______Mediana_______')
print('Mediana da coluna 14\n ', dataset['legs'].median())
print('Mediana da coluna 18\n ', dataset['type'].median())

print('_______Valor_Maximo_______')
print('Max da coluna 14\n ', dataset['legs'].max())
print('Max da coluna 18\n ', dataset['type'].max())

print('_______Valor_Minimo_______')
print('Min da coluna 14\n ', dataset['legs'].min())
print('Min da coluna 18\n ', dataset['type'].min())

input("Aperte <enter> para continuar")

print('______Tabela Odenada de Forma Ascendente_______')
print(dataset.sort_values('type'))
print('______Tabela Ordenada de Forma Descendente_______')
print(dataset.sort_values('type', ascending=False))

print(dataset['type'].describe())

input("Aperte <enter> para continuar")

print('____Coluna com valores abaixo da Media:_____')
print('Coluna 1:') 
print('Media:',dataset['legs'].mean())
print(dataset[['legs']] < dataset[['legs']].mean())
print('Coluna 2:') 
print('Media:',dataset['type'].mean())
print(dataset[['type']] < dataset[['type']].mean()) 

print('____Coluna com valores acima da Media:_____')
print('Coluna 1:') 
print('Media:',dataset['legs'].mean())
print(dataset[['legs']] > dataset[['legs']].mean())
print('Coluna 2:') 
print('Media:',dataset['type'].mean())
print(dataset[['type']] > dataset[['type']].mean()) 
