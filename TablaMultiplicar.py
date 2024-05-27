numero_tabla = int(input("Ingrese un número para la tabla de multiplicar (entre 1 y 10): "))
i = 1
while i <= 10:
    resultado = numero_tabla * i
    print(f"{numero_tabla}x{i}={resultado}")
    i += 1