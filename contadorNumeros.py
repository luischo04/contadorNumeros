cadena = input('Ingrese un mensaje: ')
contador = 0

for i in cadena:
    if i.isnumeric():
        contador += 1

print(f'La cantidad de numeros encontrados son: {contador} numeros')
