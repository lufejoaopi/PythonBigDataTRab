import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt 
import numpy as np


dataset = pd.read_csv(
    'iris.data' 
)

#print('comprimento da sepala')

dataset.head()

print(dataset)
print("Tipo de dado de cada coluna")
mostra = dataset.dtypes 
print(mostra)

print('mostra cada atributo das colunas')
coluna = list(dataset.columns)
print (coluna)


print( '__Media das Colunas__')
print('Media da coluna 1\n ', dataset['Sepallength'].mean())
print('Media da coluna 2\n ', dataset['SepalWidth'].mean())
print('Media da coluna 3\n ', dataset['PetalLength'].mean())
print('Media da coluna 4\n ', dataset['PetalWidth'].mean())


print('___Desvio Padrao___')
print('Desvio da coluna 1:\n ',dataset['Sepallength'].std())
print('Desvio da coluna 2:\n ',dataset['SepalWidth'].std())
print('Desvio da coluna 3:\n ',dataset['PetalLength'].std())
print('Desvio da coluna 4:\n ',dataset['PetalWidth'].std())

print('_______Moda_______')
print('moda da coluna 1:\n ',dataset['Sepallength'].mode())
print('moda da coluna 2:\n ',dataset['SepalWidth'].mode())
print('moda da coluna 3:\n ',dataset['PetalLength'].mode())
print('moda da coluna 4:\n ',dataset['PetalWidth'].mode())

print('_______Mediana_______')
print('mediana da coluna 1:\n ',dataset['Sepallength'].median())
print('mediana da coluna 2:\n ',dataset['SepalWidth'].median())
print('mediana da coluna 3:\n ',dataset['PetalLength'].median())
print('mediana da coluna 4:\n ',dataset['PetalWidth'].median())

print('_______Valor_Maximo_______')
print('max da coluna 1:\n ',dataset['Sepallength'].max())
print('max da coluna 2:\n ',dataset['SepalWidth'].max())
print('max da coluna 3:\n ',dataset['PetalLength'].max())
print('max da coluna 4:\n ',dataset['PetalWidth'].max())

print('_______Valor_Minimo_______')
print('min da coluna 1:\n ',dataset['Sepallength'].min())
print('min da coluna 2:\n ',dataset['SepalWidth'].min())
print('min da coluna 3:\n ',dataset['PetalLength'].min())
print('min da coluna 4:\n ',dataset['PetalWidth'].min())

print('______Tabela Odenada de Forma Ascendente_______')
print(dataset.sort_values('Sepallength'))
print('______Tabela Ordenada de Forma Descendente_______')
print(dataset.sort_values('Sepallength', ascending=False))

print(dataset['Sepallength'].describe())

print('____Coluna com valores abaixo da Media:_____') 
print('Coluna 1:')
print('Media:',dataset['Sepallength'].mean()) 
print(dataset[['Sepallength']] < dataset[['Sepallength']].mean())
print('Coluna 2:')
print('Media:',dataset['SepalWidth'].mean())  
print(dataset[['SepalWidth']] < dataset[['SepalWidth']].mean()) 
print('Coluna 3:') 
print('Media:',dataset['PetalLength'].mean())
print(dataset[['PetalLength']] < dataset[['PetalLength']].mean())
print('Coluna 4:') 
print('Media:',dataset['PetalWidth'].mean())
print(dataset[['PetalWidth']] < dataset[['PetalWidth']].mean())

print('_____Coluna com valores acima da Media:_____')
print('Coluna 1:')
print('Media:',dataset['Sepallength'].mean()) 
print(dataset[['Sepallength']] > dataset[['Sepallength']].mean())
print('Coluna 2:')
print('Media:',dataset['SepalWidth'].mean())  
print(dataset[['SepalWidth']] > dataset[['SepalWidth']].mean())
print('Coluna 3:')
print('Media:',dataset['PetalLength'].mean())  
print(dataset[['PetalLength']] > dataset[['PetalLength']].mean())
print('Coluna 4:') 
print('Media:',dataset['PetalWidth'].mean()) 
print(dataset[['PetalWidth']] > dataset[['PetalWidth']].mean())


cols = ['Sepallength','SepalWidth','PetalLength','PetalWidth']
dataset.rename(columns={cols[0]:0, cols[1]:1, cols[2]:2, cols[3]:3},inplace = True)
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
