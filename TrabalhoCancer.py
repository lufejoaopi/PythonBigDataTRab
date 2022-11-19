import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


dataset = pd.read_csv('breast-cancer-wisconsin.data')

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
#print('Media da coluna 1\n ', dataset['Class-Name'].mean())
#print('Media da coluna 1\n ', dataset['CodeNumber'].mean())
print('Media da coluna 2\n ', dataset['ClumpThickness'].mean())
print('Media da coluna 3\n ', dataset['CellSize'].mean())
print('Media da coluna 4\n ', dataset['CellShape'].mean())
print('Media da coluna 5\n ', dataset['MarginalAdhesion'].mean())
print('Media da coluna 6\n ', dataset['SingleEpithelial'].mean())
#print('Media da coluna 7\n ', dataset['BareNuclei'].mean())
print('Media da coluna 8\n ', dataset['BlandChromatin'].mean())
print('Media da coluna 9\n ', dataset['NormalNucleoli'].mean())
print('Media da coluna 10\n ', dataset['Mitoses'].mean())
print('Media da coluna 11\n ', dataset['Class'].mean())

#print('Media da coluna 5\n ', dataset['donatedBlood'].mean())


print('___Desvio Padrao___')
print('Desvio padrão da coluna 2\n ', dataset['ClumpThickness'].std())
print('Desvio padrão da coluna 3\n ', dataset['CellSize'].std())
print('Desvio padrão da coluna 4\n ', dataset['CellShape'].std())
print('Desvio padrão da coluna 5\n ', dataset['MarginalAdhesion'].std())
print('Desvio padrão da coluna 6\n ', dataset['SingleEpithelial'].std())
print('Desvio padrão da coluna 8\n ', dataset['BlandChromatin'].std())
print('Desvio padrão da coluna 9\n ', dataset['NormalNucleoli'].std())
print('Desvio padrão da coluna 10\n ', dataset['Mitoses'].std())
print('Desvio padrão da coluna 11\n ', dataset['Class'].std())
#print('Desvio padrão da coluna 5\n ', dataset['donatedBlood'].std())

print('_______Moda_______')
print('Moda da coluna 2\n ', dataset['ClumpThickness'].mode())
print('Moda da coluna 3\n ', dataset['CellSize'].mode())
print('Moda da coluna 4\n ', dataset['CellShape'].mode())
print('Moda da coluna 5\n ', dataset['MarginalAdhesion'].mode())
print('Moda da coluna 6\n ', dataset['SingleEpithelial'].mode())
print('Moda da coluna 8\n ', dataset['BlandChromatin'].mode())
print('Moda da coluna 9\n ', dataset['NormalNucleoli'].mode())
print('Moda da coluna 10\n ', dataset['Mitoses'].mode())
print('Moda da coluna 11\n ', dataset['Class'].mode())
#print('Moda da coluna 5\n ', dataset['donatedBlood'].mode())

print('_______Mediana_______')
print('Mediana da coluna 2\n ', dataset['ClumpThickness'].median())
print('Mediana da coluna 3\n ', dataset['CellSize'].median())
print('Mediana da coluna 4\n ', dataset['CellShape'].median())
print('Mediana da coluna 5\n ', dataset['MarginalAdhesion'].median())
print('Mediana da coluna 6\n ', dataset['SingleEpithelial'].median())
print('Mediana da coluna 8\n ', dataset['BlandChromatin'].median())
print('Mediana da coluna 9\n ', dataset['NormalNucleoli'].median())
print('Mediana da coluna 10\n ', dataset['Mitoses'].median())
print('Mediana da coluna 11\n ', dataset['Class'].median())

#print('Mediana da coluna 5\n ', dataset['donatedBlood'].median())


print('_______Valor_Maximo_______')
print('Max da coluna 2\n ', dataset['ClumpThickness'].max())
print('Max da coluna 3\n ', dataset['CellSize'].max())
print('Max da coluna 4\n ', dataset['CellShape'].max())
print('Max da coluna 5\n ', dataset['MarginalAdhesion'].max())
print('Max da coluna 6\n ', dataset['SingleEpithelial'].max())
print('Max da coluna 8\n ', dataset['BlandChromatin'].max())
print('Max da coluna 9\n ', dataset['NormalNucleoli'].max())
print('Max da coluna 10\n ', dataset['Mitoses'].max())
print('Max da coluna 11\n ', dataset['Class'].max())

#print('Max da coluna 5\n ', dataset['donatedBlood'].max())

print('_______Valor_Minimo_______')
print('Min da coluna 2\n ', dataset['ClumpThickness'].min())
print('Min da coluna 3\n ', dataset['CellSize'].min())
print('Min da coluna 4\n ', dataset['CellShape'].min())
print('Min da coluna 5\n ', dataset['MarginalAdhesion'].min())
print('Min da coluna 6\n ', dataset['SingleEpithelial'].min())
print('Min da coluna 8\n ', dataset['BlandChromatin'].min())
print('Min da coluna 9\n ', dataset['NormalNucleoli'].min())
print('Min da coluna 10\n ', dataset['Mitoses'].min())
print('Min da coluna 11\n ', dataset['Class'].min())

#print('Min da coluna 5\n ', dataset['donatedBlood'].min())


input("Aperte <enter> para continuar")

#print('min da coluna 1:\n ',dataset['Sepallength'].min())
print('______Tabela Odenada de Forma Ascendente_______')
print(dataset.sort_values('CodeNumber'))
print('______Tabela Ordenada de Forma Descendente_______')
print(dataset.sort_values('CodeNumber', ascending=False))

print(dataset['CodeNumber'].describe())

input("Aperte <enter> para continuar")

print('____Coluna com valores abaixo da Media:_____')
print('Coluna 2:') 
print('Media:',dataset['ClumpThickness'].mean())
print(dataset[['ClumpThickness']] < dataset[['ClumpThickness']].mean()) 
print('Coluna 3:') 
print('Media:',dataset['CellSize'].mean())
print(dataset[['CellSize']] < dataset[['CellSize']].mean())
print('Coluna 4:') 
print('Media:',dataset['CellShape'].mean())
print(dataset[['CellShape']] < dataset[['CellShape']].mean())
print('Coluna 5:') 
print('Media:',dataset['MarginalAdhesion'].mean())
print(dataset[['MarginalAdhesion']] < dataset[['MarginalAdhesion']].mean())
print('Coluna 6:') 
print('Media:',dataset['SingleEpithelial'].mean())
print(dataset[['SingleEpithelial']] < dataset[['SingleEpithelial']].mean()) 
print('Coluna 8:') 
print('Media:',dataset['BlandChromatin'].mean())
print(dataset[['BlandChromatin']] < dataset[['BlandChromatin']].mean())
print('Coluna 9:') 
print('Media:',dataset['NormalNucleoli'].mean())
print(dataset[['NormalNucleoli']] < dataset[['NormalNucleoli']].mean())
print('Coluna 10:') 
print('Media:',dataset['Mitoses'].mean())
print(dataset[['Mitoses']] < dataset[['Mitoses']].mean())
print('Coluna 11:') 
print('Media:',dataset['Class'].mean())
print(dataset[['Class']] < dataset[['Class']].mean())

#print('Coluna 5:') 
#print('Media:',dataset['donatedBlood'].mean())
#print(dataset[['donatedBlood']] < dataset[['donatedBlood']].mean())


print('____Coluna com valores acima da Media:_____')
print('Coluna 2:') 
print('Media:',dataset['ClumpThickness'].mean())
print(dataset[['ClumpThickness']] > dataset[['ClumpThickness']].mean()) 
print('Coluna 3:') 
print('Media:',dataset['CellSize'].mean())
print(dataset[['CellSize']] > dataset[['CellSize']].mean())
print('Coluna 4:') 
print('Media:',dataset['CellShape'].mean())
print(dataset[['CellShape']] > dataset[['CellShape']].mean())
print('Coluna 5:') 
print('Media:',dataset['MarginalAdhesion'].mean())
print(dataset[['MarginalAdhesion']] > dataset[['MarginalAdhesion']].mean())
print('Coluna 6:') 
print('Media:',dataset['SingleEpithelial'].mean())
print(dataset[['SingleEpithelial']] > dataset[['SingleEpithelial']].mean()) 
print('Coluna 8:') 
print('Media:',dataset['BlandChromatin'].mean())
print(dataset[['BlandChromatin']] > dataset[['BlandChromatin']].mean())
print('Coluna 9:') 
print('Media:',dataset['NormalNucleoli'].mean())
print(dataset[['NormalNucleoli']] > dataset[['NormalNucleoli']].mean())
print('Coluna 10:') 
print('Media:',dataset['Mitoses'].mean())
print(dataset[['Mitoses']] > dataset[['Mitoses']].mean())
print('Coluna 11:') 
print('Media:',dataset['Class'].mean())
print(dataset[['Class']] > dataset[['Class']].mean())
