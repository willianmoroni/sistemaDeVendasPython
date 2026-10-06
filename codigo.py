# Título - Sistema de Vendas
# Seção cadastrar venda
    # Campo Data
    # Campo Vendedor - Ana, Bruno, Carla
    # Campo Produto - Notebook, Celular, Fone
    # Campo Quantidade
    # Campo Valor
    # Botão cadastrar
        # Ao cadastrar uma venda, ela deverá ser atualizada na tabela
        # Todo o dashboard deverá ser atualizado também

# Seção vendas cadastradas
    # Tabela com as vendas

# Seção dashboard
    # Card/Métrica -> Faturamento total.
    # Gráfico Barra/Coluna venda por vendedor.
    # Gráfico de Pizza -> Venda por produto.

import streamlit as st
import pandas as pd
import plotly.express as px

st.write("# Sistema de Vendas Barbearia")

# Carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

# seção de cadastro de vendas
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data", min_value="today", max_value="today")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

# Lógica de cadastro
if botao_cadastrar:
    if valor <= 0 or quantidade <= 0:
        st.warning("Valor Vazio!")
    else:    
        nova_venda = [str(data), vendedor, produto, quantidade, valor]
        ultima_linha = len(tabela_vendas) #Esta função vai pegar o tamanho total da tabela
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv("vendas.csv", index=False)
        st.success("Venda Cadastrada!")

# seção de visualizar vendas
st.write("## Vendas Cadastradas")
st.data_editor(tabela_vendas)

# dashboard
st.write("## Dashboard")

# Card/Métrica -> Faturamento total.
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}")

# Gráfico Barra/Coluna venda por vendedor.
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

# Gráfico de Pizza -> Venda por produto.
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.60)
st.plotly_chart(grafico2)
