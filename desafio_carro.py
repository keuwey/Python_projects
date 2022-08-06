class Carro:
    def __init__(self, velocidadeMax):
        self.velocidadeMax = velocidadeMax
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        maxima = self.velocidadeMax
        nova = self.velocidade_atual + delta
        self.velocidade_atual = nova if nova <= maxima else maxima
        return self.velocidade_atual

    def frear(self, delta=5):
        nova = self.velocidade_atual - delta
        self.velocidade_atual = nova if nova >= 0 else 0
        return self.velocidade_atual

if __name__ == '__main__':
    c1 = Carro(180)
    for i in range(25):
        print(c1.acelerar(8))
    for i in range(10):
        print(c1.frear(20))