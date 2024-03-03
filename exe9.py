
altura_degrau_cm = float(input("Digite a altura de cada degrau em cm: "))
altura_desejada_metros = float(input("Digite a altura que deseja alcançar em metros: "))

altura_degrau_metros = altura_degrau_cm / 100

num_degraus = altura_desejada_metros / altura_degrau_metros

print("Para atingir a altura desejada, você precisa subir", int(num_degraus), "degraus.")
