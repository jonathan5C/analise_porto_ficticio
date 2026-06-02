# Qual mês o Isotank teve maior descarga no porto?
#  %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('base/base_logistico.csv', sep=';')
df['mes'] = pd.to_datetime(df['Data'])

isotank = type_load('Isotank', '')
summary_isotank = isotank.groupby(by=['mes'], as_index=False)[['Tipo']].count()
summary_isotank = summary_isotank.sort_values(by='Tipo', ascending=False)

sns.barplot(summary_isotank, x='mes', y='Tipo')
plt.xlabel('Mês')
plt.ylabel('Quantidade')
plt.title('Quantidade de descarga do modal Isotank')