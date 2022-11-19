import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


dataset = pd.read_csv(
    'balance-scale.data' 
)

print(dataset)
print("Tipo de dado de cada coluna")
mostra = dataset.dtypes 
print(mostra)
print('mostra cada atributo das colunas')
coluna = list(dataset.columns)
print (coluna)

input("Aperte <enter> para continuar")

print( '__Media das Colunas__')
#print('Media da coluna 1\n ', dataset['Class-Name'].mean())
print('Media da coluna 2\n ', dataset['Left-Weight'].mean())
print('Media da coluna 3\n ', dataset['Left-Distance'].mean())
print('Media da coluna 4\n ', dataset['Right-Weight'].mean())
print('Media da coluna 5\n ', dataset['Right-Distance'].mean())

print('___Desvio Padrao___')
print('Desvio padrão da coluna 2\n ', dataset['Left-Weight'].std())
print('Desvio padrão da coluna 3\n ', dataset['Left-Distance'].std())
print('Desvio padrão da coluna 4\n ', dataset['Right-Weight'].std())
print('Desvio padrão da coluna 5\n ', dataset['Right-Distance'].std())

print('_______Moda_______')
print('Moda da coluna 2\n ', dataset['Left-Weight'].mode())
print('Moda da coluna 3\n ', dataset['Left-Distance'].mode())
print('Moda da coluna 4\n ', dataset['Right-Weight'].mode())
print('Moda da coluna 5\n ', dataset['Right-Distance'].mode())

print('_______Mediana_______')
print('Mediana da coluna 2\n ', dataset['Left-Weight'].median())
print('Mediana da coluna 3\n ', dataset['Left-Distance'].median())
print('Mediana da coluna 4\n ', dataset['Right-Weight'].median())
print('Mediana da coluna 5\n ', dataset['Right-Distance'].median())

print('_______Valor_Maximo_______')
print('Max da coluna 2\n ', dataset['Left-Weight'].max())
print('Max da coluna 3\n ', dataset['Left-Distance'].max())
print('Max da coluna 4\n ', dataset['Right-Weight'].max())
print('Max da coluna 5\n ', dataset['Right-Distance'].max())

print('_______Valor_Minimo_______')
print('Min da coluna 2\n ', dataset['Left-Weight'].min())
print('Min da coluna 3\n ', dataset['Left-Distance'].min())
print('Min da coluna 4\n ', dataset['Right-Weight'].min())
print('Min da coluna 5\n ', dataset['Right-Distance'].min())


input("Aperte <enter> para continuar")

print('______Tabela Odenada de Forma Ascendente_______')
print(dataset.sort_values('Left-Weight'))
print('______Tabela Ordenada de Forma Descendente_______')
print(dataset.sort_values('Left-Weight', ascending=False))

print(dataset['Left-Weight'].describe())

input("Aperte <enter> para continuar")

print('____Coluna com valores abaixo da Media:_____')
print('Coluna 1:') 
print('Media:',dataset['Left-Weight'].mean())
print(dataset[['Left-Weight']] < dataset[['Left-Weight']].mean())
print('Coluna 2:') 
print('Media:',dataset['Left-Distance'].mean())
print(dataset[['Left-Distance']] < dataset[['Left-Distance']].mean()) 
print('Coluna 3:') 
print('Media:',dataset['Right-Weight'].mean())
print(dataset[['Right-Weight']] < dataset[['Right-Weight']].mean())
print('Coluna 4:') 
print('Media:',dataset['Right-Distance'].mean())
print(dataset[['Right-Distance']] < dataset[['Right-Distance']].mean())


print('____Coluna com valores acima da Media:_____')
print('Coluna 1:') 
print('Media:',dataset['Left-Weight'].mean())
print(dataset[['Left-Weight']] > dataset[['Left-Weight']].mean())
print('Coluna 2:') 
print('Media:',dataset['Left-Distance'].mean())
print(dataset[['Left-Distance']] > dataset[['Left-Distance']].mean()) 
print('Coluna 3:') 
print('Media:',dataset['Right-Weight'].mean())
print(dataset[['Right-Weight']] > dataset[['Right-Weight']].mean())
print('Coluna 4:') 
print('Media:',dataset['Right-Distance'].mean())
print(dataset[['Right-Distance']] > dataset[['Right-Distance']].mean())
