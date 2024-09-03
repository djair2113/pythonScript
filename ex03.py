import json
import os
import statistics

# Dados do dicionário;
dictionary = {
    "dia1": 100,
    "dia2": 200,
    "dia3": 0,
    "dia4": 300,
    "dia5": 0,
    "dia6": 400,
    "dia7": 0
}

# Converte para JSON e salva em um arquivo;
object_json = json.dumps(dictionary, indent=2)
faturamento = os.path.abspath("faturamento.json")
with open(faturamento, "w") as file:
    file.write(object_json)

# Lê o arquivo JSON criado;
with open(faturamento, "r") as file:
    dados_faturamento = json.load(file)

# Converte os valores do dicionário para uma lista;
valores_faturamento = list(dados_faturamento.values())

# Filtra os valores positivos;
valores_validos = [valor for valor in valores_faturamento if valor > 0]

# Cálculos;
menor_faturamento = min(valores_validos)
maior_faturamento = max(valores_validos)
media_mensal = statistics.mean(valores_validos)
dias_acima_da_média = sum(1 for valor in valores_validos if valor > media_mensal)

# Exibe os resultados
print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_média}")