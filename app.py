import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o CSV
df = pd.read_csv('dadosarvores.csv')

# Título principal
st.title('Desempenho AVL x Rubro-Negra - Estrutura de Dados 2')

# Seleção de estado do vetor
estado = st.radio(
    "Selecione o estado do vetor:",
    ('Ordenado', 'Desordenado')
)

# Filtragem para a métrica de Segundos
df_segundos = df[df['Métrica'] == 'Segundos'][['Árvore', estado]]

# Gráfico de barras para Segundos
fig_segundos = px.bar(df_segundos, x='Árvore', y=estado, color='Árvore',
                      labels={'value': 'Tempo (s)', estado: 'Tempo (s)'},
                      title=f'Comparação de Tempo em Segundos ({estado})')

# Exibir gráfico de Segundos
st.plotly_chart(fig_segundos)

# Filtragem para a métrica de Microssegundos
df_microssegundos = df[df['Métrica'] == 'Microssegundos'][['Árvore', estado]]

# Gráfico de barras para Microssegundos
fig_microssegundos = px.bar(df_microssegundos, x='Árvore', y=estado, color='Árvore',
                            labels={'value': 'Tempo (µs)', estado: 'Tempo (µs)'},
                            title=f'Comparação de Tempo em Microssegundos ({estado})')

# Exibir gráfico de Microssegundos
st.plotly_chart(fig_microssegundos)


# Rodapé
st.markdown("""
**INSTITUTO FEDERAL DE SÃO PAULO – IFSP 💚🤍**

**ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - Estrutura de Dados 2**

Caio Dib Laronga  
Domenico Kenjy Rizzo  
Gabriela Santana Camilo  
Isabella Urdiali Miranda  
Pedro Henrique Ramos Lauton
""")
