import plotly.graph_objects as go
import pandas as pd

# Carregue os dados
dados_piramide = pd.read_excel('c:/Users/avsj/iCloudDrive/01.Antonio/01.Projetos/01.github/mapeamento_uberaba/files/03.IBGE/Censo 2022 - Pirâmide etária - Uberaba (MG).xlsx')

grupos_idade = dados_piramide['Grupo de idade']

pop_feminina = dados_piramide['População feminina']

pop_masculina = dados_piramide['População masculina']

# Cores das barras
COR_FEM = '#FFB6C1'  # Rosa claro
COR_MASC = '#ADD8E6'  # Azul claro

# Crie o gráfico de pirâmide
fig = go.Figure()

# Adicione barras para a população feminina
fig.add_trace(go.Bar(
    y=grupos_idade,
    x=pop_feminina,
    orientation='h',
    marker=dict(color=COR_FEM),
    name='Feminino',
    hovertemplate='%{y}<br>Mulheres: %{x}'
))

# Adicione barras para a população masculina com offset positivo
fig.add_trace(go.Bar(
    y=grupos_idade,
    x=pop_masculina * -1,  # valores negativos para inverter a direção
    orientation='h',
    marker=dict(color=COR_MASC),
    name='Masculino',
    hovertemplate='%{y}<br>Homens: %{x}'
))

# Ajuste de layout
fig.update_layout(
    barmode='overlay',
    xaxis=dict(visible=False),
    #yaxis=dict(title='Grupo de Idade'),
    title='Distribuição da População por Idade e Gênero',
    legend=dict(x=0, y=1),
    plot_bgcolor='white',  # Remova o fundo azul
)

# Salve o gráfico como HTML
fig.write_html('piramide_etaria.html')
