# Durante o ano de 2025, qual tipo descarregou mais no porto?
#  %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('base/base_logistico.csv', sep=';')

def type_load(type: str, option: str):
    df['Tipo'] = df['Tipo'].astype(str)
    df_tipo = df[df['Tipo'] == type]

    if option == "contagem":
        return (df_tipo['Tipo'].count() / df['Tipo'].count()) * 100
    else:
        return df_tipo

resultados = pd.DataFrame({
    'tipos': ['Granel Sólido', 'Granel Líquidos', 'Container', 'Isotank'],
    'porcentagem': [type_load('Granel Líquido'), type_load('Granel Sólido'), type_load('Container'), type_load('Isotank')]
}).sort_values(by='porcentagem', ascending=False)

sns.barplot(resultados, y='tipos', x='porcentagem')
plt.xlabel('Porcentagem (%)')
plt.ylabel('Tipos')
plt.title('Porcentagem de tipos de cargas')