import plotly.graph_objects as go
import pandas as pd

# Carregar os dados dos bairros
dados_bairros = pd.read_excel('c:/Users/avsj/iCloudDrive/01.Antonio/01.Projetos/01.github/mapeamento_uberaba/files/03.IBGE/UPG_UBERABA.xlsx')

# Definir o tamanho da fonte para o cabeçalho
font_size_header = "16px"

# Criar a tabela interativa
fig = go.Figure(data=[go.Table(
    header=dict(values=[
        'Bairro</span>',
        'Total 🚹🚺</span>',
        'Homens 🚹</span>',
        'Mulheres 🚺</span>'
    ]),
    cells=dict(values=[
        [f"{bairro}"for bairro in dados_bairros['UPG']],
        [f"{populacao} " for populacao in dados_bairros['POPULACAO_TOTAL']],
        [f"{homens} " for homens in dados_bairros['HOMENS']],
        [f"{mulheres} " for mulheres in dados_bairros['MULHERES']]
    ])
)])

# Adicionar título
fig.update_layout(title='População por Bairro')

# Salvar como HTML
fig.write_html("tabela_populacao.html")