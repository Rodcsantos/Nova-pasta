# vetor de faturamento diário
faturamento_diario = [100, 200, 150, 300, 250, 400, 350, 220, 180, 280, 320, 270, 240, 260, 190, 230, 210, 290, 270, 180, 320, 280, 250, 220, 300, 330, 360, 340, 230, 240]

# menor valor de faturamento diário
menor_faturamento = min(faturamento_diario)

# maior valor de faturamento diário
maior_faturamento = max(faturamento_diario)

# média mensal de faturamento diário
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

# número de dias no mês em que o faturamento diário foi superior à média mensal
dias_acima_da_media = sum(1 for f in faturamento_diario if f > media_mensal)

# exibe os resultados
print(f"Menor faturamento diário: R${menor_faturamento:.2f}")
print(f"Maior faturamento diário: R${maior_faturamento:.2f}")
print(f"Dias com faturamento diário acima da média mensal: {dias_acima_da_media}")
