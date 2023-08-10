import os

def main():
#MENU
    s = 0
    while s == 0:
        print("Menu")
        x = int(input("1 - Circulo \n2 - Paralelepipedo \n3 - Sair \n"))
        if x == 1:
            os.system("cls")
            conta = int(input("1- Area \n2- Circunferencia \n3- Cilindro \n"))
            if conta == 1:
                os.system("cls")
                raio = float(input("Digite o raio: "))
                calculo = Circulo()
                calculo.calculo_area(raio)
                os.system("pause")
                os.system("cls")

                escolha = int(input("Deseja transformar esse circulo em cilindro? \n1 - Sim \n2 - Não \n"))
                if escolha == 1:
                    os.system("cls")
                    print("TRANSFORMAR CIRCULO EM CILINDRO")
                    h = float(input("Digite a altura desse cilindro: "))
                    calculo = Circulo()
                    calculo.calculo_volume_cilindro(raio, h)
                    os.system("pause")
                    os.system("cls")
                
            if conta == 2:
                os.system("cls")
                raio = float(input("Digite o raio: "))
                calculo = Circulo()
                calculo.calculo_circunferencia(raio)
                os.system("pause")
                
            if x == 2:
                s.system("cls")
                conta = int(input("1- Area da base \n2- Perimetro \n3- Volume"))
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
            break