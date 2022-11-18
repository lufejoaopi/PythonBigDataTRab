import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


dataset = pd.read_csv(
    'iris.data' 
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

#s1 = s1.style.highlight_max(color = 'lightgreen', axis = 0)
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

#print('min da coluna 1:\n ',dataset['Sepallength'].min())
print('______Tabela Odenada de Forma Ascendente_______')
print(dataset.sort_values('Sepallength'))
print('______Tabela Ordenada de Forma Descendente_______')
print(dataset.sort_values('Sepallength', ascending=False))

print(dataset['Sepallength'].describe())

print('____Coluna com valores abaixo da Media:_____')
print('Coluna 1:') 
print(dataset[['Sepallength']] < dataset[['Sepallength']].mean())
print('Coluna 2:') 
print(dataset[['SepalWidth']] < dataset[['SepalWidth']].mean()) 
print('Coluna 3:') 
print(dataset[['PetalLength']] < dataset[['PetalLength']].mean())
print('Coluna 4:') 
print(dataset[['PetalWidth']] < dataset[['PetalWidth']].mean())

print('_____Coluna com valores acima da Media:_____')
print('Coluna 1:') 
print(dataset[['Sepallength']] > dataset[['Sepallength']].mean())
print('Coluna 2:') 
print(dataset[['SepalWidth']] > dataset[['SepalWidth']].mean())
print('Coluna 3:') 
print(dataset[['PetalLength']] > dataset[['PetalLength']].mean())
print('Coluna 4:') 
print(dataset[['PetalWidth']] > dataset[['PetalWidth']].mean())





