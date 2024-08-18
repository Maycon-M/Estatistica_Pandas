import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

    # Trazer a média das vendas
    # Criar um gráfico de barras vertical mostrando o mês de referência e o valor
    # Criar um gráfico de linhas mostrando o mês de referência e o valor.

# Dicionário de faturamento
dict_faturamento = {
    'data_ref': [
        '2023-01-01', 
        '2020-02-01', 
        '2021-03-01', 
        '2022-04-01', 
        '2023-05-01',
        '2023-06-01', 
        '2020-07-01', 
        '2021-08-01', 
        '2022-09-01', 
        '2023-10-01',
        '2022-11-01', 
        '2023-12-01',
        ],
    'valor': [
        400000, 
        890000, 
        760000, 
        430000, 
        920000,
        340000, 
        800000, 
        500000, 
        200000, 
        900000,
        570000, 
        995000,
        ]
}

# Criando o df e transformando a coluna data_ref e typo datetime
df_faturamento = pd.DataFrame.from_dict(dict_faturamento)
df_faturamento['data_ref'] = pd.to_datetime(df_faturamento['data_ref'])

#Exibindo o valor medio
print(df_faturamento.valor.mean())

#ordenando pela coluna de data
df_faturamento = df_faturamento.sort_values('data_ref')

## gráfico de barras
plt.figure(figsize=(10,6))
plt.bar(df_faturamento['data_ref'].dt.strftime('%b/%Y'), df_faturamento['valor'], color='skyblue')
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x/1000)}k'))
plt.xlabel('Mês')
plt.ylabel('Valor')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
## grafico de linhas
plt.figure(figsize=(10,6))
plt.plot(df_faturamento['data_ref'].dt.strftime('%b/%Y'), df_faturamento['valor'], marker='o',color='skyblue')
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x/1000)}k'))
plt.xlabel('Mês')
plt.ylabel('Valor')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()