# Pesquisa de satisfação - TudoWeb

excelente = 0
ruim = 0

for i in range(50):
    print(f"\n--- Entrevistado {i + 1} de 50 ---")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite a opção: "))

    if opiniao == 1:
        excelente += 1
        print(f"{nome}, sua resposta foi registrada como EXCELENTE.")

    elif opiniao == 2:
        print(f"{nome}, sua resposta foi registrada como BOM.")

    elif opiniao == 3:
        ruim += 1
        print(f"{nome}, sua resposta foi registrada como RUIM.")

    else:
        print("Opção inválida.")

print("\n================================")
print("RESULTADO DA PESQUISA - TUDOWEB")
print("================================")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")
