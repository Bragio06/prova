import os
import time

def elevador():
    num_andares = int(input("Informe o número de andares: "))
    andar_atual = 0
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        
        for i in range(num_andares, -1, -1):
            if i == andar_atual:
                print("0")  
            else:
                print("=")
        
        deslocamento = int(input("Informe d: "))
        
        if deslocamento == 0:
            print("Fim do programa!")
            break
        
        novo_andar = andar_atual + deslocamento
        
        if 0 <= novo_andar <= num_andares:
            andar_atual = novo_andar
        else:
            print("Deslocamento inválido! O elevador deve ficar entre 0 e", num_andares)
            time.sleep(2) 
elevador()
