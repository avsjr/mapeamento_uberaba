import plotly.graph_objects as go
import pandas as pd

# Carregar os dados dos bairros
dados_bairros = pd.read_excel('c:/Users/avsj/iCloudDrive/01.Antonio/01.Projetos/01.github/mapeamento_uberaba/files/03.IBGE/UPG_UBERABA.xlsx')

#POPULACAO_TOTAL = dados_bairros['POPULACAO_TOTAL']

# Criar a tabela interativa
fig = go.Figure(data=[go.Table(
    header=dict(values=['Bairro', 'População Total &#9794;&#9792;', 'Homens &#9794;', 'Mulheres &#9792;']),
    cells=dict(values=[
        [bairro for bairro in dados_bairros['UPG']],
        [f"{populacao} &#9794;&#9792;" for populacao in dados_bairros['POPULACAO_TOTAL']],
        [f"{homens} &#9794;" for homens in dados_bairros['HOMENS']],
        [f"{mulheres} &#9792;" for mulheres in dados_bairros['MULHERES']]
    ])
)])

# Adicionar título
fig.update_layout(title='Dados Populacionais por Bairro')

# Exibir a tabela interativa
#fig.show()

# Salvar como imagem (PNG)
#fig.write_image("tabela_populacional.png")

# Salvar como HTML
fig.write_html("tabela_populacional.html")