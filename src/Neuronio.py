from src.Peso import Peso

class Neuronio:

    def __init__(self):
        self.pesos = Peso()

    def calcularSomatorio(self, padrao):
        soma = (padrao.bias * self.pesos.teta)
        soma = soma + (padrao.x1 * self.pesos.w1)
        soma = soma + (padrao.x2 * self.pesos.w2)

        return soma

    def funcaoSigmoid(self, u):
        y = 0

        y = 1/(1 + (2.71828183 ** -u))

        return y

    def calcular(self, padrao):
        # pesos2 = '\nOs pesos iniciais são: :\n   w1 = ' + str(self.pesos.w1) + '\n   w2 = ' + str(self.pesos.w2) + '\n   w3 = ' + str(self.pesos.w3)

        y = self.funcaoSigmoid(self.calcularSomatorio(padrao))

        return y

    def calcularErroSaida(self, resultadoEsperado, y):
        e = resultadoEsperado - y

        deltaDirac = y * (1 - y) * e

        return deltaDirac

    def calcularErroCamadaOculta(self, y, deltaDiracSaida, peso):

        deltaDirac = y * (1 - y) * deltaDiracSaida * peso

        return deltaDirac

    def corrigirPesos(self, padrao, deltaDirac):
        deltaw = []
        n = 0.1

        deltaw.append(n * padrao.bias * deltaDirac)
        deltaw.append(n * padrao.x1 * deltaDirac)
        deltaw.append(n * padrao.x2 * deltaDirac)

        self.pesos.teta = self.pesos.teta + deltaw[0]
        self.pesos.w1 = self.pesos.w1 + deltaw[1]
        self.pesos.w2 = self.pesos.w2 + deltaw[2]


