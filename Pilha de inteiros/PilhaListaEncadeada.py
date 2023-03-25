class No:
    def __init__(self, data):
        self.data = data
        self.proximo = None

class PilhaListaEncadeada:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
        
    def push(self, item):
        novo_no = No(item)
        novo_no.proximo = self.topo
        self.topo = novo_no
        self.tamanho += 1
        
    def pop(self):
        if self.is_empty():
            raise Exception("Pilha vazia")
        item = self.topo.data
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return item
        
    def top(self):
        if self.is_empty():
            raise Exception("Pilha vazia")
        return self.topo.data
        
    def is_empty(self):
        return self.tamanho == 0
        
    def size(self):
        return self.tamanho
