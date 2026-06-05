# Quantas operações foram registradas por mês ao longo de 2025?

#%%
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('base/base_logistico.csv', sep=';')

df['Data'] = pd.to_datetime(df['Data'])
df['Mês'] = df['Data'].dt.month

def month_name(x):
    match x:
        case 1:
            return 'Janeiro'
        case 2:
            return 'Fevereiro'
        case 3:
            return 'Março'
        case 4:
            return 'Abril'
        case 5:
            return 'Maio'
        case 6:
            return 'Junho'
        case 7:
            return 'Julho'
        case 8:
            return 'Agosto'
        case 9:
            return 'Setembro'
        case 10:
            return 'Outubro'
        case 11:
            return 'Novembro'
        case 12:
            return 'Dezembro'

df['Mês'] = df['Mês'].apply(month_name)

df_meses = df.groupby(by=['Mês'], as_index=False)[['Data']].count()

df_meses = df_meses.sort_values(by='Data').reset_index(drop=True)

ordem_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
               'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
df_meses['Mês'] = pd.Categorical(df_meses['Mês'], categories=ordem_meses, ordered=True)
df_meses = df_meses.sort_values('Mês').reset_index(drop=True)
df_meses.columns = ['Mês', 'Quantidade']

figura = go.Figure(
    go.Bar(
        x=df_meses['Mês'],
        y=df_meses['Quantidade'],
        text=df_meses['Quantidade'],
        textposition='auto' 
    )
)
figura.update_layout(title_text='Operações entre os meses')
figura.update_xaxes(title_text='Meses')
figura.update_yaxes(title_text='Quantidade')
figura