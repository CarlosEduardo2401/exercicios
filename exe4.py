# Recebe o salário do funcionário
salario = float(input("Digite o salário do funcionário: "))

# Recebe o percentual de aumento
percentual_aumento = float(input("Digite o percentual de aumento (em %): "))

# Calcula o valor do aumento
aumento = salario * (percentual_aumento / 100)

# Calcula o novo salário
novo_salario = salario + aumento

# Mostra o valor do aumento e o novo salário
print("O valor do aumento é:", aumento)
print("O novo salário do funcionário é:", novo_salario)
