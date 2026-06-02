# Que tipo de modal descarregou mais no 2º trimestre de 2025? (Abril - Junho)
#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('base/base_logistico.csv', sep=';')

df['mes'] = pd.to_datetime(df['Data'])
df['mes'] = df['mes'].dt.month
filtro_mes_04 = df['mes'] == 4
filtro_mes_05 = df['mes'] == 5
filtro_mes_06 = df['mes'] == 6
df_mes_04 = df[filtro_mes_04]
df_mes_05 = df[filtro_mes_05]
df_mes_06 = df[filtro_mes_06]

dfs = [df_mes_04, df_mes_05, df_mes_06]
segundo_trimestre = pd.concat(dfs)

summary_trimestre = segundo_trimestre.groupby(by=['Modal'], as_index=False)[['Data']].count()
summary_trimestre.columns = ['Modal', 'Quantidade']
summary_trimestre = summary_trimestre.sort_values(by='Quantidade', ascending=False)

sns.barplot(summary_trimestre, x=summary_trimestre['Modal'], y=summary_trimestre['Quantidade'])
plt.xlabel('Modal')
plt.ylabel('Quantidade')
plt.title('Descarga dos modais no 2º trimestre de 2025')