#Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver o software de gerenciamento de funcionários. Este software deve ter o seguinte menu e opções: 

print("Welcome to Pedro Ryan Magalhaes's store")


lista_funcionarios = []
id_global = 12345678  # Exemplo de RU

# cadastrar um funcionário
def cadastrar_funcionario(id):
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    
    funcionario = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }
    
    lista_funcionarios.append(funcionario.copy())  # Adiciona o dicionário à lista

# consultar funcionários
def consultar_funcionarios():
    while True:
        opcao = input("Escolha uma opção: 1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor / 4. Retornar ao menu: ")
        
        if opcao == "1":
            # consultar todos os funcionários
            if lista_funcionarios:
                for func in lista_funcionarios:
                    print(f"ID: {func['id']}, Nome: {func['nome']}, Setor: {func['setor']}, Salário: R${func['salario']}")
            else:
                print("Nenhum funcionário cadastrado.")
        
        elif opcao == "2":
            
            id_consulta = int(input("Digite o ID do funcionário: "))
            funcionario_encontrado = False
            
            for func in lista_funcionarios:
                if func['id'] == id_consulta:
                    print(f"ID: {func['id']}, Nome: {func['nome']}, Setor: {func['setor']}, Salário: R${func['salario']:.2f}")
                    funcionario_encontrado = True
                    break
            
            if not funcionario_encontrado:
                print("Funcionário não encontrado.")
        
        elif opcao == "3":
            # Setor
            setor_consulta = input("Digite o setor: ")
            funcionarios_encontrados = [func for func in lista_funcionarios if func['setor'].lower() == setor_consulta.lower()]
            
            if funcionarios_encontrados:
                for func in funcionarios_encontrados:
                    print(f"ID: {func['id']}, Nome: {func['nome']}, Setor: {func['setor']}, Salário: R${func['salario']:.2f}")
            else:
                print(f"Nenhum funcionário encontrado no setor {setor_consulta}.")
        
        elif opcao == "4":
            # voltar ao menu
            return
        
        else:
            print("Opção inválida. Tente novamente.")

# opção de remover funcionário
def remover_funcionario():
    while True:
        try:
            id_remocao = int(input("Digite o ID do funcionário a ser removido: "))
            for func in lista_funcionarios:
                if func['id'] == id_remocao:
                    lista_funcionarios.remove(func)
                    print(f"Funcionário com ID {id_remocao} removido com sucesso.")
                    return
            print("Id inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

# Menu principal
if __name__ == "__main__":
    while True:
        opcao = input("Escolha uma opção: 1. Cadastrar Funcionário / 2. Consultar Funcionário / 3. Remover Funcionário / 4. Encerrar Programa: ")
        
        if opcao == "1":
            id_global += 1  
            cadastrar_funcionario(id_global)
        
        elif opcao == "2":
            consultar_funcionarios()
        
        elif opcao == "3":
            remover_funcionario()
        
        elif opcao == "4":
            print("Encerrando o programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
