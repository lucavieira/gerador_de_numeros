from tkinter import *
from random import randint


class Interface:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        # Titulo
        self.titulo = Label(self.primeiroContainer, text='Gerador de Numeros')
        self.titulo['font'] = ('Arial', '25', "bold")
        self.titulo.pack()

        self.deLabel = Label(self.segundoContainer, text='De: ', font=self.fontePadrao)
        self.deLabel.pack(side=LEFT)

        self.campoDe = Entry(self.segundoContainer)
        self.campoDe['width'] = 8
        self.campoDe['font'] = self.fontePadrao
        self.campoDe.pack(side=LEFT)

        self.ateLabel = Label(self.segundoContainer, text='Até: ', font=self.fontePadrao)
        self.ateLabel.pack(side=LEFT)

        self.campoAte = Entry(self.segundoContainer)
        self.campoAte['width'] = 8
        self.campoAte['font'] = self.fontePadrao
        self.campoAte.pack(side=LEFT)

        self.quantidade_numerosLabel = Label(self.terceiroContainer, text='Quantos Resultados:')
        self.quantidade_numerosLabel['font'] = ('Arial', '10', 'bold')
        self.quantidade_numerosLabel.pack()

        self.campoQuantidade = Entry(self.terceiroContainer)
        self.campoQuantidade['width'] = 10
        self.campoQuantidade['font'] = self.fontePadrao
        self.campoQuantidade.pack()

        self.gerar = Button(self.quartoContainer)
        self.gerar['text'] = 'Gerar Resultados'
        self.gerar['font'] = ('Calibri', '11', 'bold')
        self.gerar['height'] = 1
        self.gerar['width'] = 15
        self.gerar['command'] = self.gerarNumeros
        self.gerar.pack()

        self.resultado = Label(self.quartoContainer, text='GERANDO RESULTADOS')
        self.resultado['font'] = ('Arial', '10', 'bold')
        self.resultado.pack()
        self.resultadosLabel = Label(self.quartoContainer, text='')
        self.resultadosLabel['font'] = ('Arial', '10', 'bold')
        self.resultadosLabel.pack()

    def gerarNumeros(self):
        comeco = int(self.campoDe.get())
        fim = int(self.campoAte.get())
        quantidade_numeros = int(self.campoQuantidade.get())
        if quantidade_numeros == 1:
            resultado = str(randint(int(comeco), int(fim)))
            self.resultadosLabel['text'] = resultado
        else:
            numeros = list()
            for resultado in range(0, quantidade_numeros):
                numero = randint(comeco, fim)
                if numero not in numeros:
                    numeros.append(numero)
            resultado = str(numeros)
            self.resultadosLabel['text'] = resultado
