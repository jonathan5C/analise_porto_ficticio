# Qual modal foi mais utilizado durante 2025?

#%%
import pandas as pd
import plotly.express as px

df = pd.read_csv('base/base_logistico.csv', sep=';')
df

modal = df.groupby(by=['Modal'], as_index=False)[['Data']].count()
modal = modal.sort_values(by='Data', ascending=False)

modal.columns = ['Modal', 'Quantidade']
modal

fig = px.bar(modal, x=modal['Modal'], y=modal['Quantidade'], text_auto=True, title="Quantidade por Modal")
fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
fig