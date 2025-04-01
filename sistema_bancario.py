menu = """

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: 
    opcao = input(menu)

    if opcao == "D":
        deposito = int(input("Digite seu deposito: "))
        if deposito > 0:
            saldo += deposito
            print("Deposito realizado com sucesso!!!")
            extrato += f"Deposito: R$ {deposito:.2f}\n"
        else:
            print("Valor invalido!! Por favor, tente novamente com um novo valor!!!")

    elif opcao == "S":
        saque = int(input("Digite o valor do seu saque: "))

        excedeu_saldo = saque > saldo

        excedeu_limite = saque > limite

        execedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou, você não tem saldo suficiente!!") 
        elif excedeu_limite:
            print('Operação falhou, O valor do saldo excedeu o limite!!')
        elif execedeu_saques:
            print("Operação falhou, numero máximo de saques execido!!") 
        elif saque > 0:
            saldo -= saque
            print("Saque realizado com sucesso!")
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é invalido")


    elif opcao == "E":
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

        print("=========================================")
        

    elif opcao == "Q":
        break

    else:
        print("Operação invalida! Por favor, selecione novamente a operação desejada.")

