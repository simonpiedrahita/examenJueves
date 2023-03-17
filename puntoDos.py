cuentas =[]
cont = 1
vueltas = int(input("Ingrese num vueltas: "))
for i in range (0, vueltas):
    cuentabanco = {}
    cuentabanco["numeroCuenta"] =cont
    cont +=1
    cuentabanco["saldo"] = int(input("Ingrese por favor un saldo: "))
    cuentas.append(cuentabanco)
listaCuentas = sorted(cuentas, key=lambda x: x["saldo"], reverse=True)
print(f"Los saldos de las cuentas bancarias de mayor a menor son:\n {listaCuentas}\n")