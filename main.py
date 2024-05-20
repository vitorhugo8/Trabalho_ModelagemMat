import math

class MetodoEncontrarRaiz:
    def __init__(self, func, tolerancia):
        self.func = func
        self.tolerancia = tolerancia

    def encontrar_raiz(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses")


class MetodoBissecao(MetodoEncontrarRaiz):
    def __init__(self, func, tolerancia, a, b):
        super().__init__(func, tolerancia)
        self.a = a
        self.b = b

    def encontrar_raiz(self):
        a, b = self.a, self.b
        iteracoes = 0
        while (b - a) / 2 > self.tolerancia:
            iteracoes += 1
            ponto_medio = (a + b) / 2
            if self.func(ponto_medio) == 0:
                return ponto_medio, iteracoes
            elif self.func(a) * self.func(ponto_medio) < 0:
                b = ponto_medio
            else:
                a = ponto_medio
        return (a + b) / 2, iteracoes


class MetodoNewtonRaphson(MetodoEncontrarRaiz):
    def __init__(self, func, derivada, tolerancia, x0):
        super().__init__(func, tolerancia)
        self.derivada = derivada
        self.x0 = x0

    def encontrar_raiz(self):
        x = self.x0
        iteracoes = 0
        while True:
            iteracoes += 1
            fx = self.func(x)
            dfx = self.derivada(x)
            if abs(fx) < self.tolerancia:
                return x, iteracoes
            x = x - fx / dfx


class MetodoFalsaPosicao(MetodoEncontrarRaiz):
    def __init__(self, func, tolerancia, a, b):
        super().__init__(func, tolerancia)
        self.a = a
        self.b = b

    def encontrar_raiz(self):
        a, b = self.a, self.b
        iteracoes = 0
        while True:
            iteracoes += 1
            fa, fb = self.func(a), self.func(b)
            c = (a * fb - b * fa) / (fb - fa)
            fc = self.func(c)
            if abs(fc) < self.tolerancia:
                return c, iteracoes
            if fa * fc < 0:
                b = c
            else:
                a = c

def main():
    func = lambda x: 2 * x**2 - 3 * x + 1
    derivada = lambda x: 4 * x - 3
    tolerancia = 0.05

    print("Olá! Por favor, selecione qual método você pretende usar para encontrar a raiz:")
    decisao = int(input("1 - Bisseção\n2 - Falsa Posição\n3 - Newton-Rapson\n\nEscolha: "))

    if decisao == 1 or decisao == 2:
        a = float(input("Digite o valor inicial a: "))
        b = float(input("Digite o valor inicial b: "))
        if decisao == 1:
            metodo = MetodoBissecao(func, tolerancia, a, b)
        else:
            metodo = MetodoFalsaPosicao(func, tolerancia, a, b)
    elif decisao == 3:
        x0 = float(input("Digite o valor inicial x0: "))
        metodo = MetodoNewtonRaphson(func, derivada, tolerancia, x0)
    else:
        print("Escolha inválida.")
        return

    raiz, iteracoes = metodo.encontrar_raiz()
    print(f"A raiz encontrada é: {raiz}")
    print(f"Número de iterações: {iteracoes}")

if __name__ == "__main__":
    main()