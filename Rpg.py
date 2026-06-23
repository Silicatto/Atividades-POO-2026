import random
def escolherCat():
    nome = input("Insira o nome do personagem: ");
    categorias = ["Bárbaro", "Bardo", "Clérigo", "Druida", "Guerreiro", "Monge", "Paladino", "Patrulheiro", "Ladino", "Feiticeiro", "Bruxo", "Mago", "Artífice"];
    categoria = random.choice(categorias);
    return print(f"Prazer, {nome}, o {categoria}! Seja bem-vindo ao RPG!")
def armar():
    quant = int(input("Quantas armas você quer? "))
    armamento = []
    armas = [["Adaga", "Físico"], ["Espada do rei Lich", "Mágico"], ["Espada longa", "Física"], ["Cajado mágico", "Mágico"], ["Martelo", "Físico"], ["Arco mágico", "Mágico"]]
    arma = 0
    x = 0
    while x < quant:
        for i in range(6):
            for j in range(2):
                arma = random.choice(armas)
        armamento.append(arma)
        x += 1
    return print(f"Suas armas serão: {armamento}")
escolherCat()
armar()