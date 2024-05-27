numero_tabla = int(input("Ingrese un número para la tabla de multiplicar (entre 1 y 10): "))
for i in range(1, 11):
    resultado = numero_tabla * i
    print(f"{numero_tabla}x{i}={resultado}")