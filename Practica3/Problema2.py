def generar_password(n, alfabeto):
    def backtrack(password_actual, contador_ceros):
        print (password_actual)
        if len(password_actual) == n:
            if contador_ceros <= 1:
                print("".join(password_actual))
            return

        for symbol in alfabeto:
            if symbol == "0":
                if contador_ceros < 1:
                    password_actual.append(symbol)
                    backtrack(password_actual, contador_ceros + 1)
                    password_actual.pop()
            else:
                password_actual.append(symbol)
                backtrack(password_actual, contador_ceros)
                password_actual.pop()

    if n <= 0:
        return

    password_actual = []
    backtrack(password_actual, 0)

# Ejemplo de uso
n = 3
alfabeto = ["0", "1"]
generar_password(n, alfabeto)
