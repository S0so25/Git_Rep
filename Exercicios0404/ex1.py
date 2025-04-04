num1 = int(input("Insira os segundos: "))

print(num1 / 3600)

horas = num1//3600
seg = num1 % 3600
minutos = seg // 60

seg = seg % 60

print(f"horas: {horas}, minutos: {minutos:}, segundos: {seg}")