import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
dataset = pd.read_csv('zoo.data')

dataset.head()
print(dataset)
print("Tipo de dado de cada coluna")
mostra = dataset.dtypes 
print(mostra)
print('mostra cada atributo das colunas')
coluna = list(dataset.columns)
print (coluna)

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

print('____Responde True com valores abaixo da Media:_____')
print('Coluna 1:') 
print('Media:',dataset['legs'].mean())
print(dataset[['legs']] < dataset[['legs']].mean())
print('Coluna 2:') 
print('Media:',dataset['type'].mean())
print(dataset[['type']] < dataset[['type']].mean()) 

print('____Responde True com valores acima da Media:_____')
print('Coluna 1:') 
print('Media:',dataset['legs'].mean())
print(dataset[['legs']] > dataset[['legs']].mean())
print('Coluna 2:') 
print('Media:',dataset['type'].mean())
print(dataset[['type']] > dataset[['type']].mean()) 

cols = ['hair','feathers','eggs','milk','airborne','aquatic','predator','toothed','back','bone','breathes','venomous','fins','legs','tail','domestic','catsize']
dataset.rename(columns={cols[0]:0, cols[1]:1, cols[2]:2, cols[3]:3,cols[4]:4, cols[5]:5, cols[6]:6, cols[7]:7,cols[8]:8, cols[9]:9, cols[10]:10, cols[11]:12,},inplace = True)
dataset.loc[::50]
print(dataset.shape)
print(dataset.describe())

colors = {'Iris-setosa': 'red','Iris-virginica':'blue','Iris-versicolor':'green'}
plt.scatter(
    dataset[2],
    dataset[3],
    c=dataset['Class'].map(colors),marker = '*'
)
plt.show()