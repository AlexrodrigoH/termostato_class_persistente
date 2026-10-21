import termostatus
import subprocess

print(f"Pressione (s) para subir e (n) para diminuir e (e) para sair\n")
valor = 0
valor = int(valor)
while True:
    subprocess.run("cls", shell=True)
    registrar = termostatus.temperatura(valor)
    registrar.att_temp()
    if valor < 0:
        save = termostatus.arquivo()
        save.salva_temp(valor)
    tecla = input().strip().lower()
    try:
        if tecla == "s":
            valor += 1
            registrar.temp = valor
            registrar.att_temp()
        elif tecla == "n":
            valor -= 1
            registrar.temp = valor
            registrar.att_temp()
        elif tecla == "e":
            print("Ajuste finalizado\nTemperatura Atual: ")
            registrar.att_temp()
            break
    except ValueError:
        print("Valor incorreto!\n")