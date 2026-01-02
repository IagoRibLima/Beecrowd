din = float(input())
centavos = int(round(din * 100))

notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")

for nota in notas:
    cout = centavos // nota
    centavos %= nota
    print(f"{cout} nota(s) de R$ {nota/100:.2f}")

print("MOEDAS:")

for moeda in moedas:
    cout = centavos // moeda
    centavos %= moeda
    print(f"{cout} moeda(s) de R$ {moeda/100:.2f}")
