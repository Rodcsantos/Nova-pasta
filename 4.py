# faturamento mensal por estado
faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# calcula o faturamento total mensal
faturamento_total = sum(faturamento_por_estado.values())

# calcula o percentual de representação de cada estado
percentuais = {}
for estado, faturamento in faturamento_por_estado.items():
    percentual = faturamento / faturamento_total * 100
    percentuais[estado] = percentual

# exibe os resultados
for estado, percentual in percentuais.items():
    print(f"{estado} - {percentual:.2f}%")
