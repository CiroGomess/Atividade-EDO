class PilhaVetor:
    def __init__(self, tamanho_maximo):
        self.topo = -1
        self.tamanho_maximo = tamanho_maximo
        self.vetor = [None] * tamanho_maximo

    def vazia(self):
        return self.topo == -1

    def cheia(self):
        return self.topo == self.tamanho_maximo - 1

    def inserir(self, valor):
        if self.cheia():
            print("Erro: pilha cheia")
        else:
            self.topo += 1
            self.vetor[self.topo] = valor

    def remover(self):
        if self.vazia():
            print("Erro: pilha vazia")
        else:
            valor = self.vetor[self.topo]
            self.topo -= 1
            return valor

    def topo_pilha(self):
        if self.vazia():
            print("Erro: pilha vazia")
        else:
            return self.vetor[self.topo]

    def tamanho(self):
        return self.topo + 1


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class PilhaLista:
    def __init__(self):
        self.topo = None

    def vazia(self):
        return self.topo is None

    def inserir(self, valor):
        no = No(valor)
        no.proximo = self.topo
        self.topo = no

    def remover(self):
        if self.vazia():
            print("Erro: pilha vazia")
        else:
            valor = self.topo.valor
            self.topo = self.topo.proximo
            return valor

    def topo_pilha(self):
        if self.vazia():
            print("Erro: pilha vazia")
        else:
            return self.topo.valor

    def tamanho(self):
        tamanho = 0
        no = self.topo
        while no is not None:
            tamanho += 1
            no = no.proximo
        return tamanho




pilha = PilhaVetor(5)
print(pilha.vazia())  # True
print(pilha.cheia())  # False
pilha.inserir(1)
pilha.inserir(2)
pilha.inserir(3)
print(pilha.tamanho())  # 3
print(pilha.topo_pilha())  # 3
pilha.remover()
print(pilha.tamanho())  # 2
print(pilha.topo_pilha())  # 2
print(pilha.vazia())  # False

pilha = PilhaLista()
print(pilha.vazia())  # True
pilha.inserir(1)
pilha.inserir(2)
pilha.inserir(3)
print(pilha.tamanho())  # 3
print(pilha.topo_pilha())  # 3
pilha.remover()
print(pilha.tamanho())  # 2
print(pilha.topo_pilha())  # 2
print(pilha.vazia())  # False
