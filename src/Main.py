from src.Padrao import Padrao
from src.Neuronio import Neuronio


class Main:
    if __name__ == '__main__':
        # Instanciando a lista de dados de entradas
        padroes = []

        # Populando a lista com os dados de entrada
        # Padrao(téta,ent1,ent2,resultado)
        padroes.append(Padrao(-1, 0, 0, 0))
        padroes.append(Padrao(-1, 0, 1, 1))
        padroes.append(Padrao(-1, 1, 0, 1))
        padroes.append(Padrao(-1, 1, 1, 0))

        # Inicializando Neuronios
        neuronio3 = Neuronio()
        neuronio4 = Neuronio()
        neuronio5 = Neuronio()

        print('Os pesos iniciais são:')
        print('Neuronio 3:\n   w13: ' + str(neuronio3.pesos.w1) + '\n   w23: ' + str(neuronio3.pesos.w2) + '\n   Téta 3: ' + str(neuronio3.pesos.teta))
        print('Neuronio 4:\n   w14: ' + str(neuronio4.pesos.w1) + '\n   w24: ' + str(neuronio4.pesos.w2) + '\n   Téta 4: ' + str(neuronio4.pesos.teta))
        print('Neuronio 5:\n   w35: ' + str(neuronio5.pesos.w1) + '\n   w45: ' + str(neuronio5.pesos.w2) + '\n   Téta 5: ' + str(neuronio5.pesos.teta) + '\n')
        i = 0
        while i < 20000:
            for padrao in padroes:
                a = neuronio3.calcular(padrao)
                b = neuronio4.calcular(padrao)

                padraoSaida = Padrao(-1, a, b, padrao.d)
                c = neuronio5.calcular(padraoSaida)

                deltaDirac5 = neuronio5.calcularErroSaida(padrao.d, c)
                deltaDirac3 = neuronio3.calcularErroCamadaOculta(a, deltaDirac5, neuronio5.pesos.w1)
                deltaDirac4 = neuronio4.calcularErroCamadaOculta(b, deltaDirac5, neuronio5.pesos.w2)

                neuronio5.corrigirPesos(padraoSaida, deltaDirac5)
                neuronio3.corrigirPesos(padrao, deltaDirac3)
                neuronio4.corrigirPesos(padrao, deltaDirac4)

            i = i + 1

        print('Os pesos finais são:')
        print('Neuronio 3:\n   w13: ' + str(neuronio3.pesos.w1) + '\n   w23: ' + str(neuronio3.pesos.w2) + '\n   Téta 3: ' + str(neuronio3.pesos.teta))
        print('Neuronio 4:\n   w14: ' + str(neuronio4.pesos.w1) + '\n   w24: ' + str(neuronio4.pesos.w2) + '\n   Téta 4: ' + str(neuronio4.pesos.teta))
        print('Neuronio 5:\n   w35: ' + str(neuronio5.pesos.w1) + '\n   w45: ' + str(neuronio5.pesos.w2) + '\n   Téta 5: ' + str(neuronio5.pesos.teta) + '\n')

        print('\n\nAgora, teste o Neuronio!')
        x2 = input('Digite a primeira entrada:')
        x3 = input('Digite a segunda entrada:')

        padrao = Padrao(-1, int(x2), int(x3), 0)

        a = neuronio3.calcular(padrao)
        b = neuronio4.calcular(padrao)
        c = neuronio5.calcular(Padrao(-1, a, b, padrao.d))

        print(c)
