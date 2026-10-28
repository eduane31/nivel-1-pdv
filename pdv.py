compras = []

while True:
    print("\n--- Nova Compra ---")
    valor_original = float(input("Digite o valor da compra em R$ (ou 0 para encerrar): "))

    if valor_original == 0:
        break

    if valor_original < 0:
        print("Aviso: O valor da compra nao pode ser negativo. Tente novamente.")
        continue

    idade = int(input("Digite a idade do cliente: "))

    if idade < 0:
        print("Aviso: A idade nao pode ser negativa. Tente novamente.")
        continue

    valor_atual = valor_original

    if idade >= 65:
        valor_atual = valor_atual * 0.80

    if valor_atual > 100:
        valor_atual = valor_atual * 0.90

    valor_final = valor_atual
    desconto_concedido = valor_original - valor_final

    print(f"Valor final da compra: R$ {valor_final:.2f}")

    compras.append({
        "original": valor_original,
        "desconto": desconto_concedido,
        "final": valor_final
    })

print("\n==========================================")
print("             RESUMO DO DIA                ")
print("==========================================")

qtd_compras = len(compras)
total_bruto = 0.0
total_descontos = 0.0
total_final = 0.0

for c in compras:
    total_bruto += c["original"]
    total_descontos += c["desconto"]
    total_final += c["final"]

print(f"Quantidade de compras registradas: {qtd_compras}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos concedidos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")
print("==========================================")