#Você foi contratado para desenvolver um sistema de cobrança de serviços de uma fábrica que vende Camisetas em atacado. Você ficou com a parte de desenvolver a interface com o funcionário. A Fábrica opera as vendas da seguinte maneira:


print("Pedro Ryan Magalhaes`a Store")


#escolher o modelo de camiseta
def escolha_modelo():
    while True:
        modelo = input("Escolha o modelo (MCS/MLS/MCE/MLE): ")
        if modelo == "MCS":
            return 1.80  # Valor unitário 
        elif modelo == "MLS":
            return 2.10  
        elif modelo == "MCE":
            return 2.90  
        elif modelo == "MLE":
            return 3.20 
        else:
            print("Modelo inválido. Tente novamente.")  

# definir o número de camisetas e aplicar desconto
def num_camisetas():
    while True:
        try:
            num = int(input("Digite o número de camisetas: "))
            if num > 20000:
                print("Quantidade não permitida. Tente novamente.")  
                continue
            elif num >= 2000:
                return num * 0.88  # 12% de desconto
            elif num >= 200:
                return num * 0.93  # 7% de desconto
            elif num >= 20:
                return num * 0.95  # 5% de desconto
            else:
                return num  # Sem desconto
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

# definir o valor do frete
def frete():
    while True:
        opcao = input("Escolha o frete (1-Transportadora/2-Sedex/0-Retirar na Fábrica): ")
        if opcao == "1":
            return 100  # Frete por transportadora
        elif opcao == "2":
            return 200  # Frete por Sedex
        elif opcao == "0":
            return 0  # Retirar na fábrica
        else:
            print("Opção de frete inválida. Tente novamente.")


if __name__ == "__main__":
    # Cálculo do total a pagar
    valor_modelo = escolha_modelo()  
    numero_camisetas = num_camisetas()  
    valor_frete = frete() 

    total = (valor_modelo * numero_camisetas) + valor_frete

    # valor total
    print(f"\nO valor total a pagar é: R$ {total}")
