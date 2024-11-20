import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from ucimlrepo import fetch_ucirepo

# Carregar o dataset "Productivity Prediction of Garment Employees" da UCI
dataset = fetch_ucirepo(id=597)

# Acessando os dados
df = dataset.data.features
df['target'] = dataset.data.targets  # Verificando se há as variáveis alvo necessárias

# Inspecionando as primeiras linhas do dataframe
df.head()

# Verificar o tamanho do dataset
print(f'O dataset contém {df.shape[0]} linhas e {df.shape[1]} colunas')

# Exibir estatísticas descritivas
df.describe()

# Verificar tipos de dados e valores nulos
df.info()

# Contar quantos valores nulos existem em cada coluna
print(df.isnull().sum())

# Selecionar apenas as colunas numéricas
numeric_cols = df.select_dtypes(include=[np.number]).columns

# Preencher os valores ausentes nas colunas numéricas com a mediana
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Verificar se ainda há valores nulos em todo o dataframe
print(df.isnull().sum())

# Remoção de outliers usando o IQR (Intervalo Interquartil)

# Selecionar apenas as colunas numéricas
numeric_cols = df.select_dtypes(include=[np.number])

# Calcular os quantis e o IQR (Intervalo Interquartil)
Q1 = numeric_cols.quantile(0.25)
Q3 = numeric_cols.quantile(0.75)
IQR = Q3 - Q1

# Definir os limites para outliers (1.5 vezes o IQR)
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remover os outliers das colunas numéricas
df_cleaned = df[~((numeric_cols < lower_bound) | (numeric_cols > upper_bound)).any(axis=1)]

# Comparar o tamanho do dataframe original com o dataframe limpo
print(f"Tamanho original: {df.shape}")
print(f"Tamanho após remoção de outliers: {df_cleaned.shape}")

# Codificação de variáveis categóricas preservando todas as categorias
df_encoded = pd.get_dummies(df_cleaned, columns=['department', 'day'], drop_first=True)

# Verificando as novas colunas
df_encoded.head(10)

# Definir as colunas numéricas que precisam ser normalizadas
numeric_columns = ['targeted_productivity', 'smv', 'wip', 'over_time', 'incentive', 'idle_time', 'idle_men', 'no_of_style_change', 'no_of_workers']
# Aplicar normalização
scaler = StandardScaler()
df_encoded[numeric_columns] = scaler.fit_transform(df_encoded[numeric_columns])

# Verificar como ficaram os dados normalizados
df_encoded.head()

# Gráfico de distribuição
# Selecionar apenas as colunas numéricas para o cálculo da correlação
numeric_df = df_encoded.select_dtypes(include=[np.number])

# Criar o heatmap com as colunas numéricas
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.show()

sns.pairplot(df_encoded, diag_kind='kde')  # 'kde' usa Kernel Density Estimate na diagonal para a distribuição
plt.show()
