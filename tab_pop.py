import plotly.graph_objects as go

# Dados de exemplo para a tabela
dados_bairros = {
    'PARAÍSO': {'População Total': 25314, 'Homens': 12583, 'Mulheres': 12731},
    'BOA VISTA': {'População Total': 22671, 'Homens': 10859, 'Mulheres': 11812},
    'MORUMBI': {'População Total': 17447, 'Homens': 8521, 'Mulheres': 8926},
    # Adicione mais bairros conforme necessário
}

# Criar a tabela interativa
fig = go.Figure(data=[go.Table(
    header=dict(values=['Bairro', 'População Total &#9794;&#9792;', 'Homens &#9794;', 'Mulheres &#9792;']),
    cells=dict(values=[
        [bairro for bairro in dados_bairros.keys()],
        [f"{dados['População Total']} &#9794;&#9792;" for dados in dados_bairros.values()],
        [f"{dados['Homens']} &#9794;" for dados in dados_bairros.values()],
        [f"{dados['Mulheres']} &#9792;" for dados in dados_bairros.values()]
    ])
)])

# Adicionar título
fig.update_layout(title='Dados Populacionais por Bairro')

# Exibir a tabela interativa
fig.show()

# Salvar como imagem (PNG)
fig.write_image("tabela_populacional.png")

# Salvar como HTML
fig.write_html("tabela_populacional.html")