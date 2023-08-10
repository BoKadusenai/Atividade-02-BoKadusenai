from Classes import *
import os

#Função que vai rodar o código
def main():
    #While (Opções de voltar e sair)
    s = 0
    while s == 0:
        #Tratamento de excessão
        try:
            print("Menu")
            x = int(input("1 - Circulo \n2 - Paralelepipedo \n3 - Sair \n"))
        
        #Caso tenha erro
        except ValueError:
            print("Digite apenas números inteiros")
            os.system("pause")
            os.system("cls")
            main()

        if x == 1:
            os.system("cls")
            #Tratamento de excessão
            try:
                conta = int(input("1- Area \n2- Circunferencia \n3- Cilindro \n"))
            except ValueError:
                print("Digite apenas números inteiros")
                os.system("pause")
                os.system("cls")
                main()

                if conta == 1:
                    os.system("cls")
                    #Tratamento de excessão
                    try:
                        raio = float(input("Digite o raio: "))
                    except ValueError:
                        print("Digite um valor numérico válido")
                        os.system("pause")
                        os.system("cls")
                        main()

                    calculo = Circulo()
                    calculo.calculo_area(raio)
                    os.system("pause")
                    os.system("cls")
                    
                    escolha = input("Deseja transformar esse circulo em cilindro? \n1 - Sim \n2 - Não \n")
                    if escolha == 1:
                        os.system("cls")
                        print("TRANSFORMAR CIRCULO EM CILINDRO")
                        try:
                            h = float(input("Digite a altura desse cilindro: "))
                        except ValueError:
                            print("Digite um valor numérico válido")
                            os.system("pause")
                            os.system("cls")
                            main()

                        calculo.calculo_volume_cilindro(raio, h)
                        os.system("pause")
                        os.system("cls")
                    
                    if escolha == 2:
                        main()

        if x == 2:
            os.system("cls")
            #Tratamento de excessão
            try:
                conta = int(input("1- Area da base \n2- Perimetro \n3- Volume"))
            except ValueError:
                print("Digite um valor numérico válido")
                os.system("pause")
                os.system("cls")
                main()
                if conta == 1:
                        os.system("cls")
                        base = float(input("Digite a medida da base: "))
                        altura = float(input("Digite a medida da altura: "))
                        calculo = Paralelepipedo()
                        calculo.calculo_area_da_base(base,altura)
                        os.system("pause")
                        
                if conta == 2:
                        os.system("cls")
                        comprimento = float(input("Digite a medida do comprimento: "))
                        largura = float(input("Digite a medida da largura: "))
                        altura = float(input("Digite a medida da altura: "))
                        calculo = Paralelepipedo()
                        calculo.calculo_perimetro(comprimento, largura, altura)
                        os.system("pause")
                        
                if conta == 3: 
                        os.system("cls")
                        ladoA = float(input("Informe a medida do primeiro lado: "))
                        ladoB = float(input("Informe a medida do segundo lado: "))
                        ladoC = float(input("Informe a medida do terceiro lado: "))
                        calculo = Paralelepipedo()
                        calculo.calculo_volume(ladoA, ladoB, ladoC)
                        os.system("pause")

        if x == 3:
            #Sair do código
            break


