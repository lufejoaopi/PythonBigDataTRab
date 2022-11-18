import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
dataset = pd.read_csv('C:/Users/bened/Downloads/zoo.data')

#print('tipos')
#indices de tipo inteiro
#s1 = pd.Series([1, 3, 4, 5, np.nan, 7, 8])
#s1 = pd.DataFrame(np.random.randn(6, 4), columns=list("ABCD"))
dataset.head()
#print(s1)
print(dataset)
print("Tipo de dado de cada coluna")
mostra = dataset.dtypes 
print(mostra)
#s1 = df['legs'].mean()
print('mostra cada atributo das colunas')
coluna = list(dataset.columns)
print (coluna)
display(dataset)
input("Aperte <enter> para continuar")

#s1 = s1.style.highlight_max(color ='lightgreen', axis = 0)
print( '__Media das Colunas__')
print('Media da coluna 14\n ', dataset['legs'].mean())
print('Media da coluna 18\n ', dataset['type'].mean())
#print('Media da coluna 18\n ', dataset['type'].mean())


print('___Desvio Padrao___')
print('Desvio padrão da coluna 14\n ', dataset['legs'].std())
print('Desvio padrão da coluna 18\n ', dataset['type'].std())
#print('Desvio padrão da coluna 18\n ', dataset['type'].std())

print('_______Moda_______')
print('Moda da coluna 14\n ', dataset['legs'].mode())
print('Moda da coluna 18\n ', dataset['type'].mode())
#print('Moda da coluna 18\n ', dataset['type'].mode())

print('_______Mediana_______')
print('Mediana da coluna 14\n ', dataset['legs'].median())
print('Mediana da coluna 18\n ', dataset['type'].median())
#print('Mediana da coluna 18\n ', dataset['type'].median())


print('_______Valor_Maximo_______')
print('Max da coluna 14\n ', dataset['legs'].max())
print('Max da coluna 18\n ', dataset['type'].max())
#print('Max da coluna 5\n ', dataset['donatedBlood'].max())

print('_______Valor_Minimo_______')
print('Min da coluna 14\n ', dataset['legs'].min())
print('Min da coluna 18\n ', dataset['type'].min())
#print('Min da coluna 5\n ', dataset['donatedBlood'].min())


input("Aperte <enter> para continuar")

#print('min da coluna 1:\n ',dataset['Sepallength'].min())
print('______Tabela Odenada de Forma Ascendente_______')
print(dataset.sort_values('type'))
print('______Tabela Ordenada de Forma Descendente_______')
print(dataset.sort_values('type', ascending=False))

print(dataset['type'].describe())

input("Aperte <enter> para continuar")

print('____Coluna com valores abaixo da Media:_____')
print('Coluna 1:') 
print('Media:',dataset['Recency'].mean())
print(dataset[['Recency']] < dataset[['Recency']].mean())
print('Coluna 2:') 
print('Media:',dataset['Frequency'].mean())
print(dataset[['Frequency']] < dataset[['Frequency']].mean()) 
print('Coluna 3:') 
print('Media:',dataset['Monetary'].mean())
print(dataset[['Monetary']] < dataset[['Monetary']].mean())
print('Coluna 4:') 
print('Media:',dataset['Time'].mean())
print(dataset[['Time']] < dataset[['Time']].mean())
#print('Coluna 5:') 
#print('Media:',dataset['donatedBlood'].mean())
#print(dataset[['donatedBlood']] < dataset[['donatedBlood']].mean())


print('____Coluna com valores abaixo da Media:_____')
print('Coluna 1:') 
print('Media:',dataset['Recency'].mean())
print(dataset[['Recency']] > dataset[['Recency']].mean())
print('Coluna 2:') 
print('Media:',dataset['Frequency'].mean())
print(dataset[['Frequency']] > dataset[['Frequency']].mean()) 
print('Coluna 3:') 
print('Media:',dataset['Monetary'].mean())
print(dataset[['Monetary']] > dataset[['Monetary']].mean())
print('Coluna 4:') 
print('Media:',dataset['Time'].mean())
print(dataset[['Time']] > dataset[['Time']].mean())
#print('Coluna 5:') 
#print('Media:',dataset['donatedBlood'].mean())
#print(dataset[['donatedBlood']] > dataset[['donatedBlood']].mean())
