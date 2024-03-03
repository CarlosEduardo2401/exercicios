anonascimento=int(input("Digite o ano de nascimento:"))
anoatual=int(input("digite o ano atual:"))
idade_anos=anonascimento-anoatual
idade_meses=idade_anos*12
idade_dias=idade_anos*365
idade_semanas=idade_anos*52

print("A idade é de" , idade_anos, "anos")
print("A idade é de" , idade_meses, "meses")
print("A idade é de" , idade_dias, "dias")
print("A idade é de" , idade_semanas, "semanas")