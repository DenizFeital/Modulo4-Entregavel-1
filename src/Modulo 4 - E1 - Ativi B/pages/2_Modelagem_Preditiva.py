# 2_Modelagem_Preditiva.py
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from data_generation import generate_data  # Carrega o dataset

# Configurações gerais
st.set_page_config(page_title='Modelagem Preditiva', layout='wide')
# Título do aplicativo
st.title('Modelagem Preditiva')

# ================================================
# 1. Carregar e Filtrar os Dados
# ================================================
st.header('1. Carregar e Filtrar os Dados')
# Carregar os dados gerados
df = generate_data()

# Garantir que a coluna 'date' seja removida, se existir
df = df.drop(columns=['date'], errors='ignore')  # Remover a coluna 'date', se presente

# Garantir que a coluna 'irrigation_time' seja removida, se existir
df = df.drop(columns=['irrigation_time'], errors='ignore')  # Remover a coluna 'irrigation_time', se presente

# ----------------------------------
# 1.1. Filtros na Barra Lateral
# ----------------------------------
st.sidebar.title('Filtros de Dados')
# Filtro para Nutriente
selected_nutrient = st.sidebar.multiselect(
    'Selecione o Nutriente:',
    options=df['nutrients'].unique(),
    default=df['nutrients'].unique()
)

# Filtros para variáveis numéricas
st.sidebar.subheader('Intervalos das Variáveis Numéricas')
# Temperatura
temp_min, temp_max = st.sidebar.slider(
    'Temperatura (°C):',
    min_value=float(df['temperature'].min()),
    max_value=float(df['temperature'].max()),
    value=(float(df['temperature'].min()), float(df['temperature'].max()))
)

# Umidade
umid_min, umid_max = st.sidebar.slider(
    'Umidade (%):',
    min_value=float(df['humidity'].min()),
    max_value=float(df['humidity'].max()),
    value=(float(df['humidity'].min()), float(df['humidity'].max()))
)

# ----------------------------------
# 1.2. Aplicar Filtros aos Dados
# ----------------------------------
# Aplicar os filtros selecionados ao DataFrame
df_filtered = df[
    (df['nutrients'].isin(selected_nutrient)) &
    (df['temperature'] >= temp_min) & (df['temperature'] <= temp_max) &
    (df['humidity'] >= umid_min) & (df['humidity'] <= umid_max)
]

# Verificar se o DataFrame filtrado não está vazio
if df_filtered.empty:
    st.warning('Nenhum dado corresponde aos filtros selecionados. Por favor, ajuste os filtros.')
    st.stop()
else:
    st.subheader('Dados Filtrados')
    st.dataframe(df_filtered.head())

# ================================================
# 2. Preparar os Dados para Modelagem
# ================================================
st.header('2. Preparar os Dados para Modelagem')
# Remover qualquer coluna indesejada, como 'date' e 'irrigation_time'
df_filtered = df_filtered.drop(columns=['date', 'irrigation_time'], errors='ignore')

# Garantir que a variável 'duration' (target) é numérica
df_filtered['duration'] = pd.to_numeric(df_filtered['duration'], errors='coerce')

# Transformar variáveis categóricas em variáveis dummies
df_ml = pd.get_dummies(df_filtered, columns=['nutrients'])

# Separar as variáveis independentes (X) e a variável dependente (y)
X = df_ml.drop('duration', axis=1)  # 'duration' é a variável target
y = df_ml['duration']

# Verificar se há dados suficientes para treinar o modelo
if len(X) < 2:
    st.warning('Dados insuficientes para treinar o modelo. Por favor, ajuste os filtros para incluir mais dados.')
    st.stop()
else:
    st.write(f'**Total de registros após filtragem:** {len(X)}')

# ================================================
# 3. Treinar o Modelo de Machine Learning
# ================================================
st.header('3. Treinar o Modelo de Machine Learning')
# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Instanciar o modelo de Random Forest Regressor
model = RandomForestRegressor()

# Treinar o modelo com os dados de treinamento
model.fit(X_train, y_train)

# Avaliar o modelo com os dados de teste
score = model.score(X_test, y_test)
st.write(f'**Acurácia do modelo (R² no conjunto de teste):** {score:.2f}')

# ================================================
# 4. Fazer Previsões com o Modelo
# ================================================
st.header('4. Fazer Previsões com o Modelo')
st.subheader('Insira os Dados para Previsão')

# Coletar entrada do usuário para previsão
temp_input = st.number_input('Temperatura (°C)', value=float(df['temperature'].mean()))
umidade_input = st.number_input('Umidade (%)', value=float(df['humidity'].mean()))
nutriente_input = st.selectbox('Nutriente', df['nutrients'].unique())

# ----------------------------------
# 4.1. Validar Entradas do Usuário
# ----------------------------------
# Inicializar variável de controle
input_error = False

# Validar temperatura
if not (-10 <= temp_input <= 50):
    st.error('A temperatura deve estar entre -10°C e 50°C.')
    input_error = True

# Validar umidade
if not (0 <= umidade_input <= 100):
    st.error('A umidade deve ser entre 0% e 100%.')
    input_error = True

# Se não houver erros nas entradas, proceder com a previsão
if not input_error:
    # ----------------------------------
    # 4.2. Preparar os Dados de Entrada
    # ----------------------------------
    # Criar um dicionário com os dados de entrada
    input_data = {
        'temperature': [temp_input],
        'humidity': [umidade_input],
        # Variáveis dummies para Nutriente
        'nutrients_fosforo': [1 if nutriente_input == 'fosforo' else 0],
        'nutrients_potassio': [1 if nutriente_input == 'potassio' else 0],
    }

    # Converter o dicionário em um DataFrame
    input_df = pd.DataFrame(input_data)

    # Garantir que todas as colunas necessárias estejam presentes
    for col in X.columns:
        if col not in input_df.columns:
            input_df[col] = 0  # Adicionar coluna com valor zero

    # Reordenar as colunas para corresponder ao conjunto de treinamento
    input_df = input_df[X.columns]

    # ----------------------------------
    # 4.3. Realizar a Previsão
    # ----------------------------------
    # Fazer a previsão com o modelo treinado
    prediction = model.predict(input_df)

    # Exibir o resultado da previsão
    st.subheader('Resultado da Previsão')
    st.write(f'**Previsão de Duração:** {prediction[0]:.2f} minutos')
