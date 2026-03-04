import time

print("=================  SEJA BEM-VINDO ===================")
print()
print("Para iniciarmos, será necessário realizar seu cadastro.")
print()

while True:
    cadastro = input("Digite 'start' para iniciar seu cadastro: ")
    if cadastro == 'start':
        break
    else:
        print("Não foi possível iniciar o cadastro. Tente novamente.")

print()
print("Agora serão solicitadas algumas informações pessoais.")
time.sleep(1)
print()

while True:
    nome = input("Informe seu nome completo: ").strip()
    if nome == '':
        break

    email = input("Informe seu e-mail: ").strip()
    if email == '':
        break

    telefone = input("Informe seu telefone para contato: ").strip()
    if telefone == '':
        break

    endereco = input("Informe seu endereço para entrega: ").strip()
    if endereco == '':
        break

    print("Cadastro realizado com sucesso.")
    break

print()
input("Pressione ENTER para continuar...")
print()

print("========== DADOS CADASTRADOS ==========")
print("Nome:", nome)
print("E-mail:", email)
print("Telefone:", telefone)
print("Endereço:", endereco)
print("=======================================")
print()

print("A seguir, apresentamos nosso cardápio de hambúrgueres.")
print()

while True:
    resposta = input("Digite 'ok' para acessar o cardápio: ")
    if resposta == 'ok':
        break
    else:
        print("Entrada inválida. Por favor, digite 'ok'.")

print()
print("========== CARDÁPIO ==========")
print("1 - Clássico Cheese - R$ 35.00")
print("2 - Bacon Smash - R$ 37.00")
print("3 - Avocado Burger - R$ 35.00")
print("4 - Blue Cheese Burger - R$ 35.40")
print("5 - Mushroom Swiss Burger - R$ 33.50")
print("6 - Spicy Jalapeño Burger - R$ 42.90")
print("7 - Veggie Burger - R$ 45.00")
print("================================")

while True:
    opcao = input("Escolha uma opção de (1) a (7): ")

    if opcao == "1":
        hamburguer_escolhido = "Clássico Cheese"
        preco_hamburguer = 35.00
        break
    elif opcao == "2":
        hamburguer_escolhido = "Bacon Smash"
        preco_hamburguer = 37.00
        break
    elif opcao == "3":
        hamburguer_escolhido = "Avocado Burger"
        preco_hamburguer = 35.00
        break
    elif opcao == "4":
        hamburguer_escolhido = "Blue Cheese Burger"
        preco_hamburguer = 35.40
        break
    elif opcao == "5":
        hamburguer_escolhido = "Mushroom Swiss Burger"
        preco_hamburguer = 33.50
        break
    elif opcao == "6":
        hamburguer_escolhido = "Spicy Jalapeño Burger"
        preco_hamburguer = 42.90
        break
    elif opcao == "7":
        hamburguer_escolhido = "Veggie Burger"
        preco_hamburguer = 45.00
        break
    else:
        print("Opção inválida. Tente novamente.")

print()
print("Hambúrguer selecionado com sucesso:", hamburguer_escolhido)
print()

print("========== ACOMPANHAMENTOS ==========")
print("1 - Batata Frita - R$ 15.00")
print("2 - Nuggets - R$ 20.00")
print("3 - Onion Rings - R$ 25.00")
print("4 - Batata com Cheddar e Bacon - R$ 30.00")
print("5 - Não desejo acompanhamento")
print("=====================================")

while True:
    acompanhamento = input("Escolha uma opção de (1) a (5): ")

    if acompanhamento == "1":
        nome_acomp = "Batata Frita"
        preco_acomp = 15.00
        break
    elif acompanhamento == "2":
        nome_acomp = "Nuggets"
        preco_acomp = 20.00
        break
    elif acompanhamento == "3":
        nome_acomp = "Onion Rings"
        preco_acomp = 25.00
        break
    elif acompanhamento == "4":
        nome_acomp = "Batata com Cheddar e Bacon"
        preco_acomp = 30.00
        break
    elif acompanhamento == "5":
        nome_acomp = "Sem acompanhamento"
        preco_acomp = 0.00
        break
    else:
        print("Opção inválida. Tente novamente.")

print()
print("========== BEBIDAS ==========")
print("1 - Coca-Cola - R$ 8.50")
print("2 - Fanta Laranja - R$ 8.50")
print("3 - Fanta Uva - R$ 8.50")
print("4 - Guaraná - R$ 8.50")
print("================================")

while True:
    bebida = input("Escolha uma opção de (1) a (4): ")

    if bebida == "1":
        nome_bebida = "Coca-Cola"
        preco_bebida = 8.50
        break
    elif bebida == "2":
        nome_bebida = "Fanta Laranja"
        preco_bebida = 8.50
        break
    elif bebida == "3":
        nome_bebida = "Fanta Uva"
        preco_bebida = 8.50
        break
    elif bebida == "4":
        nome_bebida = "Guaraná"
        preco_bebida = 8.50
        break
    else:
        print("Opção inválida. Tente novamente.")
total = preco_hamburguer + preco_acomp + preco_bebi

print()
print("=========== RELATÓRIO FINAL DO PEDIDO ===========")
print("Cliente:", nome)
print("Hambúrguer:", hamburguer_escolhido)
print("Acompanhamento:", nome_acomp)
print("Bebida:", nome_bebida)
print("-----------------------------------------------")
print("Endereço de entrega:", endereco)
print("Telefone para contato:", telefone)
print("-----------------------------------------------")
print(f"VALOR TOTAL DO PEDIDO: R$ {total:.2f}")
print("Pedido registrado com sucesso.")
print("Agradecemos pela preferência.")
print("=================================================")





