# %%
import pandas as pd

# %%

df = pd.read_csv('base/base_logistico.csv', sep=';')
# %%

def type_load(type: str, option: str):
    df['Tipo'] = df['Tipo'].astype(str)
    df_tipo = df[df['Tipo'] == type]

    if option == "contagem":
        return (df_tipo['Tipo'].count() / df['Tipo'].count()) * 100
    else:
        return df_tipo
# %%

import matplotlib.pyplot as plt
import seaborn as sns
# %%

resultados = pd.DataFrame({
    'tipos': ['Granel Sólido', 'Granel Líquidos', 'Container', 'Isotank'],
    'porcentagem': [type_load('Granel Líquido'), type_load('Granel Sólido'), type_load('Container'), type_load('Isotank')]
}).sort_values(by='porcentagem', ascending=False)
#%%

sns.barplot(resultados, y='tipos', x='porcentagem')
plt.xlabel('Porcentagem (%)')
plt.ylabel('Tipos')
plt.title('Porcentagem de tipos de cargas')
# %%
# Que tipo de modal descarregou mais no 2º trimestre de 2025? (Abril - Junho)

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
# %%
# Qual mês o Isotank teve maior descarga no porto?

isotank = type_load('Isotank', '')
summary_isotank = isotank.groupby(by=['mes'], as_index=False)[['Tipo']].count()
summary_isotank = summary_isotank.sort_values(by='Tipo', ascending=False)

#%%

soma_isotank = summary_isotank['Tipo'].sum()
diff = 14 / soma_isotank
diff * 100
# %%

sns.barplot(summary_isotank, x='mes', y='Tipo')
plt.xlabel('Mês')
plt.ylabel('Quantidade')
plt.title('Quantidade de descarga do modal Isotank')