import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


dataset = pd.read_csv(
    '/home/joao/sql/transfusion.data' 
)

#print('comprimento da sepala')
#indices de tipo inteiro
#s1 = pd.Series([1, 3, 4, 5, np.nan, 7, 8])
#s1 = pd.DataFrame(np.random.randn(6, 4), columns=list("ABCD"))
dataset.head()
#print(s1)
print(dataset)
print("Tipo de dado de cada coluna")
mostra = dataset.dtypes 
print(mostra)
#s1 = df['Sepal length'].mean()
print('mostra cada atributo das colunas')
coluna = list(dataset.columns)
print (coluna)

input("Aperte <enter> para continuar")

#s1 = s1.style.highlight_max(color = 'lightgreen', axis = 0)
print( '__Media das Colunas__')
print('Media da coluna 1\n ', dataset['Recency'].mean())
print('Media da coluna 2\n ', dataset['Frequency'].mean())
print('Media da coluna 3\n ', dataset['Monetary'].mean())
print('Media da coluna 4\n ', dataset['Time'].mean())
#print('Media da coluna 5\n ', dataset['donatedBlood'].mean())


print('___Desvio Padrao___')
print('Desvio padrão da coluna 1\n ', dataset['Recency'].std())
print('Desvio padrão da coluna 2\n ', dataset['Frequency'].std())
print('Desvio padrão da coluna 3\n ', dataset['Monetary'].std())
print('Desvio padrão da coluna 4\n ', dataset['Time'].std())
#print('Desvio padrão da coluna 5\n ', dataset['donatedBlood'].std())

print('_______Moda_______')
print('Moda da coluna 1\n ', dataset['Recency'].mode())
print('Moda da coluna 2\n ', dataset['Frequency'].mode())
print('Moda da coluna 3\n ', dataset['Monetary'].mode())
print('Moda da coluna 4\n ', dataset['Time'].mode())
#print('Moda da coluna 5\n ', dataset['donatedBlood'].mode())

print('_______Mediana_______')
print('Mediana da coluna 1\n ', dataset['Recency'].median())
print('Mediana da coluna 2\n ', dataset['Frequency'].median())
print('Mediana da coluna 3\n ', dataset['Monetary'].median())
print('Mediana da coluna 4\n ', dataset['Time'].median())
#print('Mediana da coluna 5\n ', dataset['donatedBlood'].median())


print('_______Valor_Maximo_______')
print('Max da coluna 1\n ', dataset['Recency'].max())
print('Max da coluna 2\n ', dataset['Frequency'].max())
print('Max da coluna 3\n ', dataset['Monetary'].max())
print('Max da coluna 4\n ', dataset['Time'].max())
#print('Max da coluna 5\n ', dataset['donatedBlood'].max())

print('_______Valor_Minimo_______')
print('Min da coluna 1\n ', dataset['Recency'].min())
print('Min da coluna 2\n ', dataset['Frequency'].min())
print('Min da coluna 3\n ', dataset['Monetary'].min())
print('Min da coluna 4\n ', dataset['Time'].min())
#print('Min da coluna 5\n ', dataset['donatedBlood'].min())


input("Aperte <enter> para continuar")

#print('min da coluna 1:\n ',dataset['Sepallength'].min())
print('______Tabela Odenada de Forma Ascendente_______')
print(dataset.sort_values('Monetary'))
print('______Tabela Ordenada de Forma Descendente_______')
print(dataset.sort_values('Monetary', ascending=False))

print(dataset['Monetary'].describe())

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


print('____Coluna com valores acima da Media:_____')
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
