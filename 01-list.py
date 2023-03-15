class List:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        # Como a lista em Python é dinâmica, ela não pode estar cheia
        # por definição. Então, vamos sempre retornar False.
        return False

    def size(self):
        return len(self.items)

    def get(self, index):
        return self.items[index]

    def set(self, index, value):
        self.items[index] = value

    def insert(self, index, value):
        self.items.insert(index, value)

    def remove(self, index):
        return self.items.pop(index)


def main():
    lst = List()

    print("Lista vazia:", lst.is_empty())
    print("Tamanho da lista:", lst.size())

    lst.insert(0, 42)
    lst.insert(1, 13)
    lst.insert(1, 7)
    print("Elementos da lista:", [lst.get(i) for i in range(lst.size())])

    lst.set(1, 21)
    print("Elementos da lista:", [lst.get(i) for i in range(lst.size())])

    lst.remove(2)
    print("Elementos da lista:", [lst.get(i) for i in range(lst.size())])

if __name__ == '__main__':
    main()
