# Qual é o peso total (em toneladas) movimentado em cada tipo de carga?

#%%
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('base/base_logistico.csv', sep=';')
df

toneladas_tipo = df.groupby(by=['Tipo'], as_index=False)[['Peso_ton']].sum()
toneladas_tipo = toneladas_tipo.sort_values(by=['Peso_ton'], ascending=False)

fig = go.Figure(data=[go.Bar(
    x=toneladas_tipo['Tipo'],
    marker_color= '#3E5DBB',
    y=toneladas_tipo['Peso_ton'],
    text=toneladas_tipo['Peso_ton'],
    textposition='auto')])

fig.update_layout(title_text='Movimentação entre cargas')
fig.update_xaxes(title_text='Tipos')
fig.update_yaxes(title_text='Quantiade (ton)')
fig

# Descobrir o valor de representatividade do total do Granel Sólido em cima do todo
valor_granel_sólido = toneladas_tipo['Peso_ton'].iloc[0]
soma_total = toneladas_tipo['Peso_ton'].sum()
(valor_granel_sólido / soma_total) * 100

# Descobrir a diferença, em porcentagem, para o segundo colocado
valor_granel_liquido = toneladas_tipo['Peso_ton'].iloc[1]
(valor_granel_liquido * 100) / valor_granel_sólido