def generar_Password(n, alfabeto):
    def backtrack(password_actual):
        print (password_actual)
        if len(password_actual) == n:
            print("".join(password_actual))
            return
        for symbol in alfabeto:
            password_actual.append(symbol)
            backtrack(password_actual)
            password_actual.pop()

    if n <= 0:
        return

    password_actual = []
    backtrack(password_actual)

#Variables de uso
n = 4
alfabeto = ["0", "1", "2", "3"]
generar_Password(n, alfabeto)
