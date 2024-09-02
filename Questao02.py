# Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma loja que vende Marmitas de Bife Acebolado ou Filé de Frango. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto. 
 
print("Pedro Ryan Magalhaes`a Store")

#input menu para facil entendimento do usuario
def exibir_menu():
    print("\nMenu:")
    print("Tamanho P - Bife Acebolado (BA): R$ 16,00  Filé de Frango (FF): R$ 15,00")
    print("Tamanho M - Bife Acebolado (BA): R$ 18,00  Filé de Frango (FF): R$ 17,00")
    print("Tamanho G - Bife Acebolado (BA): R$ 22,00  Filé de Frango (FF): R$ 21,00")

valorTotal = 0
#while usado conforme aprendido na aula
while True:
    exibir_menu()

    sabor = input("Sabor (BA/FF): ")
    if sabor not in ["BA", "FF"]:
        print("Sabor inválido. Tente novamente")
        continue  
    
    tamanho = input("Tamanho (P/M/G): ")
    if tamanho not in ["P", "M", "G"]:
        print("Tamanho inválido. Tente novamente")
        continue  

    #variaçao da estrutura condiconal
    if sabor == "BA":
        if tamanho == "P":
            valorTotal += 16
        elif tamanho == "M":
            valorTotal += 18
        elif tamanho == "G":
            valorTotal += 22
    elif sabor == "FF":
        if tamanho == "P":
            valorTotal += 15
        elif tamanho == "M":
            valorTotal += 17
        elif tamanho == "G":
            valorTotal += 21

    
    algoMais = input("Deseja pedir mais alguma coisa? (s/n): ")
    if algoMais == "n":
        break  

#f-string
print(f"\nObrigado por comprar. O valor total é R${valorTotal}")
