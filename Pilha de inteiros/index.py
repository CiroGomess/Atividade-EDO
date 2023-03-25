from PilhaVetor import PilhaVetor
from PilhaListaEncadeada import PilhaListaEncadeada

pilha_vetor = PilhaVetor()
pilha_lista_encadeada = PilhaListaEncadeada()

print("Inserindo elementos na pilha...")
for i in range(5):
    pilha_vetor.push(i)
    pilha_lista_encadeada.push(i)

print(f"Tamanho da pilha usando vetor: {pilha_vetor.size()}")
print(
    f"Tamanho da pilha usando lista encadeada: {pilha_lista_encadeada.size()}")

print("Removendo elementos da pilha...")
while not pilha_vetor.is_empty() and not pilha_lista_encadeada.is_empty():
    print(f"Elemento removido da pilha usando vetor: {pilha_vetor.pop()}")
    print(
        f"Elemento removido da pilha usando lista encadeada: {pilha_lista_encadeada.pop()}")

print(f"Tamanho da pilha usando vetor: {pilha_vetor.size()}")
print(
    f"Tamanho da pilha usando lista encadeada: {pilha_lista_encadeada.size()}")

try:
    print("Lendo o topo da pilha...")
    print(f"Topo da pilha usando vetor: {pilha_vetor.top()}")
    print(
        f"Topo da pilha usando lista encadeada: {pilha_lista_encadeada.top()}")
except Exception as e:
    print(f"Erro ao ler o topo da pilha: {e}")

print("Verificando se as pilhas estão vazias...")
print(f"Pilha usando vetor está vazia? {pilha_vetor.is_empty()}")
print(
    f"Pilha usando lista encadeada está vazia? {pilha_lista_encadeada.is_empty()}")
