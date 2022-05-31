from tkinter import *
import random
top = Tk()
cai = Frame(top)
cai.pack()
top1 = Frame(top)
top1.pack()


def jogada(a, b):
    global simboloPlayer, posicoes, botoes
    if f'{a}{b}' in posicoes:
        botoes[a][b].configure(text=simboloPlayer)
        posicoes.remove(f"{a}{b}")
        if len(posicoes) > 1:
            al = random.randint(0, len(posicoes) - 1)
            x = int(posicoes[al][0])
            y = int(posicoes[al][1])
            posicoes.remove(f"{x}{y}")
            botoes[x][y].configure(text="O" if simboloPlayer == "X" else "X")


def inicia_jogo():
    global simboloPlayer, botoes
    botoes = []
    for i in range(3):
        fileira = []
        for j in range(3):
            exec(f'fileira.append(Button(top1, text="    ", relief="groove", border=10, font="Times 24 bold", command=lambda: jogada({i}, {j})))')
            fileira[j].grid(row=i + 1, column=j + 1, stick=N + S + W + E, pady=3)
        botoes.append(fileira)


def defsimbolo(a):
    global simboloPlayer
    simboloPlayer = a
    inicia_jogo()


botoes = []
posicoes = [f'{i}{j}' for i in range(3) for j in range(3)]
simboloPlayer = ""

label = Label(text="Escolha o seu símbolo", font='Times 14 bold')
label.pack()

btnX = Button(top1, text="X", relief='groove', border=10, font='Times 24 bold', command=lambda: defsimbolo("X"))
btnX.grid(row=1, column=1, stick=N + S + W + E, pady=3)
btnO = Button(top1, text="O", relief='groove', border=10, font='Times 24 bold', command=lambda: defsimbolo("O"))
btnO.grid(row=2, column=1, stick=N + S + W + E, pady=3)

top.title('Ga')
top.geometry("250x250+200+200")
top.mainloop()
